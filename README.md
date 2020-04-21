# COVID-19_Integrative_Project

### If I tell you what happens, it won’t happen. We are in the endgame now

<img src="https://media.giphy.com/media/3FQxaJJkQR8U4gdzr0/giphy.gif" alt="Your image title" aalign="center" height="450" width="750"/>


### Assumptions

It's more accurate to predict confirmed COVID cases then to predict recovery,deaths rates. It adds other layers of complexity.
First and foremost I believe that not all cases are reported, and forecasting **confirmed** cases is more reliable then forecasting **deaths,recovered** trends.

Deaths/Recovered trends depend on:
 
* Demographics 
* Region wealth
* Health care & Population density/Mobility


### Possible improvements

Split Jupyter-Notebooks into **EDA/Trend Analysis(Arima/FbPhrophet)**.
The split  is made to improve readability and separation of scope:

* Exploratory Data Analysis
* Forecast

Analytics/Forecasts are available in **Analytics_Forecasting**. Infrastructure code in **infa_code**.

### ToDos

- [X] Split Jupyter-Notebook into EDA/Time-Analysis(Forecasting nbs)
- [X] Try to predict future trends using something like Fbprophet/Arima
- [ ] Use Docker/Elk-Stack for current statistics
- [ ] Use Jenkins or other automation tools to setup a hook to pull the data
- [ ] Possible use other variables such as:
    * Country/Region Health care systems(try to score them)
    * Demographics density


### Data sets forked from the following Github Repo

* https://github.com/CSSEGISandData/COVID-19
* https://covid19.geo-spatial.org/

### Country to Continent csv datasets

* https://github.com/dbouquin/IS_608/blob/master/NanosatDB_munging/Countries-Continents.csv
* https://github.com/lukes/ISO-3166-Countries-with-Regional-Codes/blob/master/all/all.csv

### Main packages | versions

```
elasticsearch             7.5.1                      py_0    conda-forge
geopandas                 0.7.0                      py_1    conda-forge
jupyter_client            6.1.2                      py_0    conda-forge
jupyter_core              4.6.3            py37hc8dfbb8_1    conda-forge
keplergl                  0.1.2                    pypi_0    pypi
numpy                     1.18.1           py37h8960a57_1    conda-forge
pandas                    1.0.3            py37h0da4684_0    conda-forge
plotly                    4.5.4              pyh8c360ce_0    conda-forge
scipy                     1.4.1            py37h921218d_0    conda-forge
```

### Conda | PIP environments

```
conda env export | grep -v "^prefix: " > environment.yml
pip freeze > requirements.txt
```

### Project Structure

Project structure containing forked data

```
├── Analitics_Forecasting
├── COVID-19
├── Docs
├── Enviroment
├── environment.yml
├── geo_data
├── guvidu
├── Images
├── infra_code
└── README.md

### Analytics_Forecasting

├── covid-19_forecast.ipynb
├── covid_averages.ipynb
├── covid_geo_maps.ipynb
├── covid_trends_eda.ipynb
├── dataset_exporation.ipynb
├── README.md
└── Wrangled_CSVs
    ├── eu_confirmed.csv
    ├── eu_deaths.csv
    ├── eu_recovered.csv
    ├── fbp_eu_confirmed.csv
    ├── fbp_eu_deaths.csv
    └── fbp_eu_recovered.csv

### Infrastructure Code

├── elastic_pipeline_version2.py
├── elastic_pipeline_version3.py
├── pipeline_execution.txt
├── pipeline_scheduler.py
├── __pycache__
│   └── covid19.cpython-37.pyc
└── python_envs
    └── conda_env
```


