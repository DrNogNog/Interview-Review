import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Apple = yf.download("AAPL", start = "2022-01-01",end="2022-08-08")
# doesn't include weekends
#print(Apple)
a = [1,2,3,5]
ticker = ["SPY","TSLA","XOM"]
stocks = yf.download(ticker, start = "2022-01-01",end="2022-08-08",interval="30m")
