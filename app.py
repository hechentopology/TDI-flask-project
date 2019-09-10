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

import quandl
import pandas as pd 


app = Flask(__name__)


quandl.ApiConfig.api_key = "XHUMj4gG2AGsnwtxWkx6" 
#DEFAULT_TICKERS = ['AAPL', 'GOOG', 'INTC', 'BRCM', 'YHOO']

@app.route('/', methods=['GET'])


month_data = quandl.get(("WIKI/"+'AAPL'), start_date="2005-12-01", end_date="2005-12-31") 
x = month_data.index
y = month_data['Close']
source = ColumnDataSource(data=dict(x=x, y=y))

p1 = figure(title='one month stock AAPL',plot_height = 300, plot_width = 600) # , background_fill_color = '#efefef'
r = p1.line(x="x", y="y", source=source, color = '#8888cc',line_width=1.5,alpha= 0.8)

def callback(attr, old, new):

    month_data = quandl.get(("WIKI/"+ new.strip()), start_date="2005-12-01", end_date="2005-12-31") 
    x = month_data.index
    y = month_data['Close']
    source.data = ColumnDataSource(data=dict(x=x, y=y)).data

slider = TextInput(value="AAPL", title="Stock:")
slider.on_change('value', callback)
p = column(slider, p1)

curdoc().add_root(p)

#  return render_template("index.html", script=script, template="Flask")


if __name__ == '__main__':
  app.run(port=33507)


