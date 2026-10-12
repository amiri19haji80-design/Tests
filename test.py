@'
p = r"..\gen_edges.py"
s = open(p, encoding="utf-8", newline="").read()
for old, new in [
    ("prod.setdefault(p.lower(), ref)", "prod.setdefault(p.lower(), []).append(ref)"),
    ("if prod[t] != ref:", "for src in [x for x in prod[t] if x != ref]:"),
    ("edges.add((prod[t], ref))", "edges.add((src, ref))"),
]:
    if s.count(old) != 1:
        raise SystemExit(f"ABORT: {old!r} found {s.count(old)} times")
    s = s.replace(old, new)
open(p, "w", encoding="utf-8", newline="").write(s)
print("patched")
'@ | python -





python ..\gen_edges.py



@'
p = r"dags\crm_interactions.yaml"
new = open(r"..\edges.yaml", encoding="utf-8").read().rstrip("\n").split("\n")
lines = open(p, encoding="utf-8", newline="").read().split("\n")
starts = [i for i, l in enumerate(lines) if l.rstrip("\r") == "dependencies:"]
if len(starts) != 1:
    raise SystemExit(f"ABORT: dependencies: found {len(starts)} times")
i = starts[0]; j = i + 1
while j < len(lines) and (lines[j].strip() == "" or lines[j][0] in " \t-"):
    j += 1
out = lines[:i] + new + ([""] + lines[j:] if j < len(lines) else [""])
open(p, "w", encoding="utf-8", newline="").write("\n".join(out))
print("replaced", j - i - 1, "old lines with", len(new) - 1, "edges")
'@ | python -




git diff --stat
(Select-String -Path .\dags\crm_interactions.yaml -Pattern '- edge:').Count
Select-String -Path .\dags\crm_interactions.yaml -Pattern 'crm_ce' | Select-Object -First 10 LineNumber, Line



