#Importing the required packages
import geopandas as gpd
import pandas as pd
from bokeh.models import ColumnDataSource, LabelSet, Select
from bokeh.plotting import figure, show, output_file
from bokeh.tile_providers import get_provider, Vendors #bokeh version 1.1
#from bokeh.tile_providers import CARTODBPOSITRON #bokeh version 1.0
from bokeh.io import curdoc
from bokeh.layouts import row

bike = pd.read_csv(r'/Users/marta/Desktop/Software/Project/SoftwareEng/graphs_prog/data/bike.csv')
d = pd.to_datetime(bike['time']).dt.dayofweek
bike['time'] = d
bike.rename(columns={'time':'day'}, inplace=True)
bike_days = bike.groupby('day', axis=0).median()

stat_names = list(bike)
del stat_names[0]
options=[]

for i in stat_names:
	#string = str(bike['date'][i])
    string = 'station %s' %i
    options.append(string)

#days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
days = list(bike_days.index)
data = ColumnDataSource({'x' : days, 'y': list(bike_days['1'])})

p2 = figure()
p2.vbar(x='x', top='y', source = data, width=0.9) 
p2.xaxis.major_label_overrides = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'} 

#Create Select Widget
select_widget = Select(options = options, value = options[0], 
				title = 'Select a station')

def callback(attr, old, new):
    column2plot = select_widget.value
    if len(column2plot) == 9:
        data.data = {'x' : days, 'y': list(bike_days[str(column2plot[-1])])}
    elif len(column2plot) == 10:
        data.data = {'x' : days, 'y': list(bike_days[str(column2plot[-2]+column2plot[-1])])}
    p2.vbar(x='x', top='y', source = data, width=0.9)

select_widget.on_change('value', callback)

layout = row(select_widget, p2)

#Output the plot
output_file("bike_stations_LA_1.html")
show(layout)
curdoc().add_root(layout) 