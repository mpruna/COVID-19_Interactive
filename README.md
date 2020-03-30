# COVID-19_Integrative_Project

 **If I tell you what happens, it won’t happen.**
 **We are in the endgame now.**

<img src="https://media.giphy.com/media/3FQxaJJkQR8U4gdzr0/giphy.gif" alt="Your image title" aalign="center" height="450" width="750"/>

### Possible improvements/ToDos

Split Jupyter-Nb into EDA/Trend Anaylsis(Arima/FbPhrophet)
The split made to improve readability and separation of scope:

* Forecast
* Exploratory Data Analysis

### ToDos

- [ ] Split Jupyter-Notebook into EDA/Time-Analysis(Forcasting nbs)
- [ ] Use Docker/Elk-Stack for current statistics
- [ ] Use Jenkins or other automation tools to setup a hook to pull the data
- [ ] Try to predict future trends using something like Arima
- [ ] Possible use other variables such as:
    * Country/Region Health care systems(try to score them)
    * Demographics density

## **Assumptions**

Assumptions
It's not straight forward atm to come up with predictions.
It might be possible to estimate rates such as confirmed/recovered/deaths.  
    
* It's not as straight forward to compute ratios between confirmed and  (recovered/deaths). Ratios are influenced by mobility census/density  and country healthcare.
* I believe the most accurate estimation could be related with confirmed cases


**Data sets forked from the following Github Repo:**

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
├── COVID-19
├── Docs
├── Enviroment
├── environment.yml
├── guvidu
├── Images
├── project_env
└── README.md
```


