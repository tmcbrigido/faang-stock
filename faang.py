import datetime
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib as mpl


# Define the timefrase used for this project

start = datetime.datetime(2014, 1, 1)
end = datetime.datetime(2019, 11, 30)

# Import the data that we will use

df = web.DataReader(["AAPL","AMZN","FB","NFLX","GOOGL"], 'yahoo', start, end)
df.tail()

AdjClose = df['Adj Close']
AdjClose.tail()

# Plot the Prices

mpl.rc('figure', figsize=(8,8))
style.use('ggplot')
AdjClose.plot(label='FAANG')
plt.legend()

# Daily and Monthly Returns

daily_returns = AdjClose.pct_change()
monthly_returns = AdjClose.resample('M').ffill().pct_change()

# Print Results

daily_returns.tail()
monthly_returns.tail()

# Monthly Returns for FAANG

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

# Histogram for Daily returns for Amazon

fig = plt.figure()
ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
daily_returns['AMZN'].plot.hist(bins = 80)
ax1.set_xlabel("Daily returns %")
ax1.set_ylabel("Percent")
ax1.set_title("Amazon daily returns data")
ax1.text(-0.10,100,"Extreme Low\nreturns")
ax1.text(0.10,100,"Extreme High\nreturns")
plt.show()


# Cumulative Returns

cum_returns = (daily_returns + 1).cumprod()

# Plot the cumulative returns for FAAG

fig = plt.figure()
ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
cum_returns.plot()
ax1.set_xlabel("Date")
ax1.set_ylabel("Growth of $1 investment")
ax1.set_title("FAAG daily cumulative returns data")
plt.show()

# Plot the cumulative returns in individual Graphs

fig = plt.figure()
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

# Statistics for FAAG

# Mean Monthly Return

print(monthly_returns.mean()*100)

# Standard Deviation

print(monthly_returns.std())

# Correlation and Covariance for FAAG

corr = (monthly_returns.corr())

print(monthly_returns.cov())

# Moving Average for FAAG

mavg30 = AdjClose.rolling(window=30).mean()
mavg50 = AdjClose.rolling(window=50).mean()
mavg100 = AdjClose.rolling(window=100).mean()

# Plot the moving average for Amazon

mpl.rc('figure', figsize=(8,7))
style.use('ggplot')
AdjClose["AMZN"].plot(label='AMZN')
mavg100["AMZN"].plot(label='mavg')
plt.legend()

# Plot the moving average for all FAANG Stocks

fig = plt.figure()
ax1 = fig.add_subplot(321)
ax2 = fig.add_subplot(322)
ax3 = fig.add_subplot(323)
ax4 = fig.add_subplot(324)
ax5 = fig.add_subplot(325)
ax1.plot(AdjClose['AMZN'], label='AMZN')
ax1.plot(mavg100['AMZN'], label='mavg')
ax1.set_title("Amazon")
ax2.plot(AdjClose['AAPL'], label='AAPL')
ax2.plot(mavg100['AAPL'], label='mavg')
ax2.set_title("Apple")
ax3.plot(AdjClose['FB'], label='FB')
ax3.plot(mavg100['FB'], label='mavg')
ax3.set_title("Facebook")
ax4.plot(AdjClose['NFLX'], label='NFLX')
ax4.plot(mavg100['NFLX'], label='mavg')
ax4.set_title("Netflix")
ax5.plot(AdjClose['GOOGL'], label='GOOGL')
ax5.plot(mavg100['GOOGL'], label='mavg')
ax5.set_title("Google")
plt.tight_layout()
plt.show()

# Plot Simple Moving Averages for Amazon

mpl.rc('figure', figsize=(8,7))
style.use('ggplot')
AdjClose["AMZN"].plot(label='AMZN')
mavg30["AMZN"].plot(label='mavg30')
mavg50["AMZN"].plot(label='mavg50')
mavg100["AMZN"].plot(label='mavg100')
plt.xlim('2017-01-01','2019-11-30')
plt.legend()

# Plot Simple Moving Averages for Apple

mpl.rc('figure', figsize=(8,7))
style.use('ggplot')
AdjClose["AAPL"].plot(label='AAPL')
mavg30["AAPL"].plot(label='mavg30')
mavg50["AAPL"].plot(label='mavg50')
mavg100["AAPL"].plot(label='mavg100')
plt.xlim('2017-01-01','2019-11-30')
plt.legend()

# Plot Simple Moving Averages for Netflix

mpl.rc('figure', figsize=(8,7))
style.use('ggplot')
AdjClose["NFLX"].plot(label='NFLX')
mavg30["NFLX"].plot(label='mavg30')
mavg50["NFLX"].plot(label='mavg50')
mavg100["NFLX"].plot(label='mavg100')
plt.xlim('2017-01-01','2019-11-30')
plt.legend()