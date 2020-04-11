### Infrastructure/Components

Elasticsearch requirements

```
vm.max_map_count /etc/sysctl.conf
vm.max_map_count=262144
```

**This is not a priority at the moment/Focus should be directed towards building a reliable forecast**.

**.CSV data changes every day so python pipeline must be adjusted (ex: names of the columns change, new datasets were added(US datasets))**


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

Cron working.
* Exported conda environment with printenv to conda_env.
* Add conda activate command in cron job




```
# m h  dom mon dow   command
SHELL=/bin/bash
home_dir="/home/Github/COVID-19_Interactive/code"
BASH_ENV=$home_dir/conda_env
py="/home/anaconda3/envs/py37_covidenv/bin/python"
* * * * * conda activate py37_covidenv; $py $home_dir/elastic_pipeline_version3.py >> $home_dir/cron_exec.txt 2>&1
```

### Make the script to run like a daemon

Python daemon script works

```jql
service pipeline_scheduler.py status
● pipeline_scheduler.py.service
     Loaded: loaded (/etc/init.d/pipeline_scheduler.py; generated)
     Active: activating (start) since Sat 2020-04-04 23:22:19 EEST; 1min 8s ago
       Docs: man:systemd-sysv-generator(8)
Cntrl PID: 42225 (pipeline_schedu)
      Tasks: 1 (limit: 18515)
     Memory: 11.1M
     CGroup: /system.slice/pipeline_scheduler.py.service
             └─42225 /home/anaconda3/envs/py37_covidenv/bin/python /etc/init.d/pipeline_scheduler.py start

Apr 04 23:22:19 kali systemd[1]: Starting pipeline_scheduler.py.service...

Log execution
```
### Log execution:

```
At 04/04/2020, 23:22:19Local branch is up to date
At 04/04/2020, 23:22:49Local branch is up to date
At 04/04/2020, 23:23:19Local branch is up to date
At 04/04/2020, 23:23:49Local branch is up to date
At 04/04/2020, 23:24:19Local branch is up to date
```

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

### Github polling via Jenkins works

Setup a Github polling pipeline which works atm.
Config:


### POC EX

```
 > git config remote.origin.url https://github.com/CSSEGISandData/COVID-19.git # timeout=10
Fetching upstream changes from https://github.com/CSSEGISandData/COVID-19.git
 > git --version # timeout=10
 > git fetch --tags --progress -- https://github.com/CSSEGISandData/COVID-19.git +refs/heads/*:refs/remotes/origin/* # timeout=10
 > git rev-parse refs/remotes/origin/master^{commit} # timeout=10
 > git rev-parse refs/remotes/origin/origin/master^{commit} # timeout=10
Checking out Revision 376119aa4b3dbc37b863ac11d4984e480e81227b (refs/remotes/origin/master)
 > git config core.sparsecheckout # timeout=10
 > git checkout -f 376119aa4b3dbc37b863ac11d4984e480e81227b # timeout=10
Commit message: "add 3/22 and 3/30"
 > git rev-list --no-walk 376119aa4b3dbc37b863ac11d4984e480e81227b # timeout=10
Finished: SUCCESS
``` 

Scheduled git polling at 2 minutes interval works

```
Started on Mar 31, 2020 8:12:00 PM
Using strategy: Default
[poll] Last Built Revision: Revision 376119aa4b3dbc37b863ac11d4984e480e81227b (refs/remotes/origin/master)
No credentials specified
 > git --version # timeout=10
 > git ls-remote -h -- https://github.com/CSSEGISandData/COVID-19.git # timeout=10
Found 2 remote heads on https://github.com/CSSEGISandData/COVID-19.git
[poll] Latest remote head revision on refs/heads/master is: 376119aa4b3dbc37b863ac11d4984e480e81227b - already built by 2
Done. Took 0.79 sec
No changes
```




