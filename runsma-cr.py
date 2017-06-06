# -*- coding: utf-8 -*-
"""
Created on Sun Apr 02 10:46:28 2017

@author: jyhsi

"""
#place below command in console to magnify the plot
#>>import matplotlib.pyplot as plt
#>>plt.rc('figure',figsize=(50,50))

from pyalgotrade import plotter
from pyalgotrade.barfeed import yahoofeed
from pyalgotrade.stratanalyzer import returns
import sma_crossover

# Load the yahoo feed from the CSV file
feed = yahoofeed.Feed()
ticker="000333.sz"
feed.addBarsFromCSV(ticker, r'D:\Workspace\download\%s.csv'  %ticker )

# Evaluate the strategy with the feed's bars.
myStrategy = sma_crossover.SMACrossOver(feed, ticker, 15)

# Attach a returns analyzers to the strategy.
returnsAnalyzer = returns.Returns()
myStrategy.attachAnalyzer(returnsAnalyzer)

# Attach the plotter to the strategy.
plt = plotter.StrategyPlotter(myStrategy)
# Include the SMA in the instrument's subplot to get it displayed along with the closing prices.
plt.getInstrumentSubplot(ticker).addDataSeries("SMA", myStrategy.getSMA())
# Plot the simple returns on each bar.
plt.getOrCreateSubplot("returns").addDataSeries("Simple returns", returnsAnalyzer.getReturns())

# Run the strategy.
myStrategy.run()
myStrategy.info("Final portfolio value: $%.2f" % myStrategy.getResult())

# Plot the strategy.
plt.plot()


