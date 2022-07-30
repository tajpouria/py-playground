from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python_operator import PythonOperator

default_args = {"owner": "tajpouria", "retry": 5, "retry_delay": timedelta(minutes=5)}


def get_sklearn():
    import sklearn

    print(f"scikit-learn with version {sklearn.__version__}")


with DAG(
    dag_id="dag_with_python_deps_v0",
    default_args=default_args,
    start_date=datetime(2022, 7, 29),
    schedule_interval="@daily",
) as dag:
    get_sklearn_task = PythonOperator(
        task_id="get_sklearn", python_callable=get_sklearn
    )

    get_sklearn_task
