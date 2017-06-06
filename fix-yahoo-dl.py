# -*- coding: utf-8 -*-
"""
Created on Fri Jun 02 13:37:48 2017

@author: jyhsi

Using fix_yahoo_finance to download stock data
"""

from pandas_datareader import data as pdr
import fix_yahoo_finance  # <== that's all it takes :-)

ticker = "2409.tw"
# Download dataframe
data = pdr.get_data_yahoo(ticker, start="2017-01-01", end="2017-6-6")
data.to_csv('D:\Workspace\download\%s.csv' %ticker)  
 print("Download completed!")
 # Pring last 5 rows 
print(data.tail()) 