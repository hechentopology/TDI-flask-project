from flask import Flask, render_template, request, redirect
from bokeh.plotting import figure, output_file, show, curdoc
from bokeh.embed import server_document
from bokeh.core.properties import value 
from bokeh.layouts import row, column,WidgetBox
from bokeh.models import ColumnDataSource, CustomJS, HoverTool
from bokeh.models.widgets import Slider, TextInput
from bokeh.transform import dodge , jitter, factor_cmap
from bokeh.models.markers import Asterisk,DiamondCross  
from bokeh.server.server import Server
from tornado.ioloop import IOLoop
 
import numpy as np 
import requests
import pandas as pd
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def main():
    return redirect('/prices') 

@app.route('/prices', methods=['POST'])
def prices():
    tsymbol1 = request.form['tsymbol']
    r = requests.get('https://www.quandl.com/api/v3/datatables/WIKI/PRICES.json?ticker='+tsymbol1+'&qopts.columns=date,low,close,open,high&api_key=Y2Zioiyb9r16QRthEeyU')
    json_object = r.json()
    datalist = json_object['datatable']['data'] 
    df = pd.DataFrame(datalist)
    datess = df[df.columns[0]].tolist()
    closeprices = df[df.columns[2]].tolist()

    # output to static HTML file
    output_file("lines.html")

    # create a new plot with a title and axis labels
    plot = figure(x_axis_label='Date', x_axis_type='datetime', y_axis_label='Price', toolbar_location="above",
           toolbar_sticky=False)

    def datetime(x):
        return np.array(x, dtype=np.datetime64)

    # add a line renderer with legend and line thickness
    plot.line(datetime(datess), closeprices, legend="Closing Price", color = "#D3790A", line_width=2)


    script, div = components(plot)
    return render_template('graph.html', script=script, div=div, ticker = tsymbol1)
    # show the results


if __name__ == '__main__':
    app.run(port=33507)