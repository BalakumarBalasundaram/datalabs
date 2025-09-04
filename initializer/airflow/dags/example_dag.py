from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def hello_world():
    print("Hello from Airflow!")

with DAG("example_dag", start_date=datetime(2023,1,1), schedule_interval="@daily", catchup=False) as dag:
    task = PythonOperator(task_id="hello", python_callable=hello_world)
