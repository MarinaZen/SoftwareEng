#Importing the required packages
import geopandas as gpd
import pandas as pd
from bokeh.models import ColumnDataSource, LabelSet, Select
from bokeh.plotting import figure, show, output_file
from bokeh.tile_providers import get_provider, Vendors #bokeh version 1.1
#from bokeh.tile_providers import CARTODBPOSITRON #bokeh version 1.0
from bokeh.io import curdoc
from bokeh.layouts import row
import math

bike = pd.read_csv(r'/Users/marta/Desktop/Software/Project/SoftwareEng/graphs_prog/data/bike.csv')
d = pd.to_datetime(bike['time']).dt.month
bike['time'] = d
bike.rename(columns={'time':'month'}, inplace=True)
bike_months = bike.groupby('month', axis=0).median()

stat_names = list(bike)
del stat_names[0]
options=[]

for i in stat_names:
	#string = str(bike['date'][i])
    string = 'station %s' %i
    options.append(string)

months = list(bike_months.index)
data = ColumnDataSource({'x' : months, 'y': list(bike_months['1'])})

p3 = figure()
p3.vbar(x='x', top='y', source = data, width=0.9)
p3.xaxis.ticker = months
p3.xaxis.major_label_overrides = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep',
    10: 'Oct', 11: 'Nov', 12: 'Dec'} 
p3.xaxis.major_label_orientation = math.pi/4

#Create Select Widget
select_widget = Select(options = options, value = options[0], 
				title = 'Select a station')

def callback(attr, old, new):
    column2plot = select_widget.value
    if len(column2plot) == 9:
        data.data = {'x' : months, 'y': list(bike_months[str(column2plot[-1])])}
    elif len(column2plot) == 10:
        data.data = {'x' : months, 'y': list(bike_months[str(column2plot[-2]+column2plot[-1])])}
    p3.vbar(x='x', top='y', source = data, width=0.9)

select_widget.on_change('value', callback)

layout = row(select_widget, p3)

#Output the plot
output_file("bike_stations_LA_2.html")
show(layout)
curdoc().add_root(layout) 