#Importing the required packages
import geopandas as gpd
import pandas as pd
from bokeh.models import ColumnDataSource, LabelSet, Select
from bokeh.plotting import figure, show, output_file
from bokeh.tile_providers import get_provider, Vendors #bokeh version 1.1
#from bokeh.tile_providers import CARTODBPOSITRON #bokeh version 1.0
from bokeh.io import curdoc
from bokeh.layouts import row

bike = pd.read_csv(r'C:\Users\lawfr\Desktop\graphs_prog\data\bike.csv')
d = pd.to_datetime(bike['time']).dt.date
bike['time'] = d
bike.rename(columns={'time':'date'}, inplace=True)
#bike_dates = bike.groupby('date', axis=0)

stat_names = list(bike)
del stat_names[0]
options=[]

for i in stat_names:
	#string = str(bike['date'][i])
    string = 'station %s' %i
    options.append(string)

days = []
for i in range(1,32):
    days.append(str(i))
months = []
for i in range(1,13):
    months.append(str(i))

curr_date = pd.to_datetime('1-1-2010')

hours = list(range(1,25))
data = ColumnDataSource({'x' : hours, 'y': list(bike[bike["date"] == curr_date.date()]['1'])})

#Create the Bar plot 
p = figure(x_axis_type = 'datetime', x_axis_label = 'hour of the day', y_axis_label = 'bike')
p.line(x='x', y='y', source=data)
p.circle(x = 'x', y = 'y', source=data, color = 'blue', size = 10, alpha = 0.8)

#Create Select Widget
select_widget_1 = Select(options = options, value = options[0], 
                title = 'Select a station')
select_widget_2 = Select(options = days, value = days[0], title = 'Select a day')
select_widget_3 = Select(options = months, value = months[0], title = 'Select a month')

def callback(attr, old, new):
    column2plot = select_widget_1.value
    day2plot = select_widget_2.value
    month2plot = select_widget_3.value
    date2plot = pd.to_datetime('2010-'+str(month2plot)+'-'+str(day2plot))
    if len(column2plot) == 9:
        data.data = {'x' : hours, 'y': list(bike[bike["date"] == date2plot.date()][str(column2plot[-1])])}
    elif len(column2plot) == 10:
        data.data = {'x' : hours, 'y': list(bike[bike["date"] == date2plot.date()][str(column2plot[-2]+column2plot[-1])])}
    p.line(x='x', y='y', source = data) 

#Update Select Widget to each interaction
select_widget_1.on_change('value', callback)
select_widget_2.on_change('value', callback)
select_widget_3.on_change('value', callback)


layout = row(select_widget_1, select_widget_2, select_widget_3, p)

#Output the plot
output_file("bike_stations_LA.html")
show(layout)
curdoc().add_root(layout)