import psycopg2

def update_table():

    try:
        conn = psycopg2.connect(host="postgres", database="airflow", user="airflow", password="airflow", port='5432')
        cursor = conn.cursor()

        add_data = 'create table Docker_Data as select dag_id, execution_date from dag_run order by execution_date; '
        cursor.execute(add_data)
        conn.commit()


    except:
        print("Error in connection")
    finally:
        conn.close()
        print("No issues")