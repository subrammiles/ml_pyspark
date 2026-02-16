
#airflow-project/
│
├── .venv/
├── airflow_home/
│   ├── dags/
│   │   └── first_dag.py
│   └── airflow.db
└── requirements.txt


# Create Virtual Environment
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows


Upgrade pip:

pip install --upgrade pip

# 📦 Install Apache Airflow (Local Dev Version)

Airflow requires a specific constraints file.

✅ Recommended install (Airflow 2.8+ example)
AIRFLOW_VERSION=2.8.4
PYTHON_VERSION=3.10
CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"

pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"


⚠️ Make sure your Python version matches the constraints file.

# ⚙️  Initialize Airflow

✅ Inside your activated .venv terminal
❌ Not in a random new terminal without the virtual environment.

Set Airflow home directory:

export AIRFLOW_HOME=$(pwd)/airflow_home

Windows:
set AIRFLOW_HOME=%cd%\airflow_home

# initialize database:

airflow db init

# Create admin user:

airflow users create \
  --username admin \
  --firstname Admin \
  --lastname User \
  --role Admin \
  --email admin@example.com \
  --password admin


# Start Airflow Locally

👉 Both terminals must have the .venv activated.
👉 They can be fresh terminals, but you must activate the virtual environment in each one.

In Terminal 1:
cd airflow-project/
source .venv/bin/activate 
export AIRFLOW_HOME=$(pwd)/airflow_home
airflow webserver --port 8080


In Terminal 2:
cd airflow-project/
source .venv/bin/activate 
export AIRFLOW_HOME=$(pwd)/airflow_home
airflow scheduler


Now open:

http://localhost:8080


Login:

Username: admin

Password: admin

🎉 Airflow is running locally!


Note: kill if previous one is running
kill -9 9714



# Create Your First DAG

Airflow automatically loads DAGs from:

AIRFLOW_HOME/dags/


Create folder:

mkdir -p airflow_home/dags


Create file:

touch airflow_home/dags/first_dag.py

# Refresh Airflow UI

Go to Airflow UI

Turn ON the DAG

Click ▶ Trigger DAG

You should see:

print_hello

print_world

Running in sequence.

🧪 Test DAG from CLI (Optional)
airflow tasks test my_first_dag print_hello 2024-01-01
