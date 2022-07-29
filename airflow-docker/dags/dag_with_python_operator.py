from datetime import datetime, timedelta
from enum import Enum

from airflow.models import DAG, TaskInstance
from airflow.operators.python import PythonOperator


class Task_IDs(Enum):
    GREET = "GREET"
    GET_NAME = "GET_NAME"


def get_name(ti: TaskInstance) -> str:
    ti.xcom_push(key="first_name", value="Jerry")
    ti.xcom_push(key="last_name", value="Fridman")


def greet(age: int, ti: TaskInstance) -> None:
    first_name: str = ti.xcom_pull(task_ids=str(Task_IDs.GET_NAME), key="first_name")
    last_name: str = ti.xcom_pull(task_ids=str(Task_IDs.GET_NAME), key="last_name")
    print(f"Hi my name is {first_name} {last_name}, and I'm {age} years old!")


with DAG(
    dag_id="dag_with_python_operator_v6",
    start_date=datetime(2022, 7, 28, 12),
    schedule_interval="@daily",
    default_args={
        "owner": "tajpouria",
        "retries": 5,
        "retries_delay": timedelta(minutes=5),
    },
) as dag:
    greet_task = PythonOperator(
        task_id=str(Task_IDs.GREET),
        python_callable=greet,
        op_kwargs=({"age": 20}),
    )

    get_name_task = PythonOperator(
        task_id=str(Task_IDs.GET_NAME), python_callable=get_name
    )

    get_name_task >> greet_task
