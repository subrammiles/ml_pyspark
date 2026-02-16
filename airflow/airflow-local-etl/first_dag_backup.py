from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def print_hello():
    print("Hello from Airflow!")

def print_world():
    print("World from Airflow!")

with DAG(
    dag_id="my_first_dag",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    tags=["tutorial"],
) as dag:

    task1 = PythonOperator(
        task_id="print_hello",
        python_callable=print_hello
    )

    task2 = PythonOperator(
        task_id="print_world",
        python_callable=print_world
    )

    task1 >> task2
