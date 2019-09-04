from flask import Flask, render_template, request, redirect
from bokeh.plotting import figure, output_file, show, curdoc
from bokeh.embed import components 
from bokeh.core.properties import value 
from bokeh.layouts import row, column ,WidgetBox
from bokeh.models import ColumnDataSource, CustomJS, HoverTool
from bokeh.models.widgets import Slider
from bokeh.transform import dodge , jitter, factor_cmap
from bokeh.models.markers import Asterisk,DiamondCross
import quandl
import pandas as pd 


app = Flask(__name__)

@app.route('/')
def index(): 
  month_data = quandl.get("WIKI/AAPL", start_date="2005-12-01", end_date="2005-12-31")

  x = month_data.index
  y = month_data['Close']

  p = figure(title='one month stock AAPL',plot_height = 300, plot_width = 600, background_fill_color = '#efefef')
  r = p.line(x,y, color = '#8888cc',line_width=1.5,alpha= 0.8)
  
  show(p)
  script, div = components(p)

  return render_template('index.html',script=script, div=div)

@app.route('/about')
def about():
  return render_template('about.html')

if __name__ == '__main__':
  app.run(port=33507)
