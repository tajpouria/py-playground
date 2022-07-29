from typing import Dict
from datetime import datetime
from airflow.decorators import dag, task


@dag(
    dag_id="dag_with_taskflow_api_v4",
    default_args={
        "owner": "tajpouria",
        "start_date": datetime(2022, 7, 28, 12),
        "schedule_interval": "@daily",
    },
)
def greet_etl():
    @task(multiple_outputs=True)
    def get_name() -> Dict[str, str]:
        return {"firstname": "Jerry", "lastname": "Fridman"}

    @task()
    def get_age() -> int:
        return 19

    @task()
    def greet(firstname: str, lastname: str, age: int) -> None:
        print(f"Hi my name is {firstname} {lastname}, and I am {age} years old!")

    name = get_name()
    age = get_age()
    greet(firstname=name["firstname"], lastname=name["lastname"], age=age)


greet_dag = greet_etl()
