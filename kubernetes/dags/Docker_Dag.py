import imp
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import psycopg2

default_args = {
    "owner": "Aman",
    "depends_on_past": False,
    "start_date": datetime(2022, 3, 30),
    "email": ["airflow@airflow.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(seconds=20),
}
def update_table():

    try:
        conn = psycopg2.connect(host="postgres-service-db", database="airflow", user="airflow", password="airflow", port='5432')
        cursor = conn.cursor()

        add_data = 'create table Docker_Data as select dag_id, execution_date from dag_run order by execution_date; '
        cursor.execute(add_data)
        conn.commit()


    except:
        print("Error in connection")
    finally:
        conn.close()
        print("No issues")

def fetch_table():

    try:
        conn = psycopg2.connect(host="postgres-service-db", database="airflow", user="airflow", password="airflow", port='5432')
        cursor = conn.cursor()

        query = 'select * from Docker_Data;'
        cursor.execute(query)
        data = cursor.fetchall()
        print("This is Data Execution time for every DAG runs :- ")
        for i in data:
            print(i)
        print("Data Fetched to the Console Successfully")


    except:
        print("Error in connection")
    finally:
        conn.close()
        print("No issues")


with DAG("Docker_Assignment", default_args=default_args, schedule_interval=timedelta(1))as dag:
    t1 = PythonOperator(task_id='update_table_t', python_callable=update_table)
    
    t2 = PythonOperator(task_id='fetch_table_t', python_callable=fetch_table)

    t1 >> t2
