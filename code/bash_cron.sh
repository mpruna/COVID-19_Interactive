#!/bin/bash
python="/home/anaconda3/envs/py37_covidenv/bin/python"
home="/home/Github/COVID-19_Interactive/code"
$python $home/elastic_pipeline_version3.py > $home/execution.log 2>&1
