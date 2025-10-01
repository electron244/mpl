import pandas as pd
import matplotlib.pyplot as plt

# 3. Stock Price Analysis Project 📈

df = pd.read_csv("./stock.csv")

# Convert date column
df['date'] = pd.to_datetime(df['date'])

# Plot Closing Price
plt.plot(df['date'],df['close'],color='blue')
plt.xlabel("Date")
plt.ylabel("Close Price")
plt.title("Stock Closing Price Trend")
plt.show()

# Moving Averages
df['7_days_average'] = df['close'].rolling(window=7).mean()
df['30_days_average'] = df['close'].rolling(window=30).mean()

plt.plot(df['date'],df['close'],alpha=0.5)
plt.plot(df['date'],df['7_days_average'],color='orange')
plt.plot(df['date'],df['30_days_average'],color='red')
plt.title("Stock Price with Moving Average")
plt.xlabel("Date")
plt.ylabel("Price")
plt.show()
