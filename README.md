# FAANG - Simple Moving Averages

<!Add Codacy Badge!>

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/a0d3d04c572542e484f8ee9ee99e0467)](https://www.codacy.com/manual/tmcbrigido/faang-stock?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=tmcbrigido/faang-stock&amp;utm_campaign=Badge_Grade)

FAANG is an acronym for the 5 most popular and best-performing tech stocks - Facebook, Apple, Amazon, Netflix, and Alphabet (Google). Over the past few years, FAANG stocks have delivered outstanding results to their shareholders but they start to show signs of resistance which leaves us with an open question when planning our investment strategies for 2020: Can these stocks still outperform the market consistently or should investors find return anywhere else?  I will focus this analysis in the past performance of FAANG using Python, starting with historical performance, data visualization and close with a prediction analysis using Linear Analysis and K Nearest Neighbor (KNN).

## Load Data from Yahoo Finance

Pandas Web Reader is an up to date remote acess for pandas library that allows us to extract financial information from multiple sources including Yahoo Finance, Quandl, Enigma, World Bank, etc. In my analysis, I will use Yahoo Finance using the following code with prices over the past 5 years.

```import pandas as pd
import datetime
import pandas_datareader.data as web
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib as mpl

start = datetime.datetime(2014, 1, 1)
end = datetime.datetime(2019, 11, 30)

df = web.DataReader(["AAPL","AMZN","FB","NFLX","GOOGL"], 'yahoo', start, end)
```

![FAANG - Adjusted Prices](/images/AdjClose.png)

## Data Visualization

Let's have a look at the code ad graph created using matplotlib:

``` mpl.rc('figure', figsize=(8, 8))
style.use('ggplot')
AdjClose.plot(label='FAANG')
plt.legend()
```

![FAANG Adjusted Prices](/images/stock_plot.png)

If you look at the previous graph you can easily identify trends in the markets, corrections and compare performance. The next step is to compute the monthly returns and cumulative returns and plot those results:

```monthly_returns = AdjClose.resample('M').ffill().pct_change()
fig = plt.figure()
ax1 = fig.add_subplot(321)
ax2 = fig.add_subplot(322)
ax3 = fig.add_subplot(323)
ax4 = fig.add_subplot(324)
ax5 = fig.add_subplot(325)
ax1.plot(monthly_returns['AMZN'])
ax1.set_title("Amazon")
ax2.plot(monthly_returns['AAPL'])
ax2.set_title("Apple")
ax3.plot(monthly_returns['FB'])
ax3.set_title("Facebook")
ax4.plot(monthly_returns['NFLX'])
ax4.set_title("Netflix")
ax5.plot(monthly_returns['GOOGL'])
ax5.set_title("Google")
plt.tight_layout()
plt.show()
```

![FAANG - Monthly Returns](/images/monthly_plot.png)

Based on the cumulative returns, we could plot it as following:

```cum_returns = (monthly_returns + 1).cumprod()
fig = plt.figure()
ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
cum_returns.plot()
ax1.set_xlabel("Date")
ax1.set_ylabel("Growth of $1 investment")
ax1.set_title("FAAG daily cumulative returns data")
plt.show()
```

![FAANG - Cumulative Returns](/images/cumulative_returns.png)

For each one of the stocks:

```fig = plt.figure()
ax1 = fig.add_subplot(321)
ax2 = fig.add_subplot(322)
ax3 = fig.add_subplot(323)
ax4 = fig.add_subplot(324)
ax5 = fig.add_subplot(325)
ax1.plot(cum_returns['AMZN'])
ax1.set_title("Amazon")
ax2.plot(cum_returns['AAPL'])
ax2.set_title("Apple")
ax3.plot(cum_returns['FB'])
ax3.set_title("Facebook")
ax4.plot(cum_returns['NFLX'])
ax4.set_title("Netflix")
ax5.plot(cum_returns['GOOGL'])
ax5.set_title("Google")
plt.tight_layout()
plt.show()
```

![Individual Stocks - Cumulative Returns](/images/cumulative_individual.png)

Historical performance is not a sign of future performance.

## Moving Averages

The Simple Moving Average (SMA) is a technique used by investors to make buy and sell decisions by identifying support and resistance prices where the stock or currency should be traded. The SMA takes the average price over a certain period. In this case, we will compute the SMA for 30, 60 and 90 days, which means that we will measure it based on the average for the past 30 days for example.  The length of the moving average will depend on the investment strategy that would be adopted, with shorter moving averages used for short term strategies and long term moving averages for long term investments.  A rising trend in the moving average is an indicator of an uptrend in the stock while a declining moving average is a sign of a downtrend.

```mavg30 = AdjClose.rolling(window=30).mean()
mavg50 = AdjClose.rolling(window=50).mean()
mavg100 = AdjClose.rolling(window=100).mean()
```

```fig = plt.figure()
ax1 = fig.add_subplot(321)
ax2 = fig.add_subplot(322)
ax3 = fig.add_subplot(323)
ax4 = fig.add_subplot(324)
ax5 = fig.add_subplot(325)
ax1.plot(AdjClose['AMZN'], label='AMZN')
ax1.plot(mavg90['AMZN'], label='mavg')
ax1.set_title("Amazon")
ax2.plot(AdjClose['AAPL'], label='AAPL')
ax2.plot(mavg90['AAPL'], label='mavg')
ax2.set_title("Apple")
ax3.plot(AdjClose['FB'], label='FB')
ax3.plot(mavg90['FB'], label='mavg')
ax3.set_title("Facebook")
ax4.plot(AdjClose['NFLX'], label='NFLX')
ax4.plot(mavg90['NFLX'], label='mavg')
ax4.set_title("Netflix")
ax5.plot(AdjClose['GOOGL'], label='GOOGL')
ax5.plot(mavg90['GOOGL'], label='mavg')
ax5.set_title("Google")
plt.tight_layout()
plt.show()
```

![Simple Moving Averages](/images/moving.png)

## Simple Moving Averages - Amazon

```mpl.rc('figure', figsize=(8, 7))
style.use('ggplot')
AdjClose["AMZN"].plot(label='AMZN')
mavg30["AMZN"].plot(label='mavg30')
mavg50["AMZN"].plot(label='mavg50')
mavg100["AMZN"].plot(label='mavg100')
plt.xlim('2017-01-01','2019-11-30')
plt.legend()
```

![SMA - Amazon](/images/sam_amazon.png)
