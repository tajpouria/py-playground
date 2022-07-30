from datetime import datetime, timedelta

from airflow import DAG
from airflow.sensors.s3_key_sensor import S3KeySensor


default_args = {"owner": "tajpouria", "retries": 5, "retry_delay": timedelta(minutes=5)}

with DAG(
    dag_id="dag_with_minio_s3",
    default_args=default_args,
    start_date=datetime(2022, 7, 29),
    schedule_interval="@daily",
) as dag:

    # Minio S3 local connection extra field
    # {
    #     "aws_access_key_id": "minioadmin",
    #     "aws_secret_access_key": "minioadmin",
    #     "host": "http://minio:9000",
    # }

    sensor_minio_s3_task = S3KeySensor(
        task_id="sensor_minio_s3",
        bucket_key="data.csv",
        bucket_name="airflow",
        aws_conn_id="minio_s3_local",
        poke_interval=5,  # Look for file every 5 seconds.
        timeout=30,  # Look for file in a 30 seconds window.
    )
