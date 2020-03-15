# COVID-19_Interactive
Updated Corona virus status

### Possible improvements/ToDos

- [ ] Automate data pull from Github, possibly with a Jenkins hook
- [ ] Post relenvat graphs on a Cloud platform **AWS/DigitalOcean**
- [ ] Implement a modular approach read data with a python script and use jupyter just for visualization



Forked the following Gihub Repo:
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

```jql
conda env export | grep -v "^prefix: " > environment.yml
```

### Project Structure

Project structure containing forked data

```
tree -L 2
.
├── all_countries.csv
├── Countries-Continents.csv
├── COVID-19
│   ├── all_countries.csv
│   ├── archived_data
│   ├── Countries-Continents.csv
│   ├── csse_covid_19_data
│   ├── README.md
│   └── who_covid_19_situation_reports
├── covid-19.ipynb
├── Images
│   ├── eu_reports.png
│   ├── newplot(1).png
│   ├── newplot(2).png
│   ├── newplot(3).png
│   ├── newplot(4).png
│   ├── newplot(5).png
│   ├── newplot(6).png
│   ├── newplot(7).png
│   ├── wordwide.png
│   └── worldwide.png
└── README.md
```

