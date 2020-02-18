import requests
import pandas as pd
import json
import numpy as np
from datetime import datetime
import io

def get_noaa_data(year,station="GHCND:USW00094728"):
    '''
    input: a year as an int or a string in YYYY format
        and a station as a string (defaut to central park)
    output: noaa daliy observations in central park for the given year,
        in a dictonary that specifies the type of observation,
        the date, etc.
    '''
    
    #setup the request
    year = str(year)
    
    Token = 'ocUDAtCqvEcffGgKoCvSFLubTEJVWDMc'
    base='https://www.ncdc.noaa.gov/cdo-web/api/v2/data?'
    datasetid='datasetid=GHCND'
    datatypeid='datatypeid=PRCP,SNWD,SNOW,TSUN,TAVG,AWND,WT09,WT14,WT07,WT01,WT17,WT06,WT05,WT02,WT11,WT22,WT04,WT13,WT16,WT08,WT18,WT03,WT19'
    limit='limit=1000'
    stationid='stationid='+station
    startdate='startdate='+year+'-01-01'
    enddate='enddate='+year+'-12-31'
    A='&'
    req = base+datasetid+A+datatypeid+A+limit+A+stationid+A+startdate+A+enddate
    #make the request
    r = requests.get(req,headers={'token':Token})
    #convert to json and keep only the relevant part
    j = r.json()
    j = j['results']
    
    
    #read the data into a df
    _df = pd.DataFrame(j)
    #drop unneeded info
    _df.drop(columns=['station', 'attributes'],inplace=True)
    #set the index to date
    _df.set_index('date',inplace=True)
    _df.index.names = ['DATE']
    #format the date
    _df.index = pd.to_datetime(_df.index)
    
    #pivot the df
    df = _df.pivot_table(values='value', index=_df.index, columns='datatype', aggfunc='first')
    
    #add the station info
    df['STATION'] = station
    #drop the datatype column
#     df.drop(columns=['datatype'],inplace=True)
    
    return df
    
