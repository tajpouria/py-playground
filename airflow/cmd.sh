# Install
pip install "apache-airflow[celery]==2.3.3" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.3.3/constraints-3.8.txt"

# Init DB
export AIRFLOW_HOME=$(pwd)
airflow db init

# Create a user
airflow users create \
  --username airflow \
  --firstname airflow \
  --lastname airflow \
  --role Admin \
  --email email@example.org

# Open another session
# Start the scheduler
export AIRFLOW_HOME=$(pwd)
airflow scheduler

# Start the web server
export AIRFLOW_HOME=$(pwd)
airflow webserver
