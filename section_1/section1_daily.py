    from airflow import DAG
    from airflow.operators import BashOperator
    from datetime import datetime

    default_args = {
        'owner': 'ganwei',
        'depends_on_past': False,
        'start_date': datetime(2021, 1, 24),
        'retries': 3,
        'retry_delay': timedelta(minutes=5),
      }

    dag = DAG('section1', default_args=default_args, schedule_interval='0 1 * * *')
    t1 = BashOperator(
        task_id='section1script',
        bash_command='python /home/airflow/airflow/dags/scripts/section1.py s3://mybucket/input_data/dataset.csv s3://mybucket/output_data/',
        dag=dag
    )