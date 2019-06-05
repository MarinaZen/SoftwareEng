from sqlalchemy import create_engine
from geoalchemy2 import Geometry
import pandas as pd
import geopandas as gpd
# import json
# from geojson import dump

#connection with postgres
engine = create_engine('postgresql://postgres:Sherlocked2112?@localhost:5432/se4g')
#reading the tables 
codes_sql= pd.read_sql_table('codes',engine)

bike= pd.read_sql_table('bike',engine)
# print(bike_sql)
#stations_sql = gpd.GeoDataFrame.from_postgis('stations',engine, geom_col='wkb_geometry')
# print(stations_sql)
#coverting to json bike_sql
# bikeJson = bike_sql.to_json(orient='columns')
# with open('Test.json', 'w', encoding='utf8') as fp:
#     dump(bikeJson, fp, sort_keys=True, ensure_ascii=False)
# print(bikeJson)
#print(codes_sql.at[0,'PIN_codes'])


#function for converting to geojson
# def df_to_geojson(df, properties, lat='lat', lon='lon'):
    # geojson = {'type':'FeatureCollection', 'features':[]}
    # for _, row in df.iterrows():
    #     feature = {'type':'Feature',
    #                'properties':{},
    #                'geometry':{'type':'Point','coordinates':[]}}
    #     feature['geometry']['coordinates'] = [row[lon],row[lat]]
    #     for prop in properties:
    #         feature['properties'][prop] = row[prop]
    #     geojson['features'].append(feature)
    
    # return geojson
  

#definitions of the geojeson fields to push in properties
# cols = ["id", "bike_sh", "indirizzo", "stalli", "localiz", "lat", "lon"]
# stations = df_to_geojson(stations_sql, cols)
# with open('Test.geojson', 'w', encoding='utf8') as fp:
#     dump(stations, fp, sort_keys=True, ensure_ascii=False)
# print(stations)
