import re, fnmatch
from pathlib import Path
import yaml


@'
import re
p = r"projects\interactions\tasks.yaml"
targets = [(472,"fact_meeting"),(489,"fact_client_ptcpt"),(506,"dim_sub_type"),(523,"dim_body_notes"),(540,"fact_event"),(558,"dim_sub_event"),(575,"fact_sub_event_attendees"),(592,"fact_bnpp_ptcpt")]
with open(p, encoding="utf-8", newline="") as f:
    lines = f.readlines()
for ln, n in targets:
    if not re.match(r"^\s*- name: " + n + r"\r?\n$", lines[ln-1]):
        raise SystemExit(f"ABORT line {ln}: {lines[ln-1]!r}")
for ln, n in sorted(targets, reverse=True):
    m = re.match(r"^(\s*)- name: " + n + r"(\r?\n)$", lines[ln-1])
    ind, eol = m.group(1), m.group(2)
    lines[ln-1] = f"{ind}- name: {n}_crm_ce{eol}"
    lines.insert(ln, f"{ind}  table_name: {n}{eol}")
with open(p, "w", encoding="utf-8", newline="") as f:
    f.writelines(lines)
print("done")
'@ | python -




git diff --stat
Select-String -Path .\projects\interactions\tasks.yaml -Pattern '_crm_ce$|table_name:' | Select-Object LineNumber, Line
