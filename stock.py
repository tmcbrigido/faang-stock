import pandas as pd
import datetime
import pandas_datareader.data as web
from pandas import Series, DataFrame


# Define the timefrase used for this project

start = datetime.datetime(2014, 1, 1)
end = datetime.datetime(2019, 11, 30)

# Import the data that we will use

df = web.DataReader(["AAPL","AMZN","FB","NFLX","GOOGL"], 'yahoo', start, end)
df.tail()

AdjClose = df['Adj Close']


# Plot the Prices

%matplotlib inline
import matplotlib.pyplot as plt
from matplotlib import style

# Adjusting the size of matplotlib
import matplotlib as mpl
mpl.rc('figure', figsize=(8, 7))
mpl.__version__

# Adjusting the style of matplotlib
style.use('ggplot')

AdjClose.plot(label='AAPL')
plt.legend()



daily_returns = AdjClose.pct_change()
monthly_returns = AdjClose.resample('M').ffill().pct_change()

# Print Results

daily_returns.head()
monthly_returns.head()

# Plot monthly returns for individual stocks that belong to FAANG

# Monthly Returns Apple

fig = plt.figure()
ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
ax1.plot(daily_returns['AAPL'])
ax1.set_xlabel("Date")
ax1.set_ylabel("Percent")
ax1.set_title("Apple daily returns data")
plt.show()


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



# Histogram for monthly returns

fig = plt.figure()
ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
daily_returns['AMZN'].plot.hist(bins = 80)
ax1.set_xlabel("Daily returns %")
ax1.set_ylabel("Percent")
ax1.set_title("Amazon daily returns data")
ax1.text(-0.35,200,"Extreme Low\nreturns")
ax1.text(0.25,200,"Extreme High\nreturns")
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

corr

print(monthly_returns.cov())


# Moving Average for FAAG

mavg30 = AdjClose.rolling(window=30).mean()

# Print mavg

mavg30

# Plot the moving average for Amazon

%matplotlib inline
import matplotlib.pyplot as plt
from matplotlib import style

# Adjusting the size of matplotlib
import matplotlib as mpl
mpl.rc('figure', figsize=(8, 7))
mpl.__version__

# Adjusting the style of matplotlib
style.use('ggplot')
AdjClose["AMZN"].plot(label='AAPL')
mavg30["AMZN"].plot(label='mavg')
plt.legend()


# Moving Average for FAAG - 120 days

mavg120 = AdjClose.rolling(window=120).mean()

# Print mavg

mavg120

# Plot the moving average for Amazon

%matplotlib inline
import matplotlib.pyplot as plt
from matplotlib import style

# Adjusting the size of matplotlib
import matplotlib as mpl
mpl.rc('figure', figsize=(8, 7))
mpl.__version__

# Adjusting the style of matplotlib
style.use('ggplot')
AdjClose["AMZN"].plot(label='AAPL')
mavg120["AMZN"].plot(label='mavg')
plt.legend()


# Return Deviation

rets = AdjClose / AdjClose.shift(1) - 1
rets.plot(label='return')

# Kernel Density Estimate

pd.scatter_matrix(corr, diagonal='kde', figsize=(10, 10))


# Plot Corr with a Heat Map

plt.imshow(corr, cmap='hot', interpolation='none')
plt.colorbar()
plt.xticks(range(len(corr)), corr.columns)
plt.yticks(range(len(corr)), corr.columns)

# Stocks Returns Rate and Risk

plt.scatter(corr.mean(), corr.std())
plt.xlabel('Expected returns')
plt.ylabel('Risk')
for label, x, y in zip(corr.columns, corr.mean(), corr.std()):
    plt.annotate(
        label, 
        xy = (x, y), xytext = (20, -20),
        textcoords = 'offset points', ha = 'right', va = 'bottom',
        bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
        arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))