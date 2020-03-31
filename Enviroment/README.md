### Infrastructure/Components

Elasticsearch requrements

```
vm.max_map_count /etc/sysctl.conf
vm.max_map_count=262144
```

**!!!This is not a priority at the moment/Focus should be directed towards building a reliable forecast!!!**

* **Elastic Stack(Elasticsearch/Kibana)**
* **Jenkins**

Create multiple Github pipeline solutions:

1. cron job that executes at regular interval and send recored to Elasticsearch
2. Use Jenkins with a webhook
3. **Optional** Possibly use Gitlab/Apache Airflow

### Directory structure

```
├── docker-compose_jenkins.yml
├── docker-compose_stash.yml
├── docker-compose.yml
├── environment.yml
├── jenkins
│   └── Dockerfile
├── kibana.yml
├── README.md
└── requirements.txt
```

### Cron job

```
#* 6,12,20 * * * /home/Github/COVID-19_Interactive/code/elastic_pipeline_version1.py
HOME="/home/Github/COVID-19_Interactive/code/"
PYTHON_ENV="/home/anaconda3/envs/py37_covidenv/bin/python"
49 * * * * $PYTHON_ENV ${HOME}/elastic_pipeline_version1.py > ${HOME}/cron.log
```


