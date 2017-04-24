#! python3
# A script to create a time axis chart from JSON data.

import json
import numpy as np
from bokeh.plotting import figure, output_file, show
from bokeh.embed import file_html
from bokeh.io import show, save
from dateutil import parser

def application():
    # prepare some data
    # aapl = np.array(AAPL['adj_close'])
    # aapl_dates = np.array(AAPL['date'], dtype=np.datetime64)
    with open('data.json') as data_file:
        data = json.load(data_file)

    timestampArray = []
    dataArray = []
    dataArray.append([])
    dataArray.append([])
    dataArray.append([])
    dataArray.append([])
    dataArray.append([])
    dataArray.append([])
    dataArray.append([])
    dataArray.append([])
    dataArray.append([])
    dataArray.append([])
    dataArray.append([])
    dataArray.append([])

    # Get data

    # convertedArray = [map(int, x) for x in rawArray]
    # aapl = np.array(convertedArray)

    # Get timestamp from
    # "2016-07-01_12:30:26"
    # rawDateArray = data[0]['Timestamp']
    for d in data:
        timestampArray.append(parser.parse(d['Timestamp'], fuzzy=True))
        dataArray[0].append(float(d['Data1']))
        dataArray[1].append(float(d['Data2']))
        dataArray[2].append(float(d['Data3']))
        dataArray[3].append(float(d['Data4']))
        dataArray[4].append(float(d['Data5']))
        dataArray[5].append(float(d['Data6']))
        dataArray[6].append(float(d['Data7']))
        dataArray[7].append(float(d['Data8']))
        dataArray[8].append(float(d['Data9']))
        dataArray[9].append(float(d['Data10']))
        dataArray[10].append(float(d['Data11']))
        dataArray[11].append(float(d['Data12']))

    print(timestampArray)
    print(dataArray)
    aapl_dates = np.array(timestampArray)
    # aapl = np.array(dataArray)

    window_size = 20
    window = np.ones(window_size)/float(window_size)

    # output to static HTML file
    output_file("OD_Data.html", title="CreateChart.py example", mode='inline')

    # create a new plot with a a datetime axis type
    p = figure(width=900, height=500, x_axis_type="datetime")

    # add renderers
    p.line(aapl_dates, np.array(dataArray[0]), color='Black', legend='Data1')
    p.circle(aapl_dates, np.array(dataArray[0]), size=4, fill_color='Black')

    p.line(aapl_dates, np.array(dataArray[1]), color='Blue', legend='Data2')
    p.circle(aapl_dates, np.array(dataArray[1]), size=4, fill_color='Blue')

    p.line(aapl_dates, np.array(dataArray[2]), color='Chartreuse', legend='Data3')
    p.circle(aapl_dates, np.array(dataArray[2]), size=4, fill_color='Chartreuse')

    p.line(aapl_dates, np.array(dataArray[3]), color='Crimson', legend='Data4')
    p.circle(aapl_dates, np.array(dataArray[3]), size=4, fill_color='Crimson')

    p.line(aapl_dates, np.array(dataArray[4]), color='DarkGreen', legend='Data5')
    p.circle(aapl_dates, np.array(dataArray[4]), size=4, fill_color='DarkGreen')

    p.line(aapl_dates, np.array(dataArray[5]), color='DarkOrange', legend='Data6')
    p.circle(aapl_dates, np.array(dataArray[5]), size=4, fill_color='DarkOrange')

    p.line(aapl_dates, np.array(dataArray[6]), color='DarkViolet', legend='Data7')
    p.circle(aapl_dates, np.array(dataArray[6]), size=4, fill_color='DarkViolet')

    p.line(aapl_dates, np.array(dataArray[7]), color='DeepPink', legend='Data8')
    p.circle(aapl_dates, np.array(dataArray[7]), size=4, fill_color='DeepPink')

    p.line(aapl_dates, np.array(dataArray[8]), color='GoldenRod', legend='Data9')
    p.circle(aapl_dates, np.array(dataArray[8]), size=4, fill_color='GoldenRod')

    p.line(aapl_dates, np.array(dataArray[9]), color='MediumSlateBlue', legend='Data10')
    p.circle(aapl_dates, np.array(dataArray[9]), size=4, fill_color='MediumSlateBlue')

    p.line(aapl_dates, np.array(dataArray[10]), color='Olive', legend='Data12')
    p.circle(aapl_dates, np.array(dataArray[10]), size=4, fill_color='Olive')

    p.line(aapl_dates, np.array(dataArray[11]), color='Sienna', legend='Data12')
    p.circle(aapl_dates, np.array(dataArray[11]), size=4, fill_color='Sienna')

    # NEW: customize by setting attributes
    p.title.text = "OD Data Readings"
    p.legend.location = "top_left"
    p.grid.grid_line_alpha = 0
    p.xaxis.axis_label = 'Date'
    p.yaxis.axis_label = 'OD'
    p.ygrid.band_fill_color = "olive"
    p.ygrid.band_fill_alpha = 0.1

    # show the results
    show(p)
    return

# If this program is the primary executable, then run the main loop
if __name__ == '__main__':
    application()
