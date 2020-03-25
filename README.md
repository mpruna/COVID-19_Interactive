# COVID-19_Interactive

Updated Corona virus status

### Possible improvements/ToDos

**Split Jupyter-Nb into EDA/Trend Anaylsis(Arima/FbPhrophet)**

The split is done to improve readibility and separation of scope:
* forecaset
* exploratory Data Analysis

### Assumsions

* It's not straight forward atm to come up with predictions.
* It might be possible to estimate rates such as confirmed/recovered/deaths.
    * it't not as straight forward to compute ratios between confirmed and (recovered/deaths) as these are influenced by mobility census/density and Country health care
    * I believe the most accurate estimation could be related with confirmed cases



- [ ] Split Jupyter-Notebook into EDA/Time-Analysis(Forcasting nbs)
- [ ] Use Docker/Elk-Stack for current statistics
- [ ] Use Jenkins or other automation tools to setup a hook to pull the data
- [ ] Try to predict future trends using something like Arima
- [ ] Possible use other variables such as:

    * Country/Region Health care systems(try to score them)
    * Demographics density


Data sets forked from the following Gihub Repo:

* https://github.com/CSSEGISandData/COVID-19

### Country to Continent csv datasets

* https://github.com/dbouquin/IS_608/blob/master/NanosatDB_munging/Countries-Continents.csv
* https://github.com/lukes/ISO-3166-Countries-with-Regional-Codes/blob/master/all/all.csv

### Added opengl + jupyter lab extension

```
 pip install keplergl
Collecting keplergl
  Downloading https://files.pythonhosted.org/packages/e6/2f/27093b60328cc13a1f71aed25ee9f63c0a2094efd931a7275da33b297975/keplergl-0.1.2.tar.gz (5.4MB)
    100% |████████████████████████████████| 5.4MB 2.6MB/s 
Collecting ipywidgets<8,>=7.0.0 (from keplergl)

jupyter labextension install @jupyter-widgets/jupyterlab-manager keplergl-jupyter
Building jupyterlab assets (build:prod:minimize)
```

### +exported conda env

```
conda env export | grep -v "^prefix: " > environment.yml
pip freeze > requirements.txt
```

### Project Structure

Project structure containing forked data

```
├── code
│   ├── COVID-19_Notebook.ipynb
│   ├── covid-19_thrends.ipynb
│   ├── docker-compose.yml
│   ├── __pycache__
│   ├── visualization.py
│   └── visualization.pyc
├── COVID-19
│   ├── all_countries.csv
│   ├── archived_data
│   ├── Countries-Continents.csv
│   ├── csse_covid_19_data
│   ├── README.md
│   └── who_covid_19_situation_reports
├── Enviroment
│   ├── docker-compose_stash.yml
│   ├── docker-compose.yml
│   ├── environment.yml
│   ├── kibana.yml
│   └── requirements.txt
├── environment.yml
├── Images
├── project_env
│   ├── bin
│   ├── include
│   ├── lib
│   ├── lib64 -> lib
│   └── pyvenv.cfg
└── README.md


5 directories, 7 files
```


