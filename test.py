import os 
import pytest 


sudo docker exec airflow_airflow-worker.3.6gqn997ty5pv5ha4fnmu4shh7 python -c "import os; from core.airflow import DagFactory; d=DagFactory(os.environ['DF_PIPELINES_ROOT']).generate_all_dags(); t=d['df_import_error__projects_interactions'].get_task('import_error'); print([c.cell_contents for c in t.python_callable.__closure__])"
