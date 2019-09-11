# Flask on Heroku

This is a test to practice making and commiting a change to a GitHub repo using Git. The goal is to have the user input a stock ticker, and it will return a month of stock price from 2015-12-01 to 2015-12-31.

The finished product is https://flask-stocks-demo.herokuapp.com.

## Uses the quandl API to pull stocks data
- use the `quandl.get` method to preselect stock of interest and filter by dates.
- api key has been hidden in the app.py file. to run, enter your own api key to access quandl dataset. 

## Uses Bokeh to visualize pandas data
- use the `pd.to_datetime` method to generate datetime data for the x-axis.
- use `Range1d` to initialize the Bokeh figure, which seems required by Bokeh js.

## Uses Javascript to select stocks and interact with the plot
- use `<input type ="text" name="tsymbol">` to fetch ticker input from user.

## Alternative solution: uses Bokeh server to serve the model
- my first and simpler solution was to use a Bokeh tornado server for data visualization and interaction, but the drawback was the lack of html styling.