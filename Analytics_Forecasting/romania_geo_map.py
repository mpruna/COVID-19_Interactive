#!/usr/bin/env python
# coding: utf-8


### Import Libraries ###
import pandas as pd
import numpy as np
import geopandas as gdf
import json
import matplotlib.pyplot as plt
import os
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff

import warnings
warnings.filterwarnings('ignore')


import folium
from folium import Choropleth, Circle, Marker
from folium.plugins import HeatMap, MarkerCluster
gdf.crs="EPSG:31700"


def read_data():
	home_path="/home/Github/COVID-19_Interactive/infra_code/"
	file_list=[]
	for file in os.listdir(home_path):
    		if "ByCounty" in file:
        		print(file)
        		file_list.append(file)

	df_list=[]
	for f in file_list:
    		d=os.path.join(home_path,f)
    		d_dict=pd.read_json(d)['data'][0]
    		df=pd.DataFrame(d_dict)
    		df_list.append(df)

	df1,df2,df3=df_list[0],df_list[1],df_list[2]
	for d in df_list:
    		print(d.head(),"\n")

	return(df_list)


def add_geodata(df1):
	ro_map1=gdf.read_file('romania-counties.json')
	ro_map1['NAME_1']=ro_map1['NAME_1'].str.upper()
	ro_map1.drop(columns=['id','NL_NAME_1','VARNAME_1'],inplace=True)
	ro_map1['NAME_1'].replace({"BUCHAREST":"BUCUREȘTI"},inplace=True)
	
	total=ro_map1.merge(df1,left_on='NAME_1',right_on="county")
	total.drop(columns=['county'],inplace=True)

	return(total)

def get_statistics(df1):
	stats=df1.describe()
	stats.drop(index='count',inplace=True)
	stats.reset_index(inplace=True)
	stats.columns=['stats','total_county','total_healed','total_dead']
	
	return stats


def plot_map(total,col):
	colors = 20
	cmap = 'Blues'
	figsize = (16, 10)
	total.plot(figsize=figsize, column=col, cmap=cmap, scheme='quantiles', k=colors, legend=True)
	plt.axis('off')


def plot_table(df):
	fig=ff.create_table(df)
	return fig

### Main ###
def main():
	df_list=read_data()
	df1=df_list[0]
	
	total=add_geodata(df1)
	
	for c in ['total_county','total_healed','total_dead']:
		plot_map(total,col=c)
		name=c+".png"
		plt.savefig(name)
		
	
	df=df1[df1.columns[1:]]
	fig=plot_table(df)
	fig.write_image("county_numbers.png")
	
	df=get_statistics(df1)
	fig=plot_table(df)
	fig.write_image("general_stats.png")
	
	
		
	
if __name__=="__main__":
	main()






