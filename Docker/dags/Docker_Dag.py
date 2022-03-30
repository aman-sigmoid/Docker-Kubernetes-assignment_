from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from update_table_info import *
from fetch_table_info import *

default_args = {
    "owner": "Aman",
    "depends_on_past": False,
    "start_date": datetime(2022, 3, 21),
    "email": ["airflow@airflow.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(seconds=20),
}

with DAG("Docker_Assignment", default_args=default_args, schedule_interval=timedelta(1))as dag:
    t1 = PythonOperator(task_id='update_table_t', python_callable=update_table)
    
    t2 = PythonOperator(task_id='fetch_table_t', python_callable=fetch_table)

    t1 >> t2
