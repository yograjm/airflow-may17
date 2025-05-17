
# DAG

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from data_processing import append_data_to_db


default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 5, 17),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'data_process_pipeline_1',
    default_args=default_args,
    schedule_interval='* * * * *',  # every minute
    catchup=False
)


process_data_task = PythonOperator(
    task_id='append_data_to_database',
    python_callable=append_data_to_db,
    dag=dag
)

