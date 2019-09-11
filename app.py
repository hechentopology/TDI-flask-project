from flask import Flask, render_template, request, redirect
from bokeh.plotting import figure, output_file, show, curdoc
from bokeh.embed import server_document, components
from bokeh.core.properties import value 
from bokeh.layouts import row, column,WidgetBox
from bokeh.models import ColumnDataSource, CustomJS, HoverTool, DatetimeTickFormatter, Range1d
from bokeh.models.widgets import Slider, TextInput
from bokeh.transform import dodge , jitter, factor_cmap
from bokeh.models.markers import Asterisk,DiamondCross  
from bokeh.server.server import Server
from tornado.ioloop import IOLoop
import quandl
import numpy as np 
import pandas as pd
from datetime import datetime

app = Flask(__name__)

quandl.ApiConfig.api_key = "XHUMj4gG2AGsnwtxWkx6" 

@app.route('/')
def main():
    return redirect('/index')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/prices', methods=['POST'])
def prices():
    tsymbol1 = request.form['tsymbol']
    month_data = quandl.get(("WIKI/"+ tsymbol1.strip()), start_date="2005-12-01", end_date="2005-12-31") 
    x = pd.to_datetime(month_data.index)
    y = month_data['Close']

    # output to static HTML file
    output_file("lines.html")

    # create a new plot with a title and axis labels
    start_date=datetime(2005,12,1)
    end_date=datetime(2005,12,31)
    p1 = figure(title=('One month stock closing price: AAPL'),plot_height = 300, plot_width = 600,
           x_axis_label='Date', x_axis_type='datetime', y_axis_label='Price',
           x_range=Range1d(start=start_date, end=end_date))
    r = p1.line(x, y, color = '#8888cc',line_width=2,alpha= 0.8)
    
    script, div = components(p1)
    return render_template('graph.html', script=script, div=div, ticker = tsymbol1)
    # show the results


if __name__ == '__main__':
    app.run(port=33507)