from flask import Flask, render_template, request, redirect
from bokeh.plotting import figure, output_file, show, curdoc
from bokeh.embed import components 
from bokeh.core.properties import value 
from bokeh.layouts import row, column,WidgetBox
from bokeh.models import ColumnDataSource, CustomJS, HoverTool
from bokeh.models.widgets import Slider, TextInput
from bokeh.transform import dodge , jitter, factor_cmap
from bokeh.models.markers import Asterisk,DiamondCross  
import quandl
import pandas as pd 


app = Flask(__name__)

@app.route('/')
def index(): 

  quandl.ApiConfig.api_key = "XHUMj4gG2AGsnwtxWkx6"
  month_data = quandl.get("WIKI/AAPL", start_date="2005-12-01", end_date="2005-12-31")

  x = month_data.index
  y = month_data['Close']
  source = ColumnDataSource(data=dict(x=x, y=y))

  p1 = figure(title='one month stock AAPL',plot_height = 300, plot_width = 600) # , background_fill_color = '#efefef'
  r = p1.line(x="x", y="y", source=source, color = '#8888cc',line_width=1.5,alpha= 0.8)
 
  ticker = TextInput(value="AAPL", title="Stock:")

  def update():
    month_data = quandl.get(("WIKI/"+ticker.value.strip()), start_date="2005-12-01", end_date="2005-12-31") 
    source.data = dict(
        x=month_data.index,
        y=month_data['Close'], 
    )
    show(p)

  ticker.on_change('value', lambda attr, old, new: update())
  
  p = column(p1,ticker)
  update()  # initial load of the data

  #curdoc().add_root(p) 

  

  script, div = components(p)

  return render_template('index.html',script=script, div=div)

@app.route('/about')
def about():
  return render_template('about.html')

if __name__ == '__main__':
  app.run(port=33507)



