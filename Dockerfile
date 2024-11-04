FROM apache/airflow:2.9.3

COPY airflow_local_settings.py $AIRFLOW_HOME/config/airflow_local_settings.py

