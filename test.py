import re, fnmatch
from pathlib import Path
import yaml



python -c "p='dags/crm_interactions.yaml'; d=open(p,encoding='utf-8').read(); e=open('../edges.yaml',encoding='utf-8').read(); e=e if e.lstrip().startswith('dependencies:') else 'dependencies:\n'+e; print('already there') if 'dependencies:' in d else open(p,'w',encoding='utf-8',newline='\n').write(d.rstrip('\n')+'\n\n'+e)"
