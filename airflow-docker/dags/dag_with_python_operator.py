from airflow import models
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta


def greet(name, age):
    print(f"Hi my name is {name}, and I'm {age} years old!")


with models.DAG(
    dag_id="dag_with_python_operator_v2",
    start_date=datetime(2022, 7, 28, 12),
    schedule_interval="@daily",
    default_args={
        "owner": "tajpouria",
        "retries": 5,
        "retries_delay": timedelta(minutes=5),
    },
) as dag:
    greet_task = PythonOperator(
        task_id="greet", python_callable=greet, op_kwargs=({"name": "tom", "age": 20})
    )

    greet_task
