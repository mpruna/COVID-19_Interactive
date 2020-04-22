#!/usr/bin/env python
# coding: utf-8

# In[23]:


import pandas as pd
import numpy as np
import geopandas as gdf
import matplotlib.pyplot as plt
import os
import plotly.express as px

import warnings
warnings.filterwarnings('ignore')


# In[24]:


world=gdf.read_file(gdf.datasets.get_path('naturalearth_lowres'))
world.head()

data=world[world['continent']=="Europe"]


# In[25]:


data.head()


# In[26]:


countries=data['name'].unique()


# In[27]:


contour=data[data['name'].isin(countries)]


# In[28]:


info_path = os.path.join(os.path.dirname(os.getcwd()),"COVID-19/csse_covid_19_data/csse_covid_19_daily_reports")


# In[29]:


all_files = []
for csv_file in os.listdir(info_path):
    if not csv_file.strip().endswith(".csv"): continue
    all_files.append(csv_file)
    
all_files = sorted(all_files)
for csv_file in all_files:
    if not csv_file.strip().endswith(".csv"): continue
    full_path = os.path.join(info_path, csv_file)
    df = pd.read_csv(full_path)


# In[30]:


df['Last_Update']=pd.to_datetime(df['Last_Update'])
df.sort_values(by=['Last_Update'],ascending=False).head()
eu_df=df[df['Combined_Key'].isin(countries)]
eu_df=eu_df.loc[:,['Confirmed','Deaths','Recovered','Country_Region']]


merged=eu_df.merge(contour, right_on='name',left_on='Country_Region')
merged.head()


# In[31]:


merged['iso_a3'].iloc[10]='FRA'
merged['iso_a3'].iloc[17]='UNK'
merged['iso_a3'].iloc[24]='NOR'


# In[32]:


def plot(cases,title):
    fig = px.choropleth(merged, locations="iso_a3",
                        scope="europe",
                        color=cases,
                        hover_name="name",
                        color_continuous_scale=px.colors.sequential.Plasma)
    #fig.update_layout(width=900,margin={"r":0,"t":0,"l":0,"b":0})
    fig.update_layout(width=900, height=800,
                        title_text=title,
                        title_x=0.5,
                        font_family='BalO',
                        coloraxis=dict(colorscale='Portland',
                                       showscale=False),
                        mapbox = dict(center= dict(lat=55.499998,lon=17.3833318),
                        zoom=2.55),
                        margin={"r":0,"t":0,"l":0,"b":0}                
                        )
    fig.show()


# In[33]:


cases="Confirmed"
title='Confirmed COVID-19 cases'
plot(cases,title)


# In[34]:


cases="Deaths"
title='Europe - March 21, 2020 <br>Deaths COVID-19 cases'
plot(cases,title)


# In[35]:


cases="Recovered"
title='Europe - March 21, 2020 <br>Confirmed COVID-19 cases'
plot(cases,title)


# ### GEOPANDAS | BELOW UNDER CONSTRUCTION

# In[36]:


data.crs="EPSG:2176"


# ### Focus map on continental Europe
# 
# * Make the map smaller by exluding countries at the edge of the projection
# * Remove **Rusia|Norway|Belarus|Ukraine**

# In[37]:


'''
countries=data['name'].unique().tolist()
for idx in [0,1,4,5]:
    del countries[idx]
'''


# ### Map contour

# In[38]:


contour=data[data['name'].isin(countries)]


# In[39]:


contour.head()


# In[40]:


contour.plot(figsize=(15,15), color='none', edgecolor='black', zorder=3)


# In[ ]:




