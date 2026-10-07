import re, fnmatch
from pathlib import Path
import yaml

Select-String -Path .\projects\interactions\tasks.yaml -Pattern 'name:\s*"?(fact_meeting|fact_client_ptcpt|dim_sub_type|dim_body_notes|fact_event|dim_sub_event|fact_sub_event_attendees|fact_bnpp_ptcpt)"?\s*$' | Select-Object LineNumber, Line
