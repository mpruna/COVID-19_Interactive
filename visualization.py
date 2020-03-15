#!/home/anaconda3/envs/python_35/bin/

'''Import analytics and plotting modules'''

import pandas as pd
import numpy as np
import glob
import os

from plotly.offline import download_plotlyjs, init_notebook_mode, iplot
from plotly.subplots import make_subplots
import plotly.express as px
from plotly import tools
import plotly.graph_objs as go
init_notebook_mode()
config={'showLink': False,'displayModeBar': False}
import plotly.figure_factory as ff


basepath=os.getcwd()
print(basepath)

fp_timeseries="COVID-19/csse_covid_19_data/csse_covid_19_time_series/"
fp_dataset="COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/"

cc_map=pd.read_csv("/home/Github/COVID-19_Interactive/COVID-19/all_countries.csv")

times_dir=os.path.join(basepath,fp_timeseries)

def get_filelist(path):
    list=[]
    for item in os.listdir(path):
        if item.endswith(".csv"):
            fn = (os.path.join(path, item))
            list.append(fn)

    return list



def plot_gauge(x,title):
    fig = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = x,
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': title}))

    return fig.show()

''' Main Sort of '''
times_dir=os.path.join(basepath,fp_timeseries)
dataset_dir=os.path.join(basepath,fp_dataset)

times_list=get_filelist(path=times_dir)
dataset_list=get_filelist(path=times_dir)

times_df=pd.read_csv(times_list[-1])
print(times_df.head())