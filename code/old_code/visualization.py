#!/home/anaconda3/envs/py37_covidenv/bin/python

'''Import analitics and Data modules'''

import pandas as pd
import numpy as np
import os
import sys

from plotly.offline import download_plotlyjs, init_notebook_mode, iplot
import plotly.express as px
from plotly import tools
import plotly.graph_objs as go
init_notebook_mode()
config={'showLink': False,'displayModeBar': False}
import plotly.figure_factory as ff

def get_filelist(basedir,data_dir):

    data_path = os.path.join(basedir,data_dir)
    data_list=[]
    for item in os.listdir(data_path):
        if item.endswith(".csv"):
            fn = (os.path.join(data_path, item))
            data_list.append(fn)

    return data_list

''' Main script body '''

#dir=os.getcwd()
basedir=os.path.dirname(os.getcwd())

''' Directories for time series | Data directories'''

ts_dir="COVID-19/csse_covid_19_data/csse_covid_19_time_series/"
data_dir="COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/"

times_list=get_filelist(basedir,ts_dir)
data_list=get_filelist(basedir,data_dir)


### Latest Datasets

time_recovered=pd.read_csv(times_list[0])
time_deaths=pd.read_csv((times_list[1]))
time_confirmed=pd.read_csv(times_list[1])

data=pd.read_csv(data_list[-1])




