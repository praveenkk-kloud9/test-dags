from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

from datetime import datetime

import training as train

def my_func(first,second):
    print('Hello from my_func')
#    print(train.add(first,second))
 
with DAG('python_dag', description='Python DAG', schedule_interval='*/5 * * * *', start_date=datetime(2018, 11, 1), catchup=False) as dag:
	dummy_task 	= DummyOperator(task_id='dummy_task', retries=3)
	python_task	= PythonOperator(task_id='python_task', python_callable=my_func)
#	python_task	= PythonOperator(task_id='python_task', python_callable=my_func, op_kwargs={'first': 100,'second': 200})
 
	dummy_task >> python_task
