### Infrastructure/Components

Elasticsearch requrements

```
vm.max_map_count /etc/sysctl.conf
vm.max_map_count=262144
```

**This is not a priority at the moment/Focus should be directed towards building a reliable forecast**.

**.CSV data changes every day so python pipeline must be adjusted (ex: names of the columns change, new datasets are added(US))**


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

### Scheduling

Multiple options:
1. setup a cron job
2. Setup the script as a service daemon

### Cron job

At the moment script execution is not sent to a log

```
#* 6,12,20 * * * /home/Github/COVID-19_Interactive/code/elastic_pipeline_version1.py
HOME="/home/Github/COVID-19_Interactive/code/"
PYTHON_ENV="/home/anaconda3/envs/py37_covidenv/bin/python"
49 * * * * $PYTHON_ENV ${HOME}/elastic_pipeline_version1.py > ${HOME}/cron.log
```

### Make the script to run like a daemon

Setup steps:

```
update-rc.d script_namel.sh defaults
systemctl daemon-reload

service [ServiceName] start
service [ServiceName] stop
service [ServiceName] restart

service [ServiceName] status
```

Need to change the **path/home** variable as at the moment in point to the folder where the script is running.

```jql
service elastic_pipeline_version2.py status
● elastic_pipeline_version2.py.service
     Loaded: loaded (/etc/init.d/elastic_pipeline_version2.py; generated)
     Active: failed (Result: exit-code) since Tue 2020-03-31 21:30:35 EEST; 43s ago
       Docs: man:systemd-sysv-generator(8)
    Process: 7214 ExecStart=/etc/init.d/elastic_pipeline_version2.py start (code=exited, status=1/FAILURE)

Mar 31 21:30:35 kali elastic_pipeline_version2.py[7214]:     return lambda *args, **kwargs: self._call_process(name, *args, **kwargs)
Mar 31 21:30:35 kali elastic_pipeline_version2.py[7214]:   File "/home/anaconda3/envs/py37_covidenv/lib/python3.7/site-packages/git/cmd.py", line 1005, in _call_process
Mar 31 21:30:35 kali elastic_pipeline_version2.py[7214]:     return self.execute(call, **exec_kwargs)
Mar 31 21:30:35 kali elastic_pipeline_version2.py[7214]:   File "/home/anaconda3/envs/py37_covidenv/lib/python3.7/site-packages/git/cmd.py", line 735, in execute
Mar 31 21:30:35 kali elastic_pipeline_version2.py[7214]:     raise GitCommandNotFound(command, err)
Mar 31 21:30:35 kali elastic_pipeline_version2.py[7214]: git.exc.GitCommandNotFound: Cmd('git') not found due to: FileNotFoundError('[Errno 2] No such file or directory: '/COVID-19': '/COVID-19'')
Mar 31 21:30:35 kali elastic_pipeline_version2.py[7214]:   cmdline: git pull
Mar 31 21:30:35 kali systemd[1]: elastic_pipeline_version2.py.service: Control process exited, code=exited, status=1/FAILURE
Mar 31 21:30:35 kali systemd[1]: elastic_pipeline_version2.py.service: Failed with result 'exit-code'.
Mar 31 21:30:35 kali systemd[1]: Failed to start elastic_pipeline_version2.py.service.
(py37_covidenv) root@kali:/home/Github/COVID-19_Interactive/code# update-rc.d elastic_pipeline_version2.py remove
```
