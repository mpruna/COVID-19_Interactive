#!/home/anaconda3/envs/py37_covidenv/bin/python

import git
import logging
from datetime import datetime
from time import sleep
import os
import subprocess


pid = "/tmp/pipeline_scheduler.pid"

def main():
    #cmd = ['/usr/bin/python', '/path/to/my/second/pythonscript.py']
    #subprocess.Popen(cmd)

    python_env="!/home/anaconda3/envs/py37_covidenv/bin/python"
    #cmd="./elastic_pipeline_version3.py"
    repo_home="/home/Github/COVID-19_Interactive/COVID-19"
    script_home = "/home/Github/COVID-19_Interactive/code/"
    log_file=open("/home/Github/COVID-19_Interactive/code/cron.log","w")
    while True:
        repo = git.Repo(repo_home)
        repo_status=repo.git.status().split("\n")[1]
        print(repo_home)
        print(repo_status)
        if "Your branch is up to date" in repo_status:
            exec_time=datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
            #logger.debug("At ",str(exec_time))
            #logger.debug("Local branch is up to date")
            log_file.write("At "+exec_time)
            log_file.write("Local branch is up to date"+"\n")

        else:
            print("there")
            exec_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
            #logger.debug("At " + str(exec_time))
            log_file.write("At "+exec_time)
            os.chdir(script_home)
            pipe_exec = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
            (output, err) = pipe_exec.communicate()
            pipeline_exec=str(output.decode()).split("\n")
            for line in pipeline_exec:
                #logger.debug(line)
                log_file.write("At " + exec_time+"\n")

        log_file.flush()
        sleep(360)
    log_file.close()

if __name__=="__main__":
    main()