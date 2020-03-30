# COVID-19_Integrative_Project

 **If I tell you what happens, it won’t happen.**
 **We are in the endgame now.**

<img src="https://media.giphy.com/media/3FQxaJJkQR8U4gdzr0/giphy.gif" alt="Your image title" aalign="center" height="550" width="950"/>

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


