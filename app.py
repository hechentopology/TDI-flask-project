from flask import Flask, render_template, request, redirect
from bokeh.plotting import figure, output_file, show, curdoc
from bokeh.embed import server_document, components
from bokeh.core.properties import value 
from bokeh.layouts import row, column
from bokeh.models import ColumnDataSource, CustomJS, HoverTool, DatetimeTickFormatter, Range1d

import quandl
import numpy as np 
import pandas as pd
from datetime import datetime

app = Flask(__name__)

quandl.ApiConfig.api_key = "XHUMj4gG2AGsnwtxWkx6" # you_private_api_key

@app.route('/')
def main():
    return redirect('/index')

@app.route('/index')
def index():
    user_ticker = 'AAPL'
    month_data = quandl.get(("WIKI/"+ user_ticker.strip()), start_date="2015-12-01", end_date="2015-12-31") 
    x = pd.to_datetime(month_data.index)
    y = month_data['Close']
    source = ColumnDataSource(data={
        'x' : x,
        'y' : y})
    start_date=datetime(2015,12,1,0,0)
    end_date=datetime(2015,12,31,0,0)
    p1 = figure(title=('One month stock closing price:'+ user_ticker.strip()),plot_height = 300, plot_width = 600,
           x_axis_label='Date', x_axis_type='datetime', y_axis_label='Price',
           x_range = Range1d(start=start_date, end=end_date),
           y_range = Range1d(y.min()-1,y.max()+1))
    r = p1.line(x='x', y='y', color = '#8888cc',line_width=2, source = source)

    hover = HoverTool(tooltips=[('Date', '@x{date}'), 
                                ('Closing Price', '@y{0.00}')],
                    formatters={'Date': 'datetime',
                                'Closing Price' : 'printf', },
                          mode='vline')

    p1.add_tools(hover)

    p1.background_fill_color = "beige"
    p1.background_fill_alpha = 0
    p1.border_fill_color = None

    script, div = components(p1)
    return render_template('index.html', script=script, div=div, ticker = user_ticker)

@app.route('/getprice', methods=['POST'])
def prices():
    user_ticker = request.form['user_ticker']
    month_data = quandl.get(("WIKI/"+ user_ticker.strip()), start_date="2015-12-01", end_date="2015-12-31") 
    x = pd.to_datetime(month_data.index)
    y = month_data['Close']
    source = ColumnDataSource(data={
        'x' : x,
        'y' : y})
    start_date=datetime(2015,12,1,0,0)
    end_date=datetime(2015,12,31,0,0)
    p1 = figure(title=('One month stock closing price:'+ user_ticker.strip()),plot_height = 300, plot_width = 600,
           x_axis_label='Date', x_axis_type='datetime', y_axis_label='Price',
           x_range = Range1d(start=start_date, end=end_date),
           y_range = Range1d(y.min()-1,y.max()+1))
    r = p1.line(x='x', y='y', color = '#8888cc',line_width=2, source = source)

    hover = HoverTool(tooltips=[('Date', '@x{date}'), 
                                ('Closing Price', '@y{0.00}')],
                    formatters={'Date': 'datetime',
                                'Closing Price' : 'printf', },
                          mode='vline')
    p1.add_tools(hover)

    p1.background_fill_color = "beige"
    p1.background_fill_alpha = 0
    p1.border_fill_color = None

    script, div = components(p1)
    return render_template('index.html', script=script, div=div, ticker = user_ticker)


if __name__ == '__main__':
    app.run(port=33507)