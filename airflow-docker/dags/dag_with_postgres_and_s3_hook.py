import os
import csv
import logging
from datetime import datetime, timedelta

from airflow import DAG
from airflow.exceptions import AirflowSkipException
from airflow.hooks.postgres_hook import PostgresHook
from airflow.hooks.S3_hook import S3Hook
from airflow.operators.python_operator import PythonOperator

default_args = {
    "owner": "tajpouria",
    "retries": 5,
    "retries_delay": timedelta(minutes=10),
}


def postgres_to_text(ds_nodash, next_ds_nodash, ds):
    """Query data from Postgres DB and store as text file."""
    hook = PostgresHook("postgres_shop_local")
    conn = hook.get_conn()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM public.orders WHERE dt >= %s AND dt < %s",
        (ds_nodash, next_ds_nodash),
    )
    if cursor.rowcount == 0:
        logging.info(f"Orders count for date {ds} are zero thus skipping it.")
        raise AirflowSkipException

    filename = f"dags/get_orders_{ds_nodash}.report"

    with open(filename, "w") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow([i[0] for i in cursor.description])
        csv_writer.writerows(cursor)
    cursor.close()
    conn.close()
    logging.info(f"Saved orders data for date {ds} in text file: {filename}")


def text_to_s3(ds_nodash, ds):
    filename = f"dags/get_orders_{ds_nodash}.report"

    if not os.path.exists(filename):
        logging.info(f"Skipping {ds} cuz {filename} doesn't exists.")
        raise AirflowSkipException

    hook = S3Hook(
        aws_conn_id="minio_s3_local",
    )
    key = f"orders/{ds_nodash}.csv"
    hook.load_file(
        filename=filename,
        key=key,
        bucket_name="airflow",
        replace=True,
    )
    logging.info(f"Load orders data for date {ds} in target bucket as object: {key}")


def delete_text(ds_nodash, ds):
    filename = f"dags/get_orders_{ds_nodash}.report"

    if not os.path.exists(filename):
        logging.info(f"Skipping {ds} cuz {filename} doesn't exists.")
        raise AirflowSkipException

    os.remove(filename)
    logging.info(f"Deleted text file: {filename}")


with DAG(
    dag_id="dag_with_postgres_and_s3_hook_v8",
    default_args=default_args,
    start_date=datetime(2022, 6, 25),
    schedule_interval="@daily",
) as dag:
    postgres_to_text_task = PythonOperator(
        task_id="postgres_to_text", python_callable=postgres_to_text
    )

    text_to_s3_task = PythonOperator(
        task_id="text_to_s3_task", python_callable=text_to_s3
    )

    delete_text_task = PythonOperator(
        task_id="delete_text", python_callable=delete_text
    )

    postgres_to_text_task >> text_to_s3_task >> delete_text_task
