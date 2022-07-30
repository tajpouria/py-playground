from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.postgres_operator import PostgresOperator

default_args = {"owner": "tajpouria", "retries": 5, "retry_delay": timedelta(minutes=5)}

with DAG(
    dag_id="dag_with_postgres_operator_v1",
    default_args=default_args,
    start_date=datetime(2022, 7, 29),
    schedule_interval="@daily",
) as dag:
    create_table_task = PostgresOperator(
        task_id="create_table",
        postgres_conn_id="postgres_local",
        sql="""
        CREATE TABLE IF NOT EXISTS dag_runs (
            dt date,
            dag_id character varying,
            primary key (dt, dag_id)
        )
    """,
    )

    delete_from_table = PostgresOperator(
        task_id="delete_from_table",
        postgres_conn_id="postgres_local",
        sql="""
        DELETE FROM dag_runs WHERE dt = '{{ ds }}' AND dag_id = '{{ dag.dag_id }}'
        """,
    )

    insert_into_table = PostgresOperator(
        task_id="insert_into_table",
        postgres_conn_id="postgres_local",
        sql="""
        INSERT INTO dag_runs (dt, dag_id) values ('{{ ds }}', '{{ dag.dag_id }}')
        """,
    )

    create_table_task >> delete_from_table >> insert_into_table
