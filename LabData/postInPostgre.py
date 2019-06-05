#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  3 11:47:02 2019

@author: uby
"""
from sqlalchemy import create_engine
from geoalchemy2 import Geometry
import pandas as pd
import geopandas as gpd



engine = create_engine('postgresql://postgres:Sherlocked2112?@localhost:5432/se4g')

#input data
#df= pd.read_csv('/media/sf_Condivisa/Laboratorio/LabData/bike.csv')
df2= pd.read_csv(r'C:\Users\lawfr\Desktop\DEFINITIVO\SoftwareEng\LabData\codes.csv')
#gdf= gpd.read_file('/media/sf_Condivisa/Laboratorio/LabData/stations.shp')

#write bike and shp into Postgre
#df.to_sql('bike', engine, if_exists= 'replace', index=False)
df2.to_sql('codes', engine, if_exists= 'replace', index=False)


#gdf.to_sql('stations', engine, if_exists='replace', index=True, dtype={'geom': Geometry('POINT', srid= 4326)})