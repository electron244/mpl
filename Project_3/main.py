import pandas as pd
import matplotlib.pyplot as plt
from scipy.ndimage import label

df = pd.read_csv("./stock.csv")

# Convert date column
df['date'] = pd.to_datetime(df['date'])

# Plot Closing Price
plt.plot(df['date'],df['close'],color='blue')
plt.xlabel("Date")
plt.ylabel("Close Price")
plt.title("Stock Closing Price Trend")
plt.show()

