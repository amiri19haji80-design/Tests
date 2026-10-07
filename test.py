import re, fnmatch
from pathlib import Path
import yaml

root = Path('.').resolve()
dag = yaml.safe_load(open(root / 'dags' / 'crm_interactions.yaml', encoding='utf-8'))
sel = []
groups = dag['tasks']
for v in (groups.values() if isinstance(groups, dict) else [groups]):
    sel += v if isinstance(v, list) else [v]

def in_dag(ref):
    return any(ref == s or (any(c in s for c in '*?[') and fnmatch.fnmatchcase(ref, s)) for s in sel)

PAT = re.compile(r'polaris\.(?:alpha\.\w+\.\w+|beta\.(?:trusted|post_trusted)\.\w+\.\w+)', re.I)

files = []
for top in ('sources', 'projects'):
    for name in ('app.yaml', 'tasks.yaml'):
        files += list((root / top).rglob(name))

tasks = []
for f in sorted(set(files)):
    doc = yaml.safe_load(open(f, encoding='utf-8')) or {}
    lst = doc.get('tasks') or []
    base = '.'.join(f.parent.relative_to(root).parts)
    for tk in lst:
        ref = base + ('.' + tk['name'] if len(lst) > 1 else '')
        if in_dag(ref):
            tasks.append((ref, tk, f.parent))

def produced(tk):
    name = tk.get('table_name') or tk['name']
    md = tk.get('metadata') or {}
    if tk.get('layer') == 'alpha':
        gs = tk.get('golden_source') or {}
        return f"polaris.alpha.{gs['name']}.{name}" if gs.get('name') else None
    if tk.get('layer') == 'beta':
        if tk.get('sub_layer') == 'trusted' and md.get('domain'):
            return f"polaris.beta.trusted.{md['domain']}.{name}"
        if tk.get('sub_layer') == 'post-trusted' and md.get('project'):
            return f"polaris.beta.post_trusted.{md['project']}.{name}"
    return None

def consumed(tk, d):
    out, tr = set(), (tk.get('transform') or {})
    for s in tr.get('sources') or []:
        if isinstance(s, dict) and isinstance(s.get('table'), str):
            out.add(s['table'].lower())
    txt = tr.get('sql') or ''
    if tr.get('sql_file') and (d / tr['sql_file']).exists():
        txt += (d / tr['sql_file']).read_text(encoding='utf-8', errors='ignore')
    return out | {m.lower() for m in PAT.findall(txt)}

prod = {}
for ref, tk, d in tasks:
    p = produced(tk)
    if p:
        prod.setdefault(p.lower(), ref)

edges, external, has_in = set(), set(), set()
for ref, tk, d in tasks:
    for t in consumed(tk, d):
        if t in prod:
            if prod[t] != ref:
                edges.add((prod[t], ref)); has_in.add(ref)
        else:
            external.add(t)

with open(root.parent / 'edges.yaml', 'w', encoding='utf-8', newline='\n') as fh:
    fh.write('dependencies:\n')
    for a, b in sorted(edges):
        fh.write(f'  - edge: "{a} >> {b}"\n')

print(f"TASKS IN DAG: {len(tasks)}   EDGES: {len(edges)}   -> written to ..\\edges.yaml")
print("\nREAD BUT NOT PRODUCED IN THIS DAG:")
for t in sorted(external): print("  ", t)
print("\nNON-ALPHA TASKS WITH NO UPSTREAM EDGE:")
for ref, tk, d in tasks:
    if tk.get('layer') != 'alpha' and ref not in has_in: print("  ", ref)
