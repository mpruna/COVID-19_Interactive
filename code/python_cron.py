from crontab import CronTab

my_cron = CronTab(user='root')
job = my_cron.new(command='/home/anaconda3/envs/py37_covidenv/bin/python /home/Github/COVID-19_Interactive/code/elastic_pipeline_version1.py > /home/Github/COVID-19_Interactive/code/cron.log')
job.minute.every(27)
