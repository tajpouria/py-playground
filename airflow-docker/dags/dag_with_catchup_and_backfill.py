from datetime import datetime, timedelta
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator

with DAG(
    dag_id="dag_with_catchup_and_backfill_v4",
    default_args={
        "owner": "tajpouria",
        "retries": 5,
        "retries_delay": timedelta(minutes=5),
    },
    start_date=datetime(2022, 7, 15),
    schedule_interval="@daily",
    catchup=False,
) as dag:
    task_one = BashOperator(
        task_id="task_one", bash_command="echo 'This is task NO. 1'"
    )

    task_one

# To run the Backfill:
# Attach a shell to scheduler instance (airflow-docker-airflow-scheduler-1)
# > docker exec -it <scheduler container ID> bash
# Run the Backfill (For example between Jul 15th to Jul 29th)
# > airflow dags backfill -s 2022-7-15 -e 2022-7-29
# > exit
