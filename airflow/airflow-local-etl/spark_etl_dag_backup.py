from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from etl_spark import run_etl

with DAG(
    dag_id="spark_etl_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
) as dag:

    spark_task = PythonOperator(
        task_id="run_spark_etl",
        python_callable=run_etl
    )

    spark_task
