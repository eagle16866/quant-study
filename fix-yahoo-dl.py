# -*- coding: utf-8 -*-
"""
Created on Fri Jun 02 13:37:48 2017

@author: jyhsi

Using fix_yahoo_finance to download stock data

用fix-yahoo-finance 取代 yahoo-finance
"""

from pandas_datareader import data as pdr
import fix_yahoo_finance  # <== that's all it takes :-)

ticker = "amzn"
# Download dataframe
data = pdr.get_data_yahoo(ticker, start="2010-01-01", end="2017-6-6")
data.to_csv('D:\Workspace\download\%s.csv' %ticker)  
print("Download completed!")
# Print last 5 rows 
print(data.tail()) 