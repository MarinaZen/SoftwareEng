#Importing the required packages
import geopandas as gpd
import pandas as pd
from bokeh.models import ColumnDataSource, LabelSet, Select
from bokeh.plotting import figure, show, output_file
from bokeh.tile_providers import get_provider, Vendors #bokeh version 1.1
#from bokeh.tile_providers import CARTODBPOSITRON #bokeh version 1.0
from bokeh.io import curdoc
from bokeh.layouts import column, row
import math
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:1234@localhost:5432/se4g')
bike = pd.read_sql_table('bike',engine)
bike_1 = pd.read_sql_table('bike',engine)
bike_2 = pd.read_sql_table('bike',engine)

# #FIRST GRAPH

#bike = pd.read_csv(r'C:\Users\lawfr\Desktop\graphs_prog\data\bike.csv')
d = pd.to_datetime(bike['time']).dt.date
bike['time'] = d
bike.rename(columns={'time':'date'}, inplace=True)
#bike_dates = bike.groupby('date', axis=0)

stat_names = list(bike)
del stat_names[0]
options=[]

for i in stat_names:
	#string = str(bike['date'][i])
    string = 'Station %s' %i
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
p = figure(title='Daily trend of the number of bikes in a selected station', title_location='above', x_axis_label = 'Hour of the day', y_axis_label = 'Number of bikes', x_range=(1, 24))
p.line(x='x', y='y', source=data, color= (9, 119, 27))
p.circle(x = 'x', y = 'y', source=data, color = (9, 119, 27), size = 10, alpha = 0.8)
p.title.text_color = '#ff6347'
p.title.text_font_size = '13pt'

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
    p.line(x='x', y='y', source = data, color = (9, 119, 27)) 

#Update Select Widget to each interaction
select_widget_1.on_change('value', callback)
select_widget_2.on_change('value', callback)
select_widget_3.on_change('value', callback)

#SECOND GRAPH

#bike_1 = pd.read_csv(r'C:\Users\lawfr\Desktop\SoftwareEng\graphs_prog\data\bike_1.csv')
d_1 = pd.to_datetime(bike_1['time']).dt.dayofweek
bike_1['time'] = d_1
bike_1.rename(columns={'time':'day'}, inplace=True)
bike_1_days = bike_1.groupby('day', axis=0).median()

days_1 = list(bike_1_days.index)
data_1 = ColumnDataSource({'x_1' : days_1, 'y_1': list(bike_1_days['1'])})

p1 = figure(title='Median number of bikes for each week-day in a selected station', title_location='above', x_axis_label = 'Day of the week', y_axis_label = 'Median number of bikes')
p1.title.text_color = '#ff6347'
p1.title.text_font_size = '13pt'
p1.vbar(x='x_1', top='y_1', source = data_1, width=0.9, color = (9, 119, 27)) 
p1.xaxis.major_label_overrides = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'} 

#Create Select Widget
select_widget_4 = Select(options = options, value = options[0], 
                title = 'Select a station')

def callback_1(attr, old, new):
    column2plot_1 = select_widget_4.value
    if len(column2plot_1) == 9:
        data_1.data = {'x_1' : days_1, 'y_1': list(bike_1_days[str(column2plot_1[-1])])}
    elif len(column2plot_1) == 10:
        data_1.data = {'x_1' : days_1, 'y_1': list(bike_1_days[str(column2plot_1[-2]+column2plot_1[-1])])}
    p1.vbar(x='x_1', top='y_1', source = data_1, width=0.9, color = (9, 119, 27))

select_widget_4.on_change('value', callback_1)

#THIRD PLOT

#bike_2 = pd.read_csv(r'C:\Users\lawfr\Desktop\SoftwareEng\graphs_prog\data\bike_2.csv')
d_2 = pd.to_datetime(bike_2['time']).dt.month
bike_2['time'] = d_2
bike_2.rename(columns={'time':'month'}, inplace=True)
bike_2_months = bike_2.groupby('month', axis=0).median()

months_2 = list(bike_2_months.index)
data_2 = ColumnDataSource({'x_2' : months_2, 'y_2': list(bike_2_months['1'])})

p2 = figure(title='Median number of bikes for each month in a selected station', title_location='above', x_axis_label = 'Month of the year', y_axis_label = 'Median number of bikes')
p2.vbar(x='x_2', top='y_2', source = data_2, width=0.9, color = (9, 119, 27))
p2.title.text_color = '#ff6347'
p2.title.text_font_size = '13pt'
p2.xaxis.ticker = months_2
p2.xaxis.major_label_overrides = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep',
     10: 'Oct', 11: 'Nov', 12: 'Dec'}
p2.xaxis.major_label_orientation = math.pi/4

#Create Select Widget
select_widget_5 = Select(options = options, value = options[0], 
                title = 'Select a station')

def callback_2(attr, old, new):
    column2plot_2 = select_widget_5.value
    if len(column2plot_2) == 9:
        data_2.data = {'x_2' : months_2, 'y_2': list(bike_2_months[str(column2plot_2[-1])])}
    elif len(column2plot_2) == 10:
        data_2.data = {'x_2' : months_2, 'y_2': list(bike_2_months[str(column2plot_2[-2]+column2plot_2[-1])])}
    p2.vbar(x='x_2', top='y_2', source = data_2, width=0.9, color = (9, 119, 27))

select_widget_5.on_change('value', callback_2)

layout = column(row(column(select_widget_1, select_widget_2, select_widget_3), p), row(select_widget_4, p1), row(select_widget_5, p2))
#Output the plot
output_file("statistic.html")
show(layout)
curdoc().add_root(layout)