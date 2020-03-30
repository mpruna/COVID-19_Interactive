#!/home/anaconda3/envs/py37_covidenv/bin/python

import pandas as pd
import numpy as np
import subprocess
import os
import importlib.util
import git
import geopandas as gpd
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import time


'''
Load pandas from filepath
https://stackoverflow.com/questions/67631/how-to-import-a-module-given-the-full-path#67692

'''
#gdp = importlib.util.spec_from_file_location("geopandas", "/home/anaconda3/envs/py37_covidenv/lib/python3.7/site-packages/geopandas")
'''

Structure:
1. pull github data at regular intervals
2. Check Elasticsearch  is running
2. read data from File paths(Daily/Time series)
3. Manipulate data
4. Import into elasticsearch

'''

def exec_command(cmd):
    result=subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    output, err = result.communicate()

    return output,err

def check_docker(cmd):
    output,err=exec_command(cmd)
    docker_status=str(output.decode()).split("\n")

    if "active (running)" in docker_status[2]:
        print("docker service running")
    elif "Active: inactive (dead)" in docker_status[2]:
        print("docker service stopped")

def check_elasticstack():
    containers=[" elasticsearch"," kibana"]
    cmd="docker inspect --format '{{ .State.Status }}'"
    for c in containers:
        exec_cmd=cmd+ c
        output, err = exec_command(exec_cmd)
        status = str(output.decode())
        print(c,status)

def git_pull():
    dir=os.getcwd()
    git_dir=os.path.join(os.path.dirname(dir),"COVID-19/")
    g = git.cmd.Git(git_dir)
    g.pull()
    status=g.pull()
    print(status)

def read_datasets():

    cwd=os.getcwd()
    data_dir=os.path.join(cwd,"../COVID-19/csse_covid_19_data/")
    sub_fd=["csse_covid_19_time_series","csse_covid_19_daily_reports"]

    files1=[]
    daily_dir=os.path.join(data_dir,"csse_covid_19_daily_reports/")
    for file in os.listdir(daily_dir):
        if file.endswith(".csv"):
            files1.append(file)

    '''Order files get latest'''
    files1 = sorted(files1)
    df_file = files1[-1]
    daily_df=pd.read_csv(os.path.join(daily_dir,df_file))


    files2=[]
    times_dir=os.path.join(data_dir,"csse_covid_19_time_series/")
    for file in os.listdir(os.path.join(times_dir)):
        if file.endswith(".csv"):
            files2.append(file)

    files2=sorted(files2)

    '''Sugar spice and everything nice'''
    confirmed,deaths,recovered=[pd.read_csv(os.path.join(times_dir,f)) for f in files2]

    return daily_df,confirmed,deaths,recovered

def fix_missingdata(df):

    cols=df.columns
    for c in cols:
        if "FIPS" in c:
            df[c]=df[c].fillna(0)
        else:
            df[c]=df[c].fillna("Other")

    return df

def convert_todate(df):
    if "Last_Update" in df.columns.tolist():
        df['Last_Update']=pd.to_datetime(df['Last_Update'])
        return df
    else:
        df[df.columns[11:]]=pd.to_datetime(df.columns[11:])
        return df

def add_location(df):
    cols=df.columns.tolist()

    loc_cols=['name','alpha-2','alpha-3','country-code','iso_3166-2','region','sub-region']
    loc_dir = os.path.join(os.path.dirname(os.getcwd()), "COVID-19/all_countries.csv")
    loc_df = pd.read_csv(loc_dir)

    '''Slice location dataset'''
    loc_df=loc_df[loc_cols]

    '''
    if "intermediate-region-code" in cols:
        loc_df=loc_df.drop('intermediate-region-code',axis=1)
    '''

    if "Country_Region" in cols:
        df = df.merge(loc_df, left_on='Country_Region', right_on='name')
    elif "Country/Region" in cols:
        df = loc_df.merge(df, right_on='Country/Region', left_on='name')
        print(df.head(5))


    return df

def import_toelastic():
    daily_df,confirmed,deaths,recovered=read_datasets()
    dataset_list=[daily_df,confirmed,deaths,recovered]
    titles=["daily","confirmed","deaths","recovered"]

    for data,t in zip(dataset_list,titles):
        idx=t+"_index"
        doc=t+"_records"

        data=add_location(df=data)
        #print(add_location(df=data))

        null_count=data.isnull().sum().sum()
        print(t,"null count is: ",null_count)
        print("Replace missing values")
        data=fix_missingdata(df=data)
        data = convert_todate(df=data)


        es = Elasticsearch(["127.0.0.1:9200"])
        es.indices.delete(index=idx,ignore=404)  # if index exist delete it, or ignore error messages, 404=index not found
        docs = data.to_dict(orient='records')  # from dataset create a serialize object for import
        bulk(es, docs, index=idx, doc_type=doc, raise_on_error=True)  # bulk import
        es.indices.refresh()  # get import status
        print(t,es)
        time.sleep(3)

def main():
    cmd="service docker status"
    status=check_docker(cmd)
    print(status)

    status=check_elasticstack()
    print(status)

    print(git_pull())
    import_toelastic()

if __name__=="__main__":
    main()