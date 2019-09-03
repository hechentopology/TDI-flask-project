from flask import Flask, render_template, request, redirect
from bokeh.plotting import figure, output_file, show, curdoc
from bokeh.embed import components 
from bokeh.core.properties import value 
from bokeh.layouts import row, column ,WidgetBox
from bokeh.models import ColumnDataSource, CustomJS, HoverTool
from bokeh.models.widgets import Slider
from bokeh.transform import dodge , jitter, factor_cmap
from bokeh.models.markers import Asterisk,DiamondCross

import pandas as pd 


app = Flask(__name__)

@app.route('/')
def index():
  opts = dict(plot_width=250, plot_height=250,min_border=0)
  p1 = figure(**opts)
  r1 = p1.circle([1,2,3],[4,5,6],size=20)
 

  show(p1, notebook_handle = True)
  script, div = components(p)

  return render_template('index.html',{'script': script, 'div': div})

@app.route('/about')
def about():
  return render_template('about.html')

if __name__ == '__main__':
  app.run(port=33507)
