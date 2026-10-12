import os 
import pytest 


@'
import re, pathlib
names = "fact_meeting fact_client_ptcpt dim_sub_type dim_body_notes fact_event dim_sub_event fact_sub_event_attendees fact_bnpp_ptcpt".split()
for f in [p for d in ("projects","sources") for p in pathlib.Path(d).rglob("*") if p.suffix in (".yaml",".sql")]:
    s = open(f, encoding="utf-8", newline="").read()
    n = re.sub(r"(- name: (\w+)_crm_ce\r?\n)[ \t]*table_name: \2\r?\n", r"\1", s)
    for x in names:
        n = re.sub(r"(polaris\.beta\.trusted\.crm_ce\.)" + x + r"\b", r"\g<1>" + x + "_crm_ce", n, flags=re.I)
    if n != s:
        open(f, "w", encoding="utf-8", newline="").write(n); print("changed", f)
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
Select-String -Path .\projects\interactions\tasks.yaml -Pattern 'table_name:'



