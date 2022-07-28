# I followed the instruction here:
# https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html
# Just made a couple of changes to  docker compose file to remove the example DAGs
# and to use the 'LocalExecuter' Instead of 'CeleryExecuter'. (Just to make it simpler).

mkdir -p ./dags ./logs ./plugins

# On Linux, the quick-start needs to know your host user id and needs to have group id set to 0.
# Otherwise the files created in dags, logs and plugins will be created with root user
echo -e "AIRFLOW_UID=$(id -u)" >.env

# Initialize the database
docker compose up airflow-init
# The account created has the login `airflow` and the password `airflow`.

# Running Airflow
docker compose up

# Stop and remove the volumes
docker compose down -v
