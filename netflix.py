#!/usr/bin/env python
# coding: utf-8

# # Introduction
# 
# In this project, you will act as a data visualization developer at Yahoo Finance! You will be helping the "Netflix Stock Profile" team visualize the Netflix stock data. In finance, a _stock profile_ is a series of studies, visualizations, and analyses that dive into different aspects a publicly traded company's data. 
# 
# For the purposes of the project, you will only visualize data for the year of 2017. Specifically, you will be in charge of creating the following visualizations:
# + The distribution of the stock prices for the past year
# + Netflix's earnings and revenue in the last four quarters
# + The actual vs. estimated earnings per share for the four quarters in 2017
# + A comparison of the Netflix Stock price vs the Dow Jones Industrial Average price in 2017 
# 
# Note: We are using the Dow Jones Industrial Average to compare the Netflix stock to the larter stock market. Learn more about why the Dow Jones Industrial Average is a general reflection of the larger stock market [here](https://www.investopedia.com/terms/d/djia.asp).
# 
# During this project, you will analyze, prepare, and plot data. Your visualizations will help the financial analysts asses the risk of the Netflix stock.

# ## Step 1
# 
# Let's get our notebook ready for visualizing! Import the modules that you'll be using in this project:
# - `from matplotlib import pyplot as plt`
# - `import pandas as pd`
# - `import seaborn as sns`


from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns


# ## Step 2

# Let's load the datasets and inspect them.


netflix_stocks = pd.read_csv('NFLX.csv')
print(netflix_stocks.head())


# Load **DJI.csv** into a DataFrame called `dowjones_stocks`. Then, quickly inspect the DataFrame using `print()`.
# 

dowjones_stocks = pd.read_csv('DJI.csv')
print((dowjones_stocks.head()))


# Load **NFLX_daily_by_quarter.csv** into a DataFrame called `netflix_stocks_quarterly`. Then, quickly inspect the DataFrame using `print()`.
# 

netflix_stocks_quarterly = pd.read_csv('NFLX_daily_by_quarter.csv')
print(netflix_stocks_quarterly.head())


# ## Step 3

# Let's learn more about our data. The datasets are large and it may be easier to view the entire dataset locally on your computer. Open the CSV files directly from the folder you downloaded for this project.
#  - `NFLX` is the stock ticker symbol for Netflix and `^DJI` is the stock ticker symbol for the Dow Jones industrial Average, which is why the CSV files are named accordingly
#  - In the Yahoo Data, `Adj Close` is documented as adjusted close price adjusted for both dividends and splits.
#  - You can learn more about why the Dow Jones Industrial Average is a industry reflection of the larger stock market [here](https://www.investopedia.com/terms/d/djia.asp). 

print(netflix_stocks.head())

netflix_stocks.rename(columns={ 'Adj Close': 'Price'}, inplace=True)
dowjones_stocks.rename(columns={ 'Adj Close': 'Price'}, inplace=True)
netflix_stocks_quarterly.rename(columns={ 'Adj Close': 'Price'}, inplace=True)


print(netflix_stocks.head())


# Call `.head()` on the DataFrame `dowjones_stocks` and `netflix_stocks_quarterlyprint(dowjones_stocks.head())
print(netflix_stocks_quarterly.head())


# ## Step 5
# 
# In this step, we will be visualizing the Netflix quarterly data! 
# 
# We want to get an understanding of the distribution of the Netflix quarterly stock prices for 2017. Specifically, we want to see in which quarter stock prices flucutated the most. We can accomplish this using a violin plot with four violins, one for each business quarter

ax = sns.violinplot(data = netflix_stocks_quarterly, x='Quarter', y='Price')
ax.set_title('Distribution of 2017 Netflix Stock Prices by Quarter')
plt.xlabel("Business Quarters in 2017")
plt.ylabel('Closing Stock Price')
plt.show()
plt.savefig("NetflixPriceDistributions.png")


# ## Step 6
# 
# Next, we will chart the performance of the earnings per share (EPS) by graphing the estimate Yahoo projected for the Quarter compared to the actual earnings for that quarters. We will accomplish this using a scatter chart. 


x_positions = [1, 2, 3, 4]
chart_labels = ["1Q2017","2Q2017","3Q2017","4Q2017"]
earnings_actual =[.4, .15,.29,.41]
earnings_estimate = [.37,.15,.32,.41]


plt.scatter(x=x_positions, y=earnings_actual , color='red', alpha=0.5)
plt.scatter(x=x_positions, y=earnings_estimate , color='blue', alpha=0.5)
plt.legend(['Actual', 'Estimate'])
plt.xticks(x_positions, chart_labels)
plt.title('Earnings Per Share in Cents')
plt.savefig("EarningsinCents.png")


# ## Step 7

# Next, we will visualize the earnings and revenue reported by Netflix by mapping two bars side-by-side. We have visualized a similar chart in the second Matplotlib lesson [Exercise 4](https://www.codecademy.com/courses/learn-matplotlib/lessons/matplotlib-ii/exercises/side-by-side-bars).
# 

# The metrics below are in billions of dollars
revenue_by_quarter = [2.79, 2.98,3.29,3.7]
earnings_by_quarter = [.0656,.12959,.18552,.29012]
quarter_labels = ["2Q2017","3Q2017","4Q2017", "1Q2018"]

# Revenue
n = 1
t = 2 
d = 4
w = .8
bars1_x = [t*element + w*n for element
             in range(d)]
plt.bar(bars1_x, revenue_by_quarter)


# Earnings
n = 2
t = 2 
d = 4
w = .8 
bars2_x = [t*element + w*n for element
             in range(d)]

plt.bar(bars2_x, earnings_by_quarter)
middle_x = [ (a + b) / 2.0 for a, b in zip(bars1_x, bars2_x)]

plt.title('Revenue and Earnings by Quarter')
plt.xticks(middle_x, quarter_labels)
plt.legend(labels)



labels = ["Revenue", "Earnings"]
plt.show()
plt.savefig("RevenueEarnings.png")


# ## Step 8
# 
# In this last step, we will compare Netflix stock to the Dow Jones Industrial Average in 2017. We will accomplish this by plotting two line charts side by side in one figure. 

# Left plot Netflix
ax1 = plt.subplot(1,2,1)
ax1.plot(netflix_stocks['Date'], netflix_stocks['Price'])
ax1.set_title('Netflix')
ax1.set_xticklabels(range(1,13))
ax1.set_xlabel('Date')
ax1.set_ylabel('Stock Price')


# Right plot Dow Jones
ax2 = plt.subplot(1,2,2)

ax2.plot(dowjones_stocks['Date'], dowjones_stocks['Price'])
ax2.set_title('Netflix')
ax2.set_xticklabels(range(1,13))
ax2.set_xlabel('Date')
ax2.set_title('Dow Jones')
plt.subplots_adjust(wspace=.5)
plt.show()
plt.savefig("NetflixvsDowJones.png")


