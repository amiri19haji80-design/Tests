import re, fnmatch
from pathlib import Path
import yaml



sudo docker exec -i CONTAINER_NAME python - <<'EOF'
import os, logging
logging.basicConfig(level=logging.INFO)
from core.airflow import DagFactory
dags = DagFactory(os.environ["DF_PIPELINES_ROOT"]).generate_all_dags()
t = dags["df_import_error__projects_interactions"].get_task("import_error")
print("ARGS:", t.op_args)
print("KWARGS:", t.op_kwargs)
print("DOC:", t.doc_md)
for c in (t.python_callable.__closure__ or []):
    print("CLOSURE:", c.cell_contents)
EOF
