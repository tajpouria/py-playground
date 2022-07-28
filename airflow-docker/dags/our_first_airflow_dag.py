from datetime import datetime, timedelta
from airflow import models
from airflow.operators.bash_operator import BashOperator

default_args = {"owner": "tajpouria", "retries": 5, "retry_delay": timedelta(minutes=2)}

with models.DAG(
    dag_id="our_first_dag_v7",
    description="This is our very first Airflow Dag.",
    default_args=default_args,
    start_date=datetime(2022, 7, 28, 2),
    schedule_interval="@daily",
) as dag:
    task_one = BashOperator(
        task_id="task_one", bash_command="echo 'Hello World from the Task One!'"
    )

    task_two = BashOperator(
        task_id="task_two", bash_command="echo 'Hello World from the Task Two!'"
    )

    task_three = BashOperator(
        task_id="task_three", bash_command="echo 'Hello World from the Task Three!'"
    )

    # task_one.set_downstream([task_two, task_three])

    # task_one >> task_two
    # task_one >> task_three

    task_one >> [task_two, task_three]
