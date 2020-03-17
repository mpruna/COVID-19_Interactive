# COVID-19_Interactive

Updated Corona virus status

### Possible improvements/ToDos

**The previous code was deleated**

- [ ] Use Docker/Elk-Stack for current statistics
- [ ] Use Jenkins or other automation tools to setup a hook to pull the data
- [ ] Try to predict future trends using something like Arima
- [ ] Possible use other variables as Country/Region Health care systems(try to score them)/demographics/density


Datas-ets forked from the following Gihub Repo:

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


