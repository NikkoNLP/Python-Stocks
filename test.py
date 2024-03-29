#!/usr/bin/python
# Author: Nikko Pedersen
# Revised: 12/14/2017
# =========================
import pandas as pd
from pandas_datareader import data, wb
import datetime

# We will look at stock prices over the past year, starting at January 1, 2016
start = datetime.datetime(2017,12,1)
end = datetime.date.today()
 
# Let's get Apple stock data; Apple's ticker symbol is AAPL
# First argument is the series we want, second is the source ("yahoo" for Yahoo! Finance), third is the start date, fourth is the end date
apple = data.DataReader("AAPL", "yahoo", start, end)
 
type(apple)

print apple.head()

