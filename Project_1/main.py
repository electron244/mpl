from operator import index
import matplotlib.pyplot as plt
import pandas as pd
from sympy.physics.units import temperature

''' 
Weather Data Analysis
    Use a CSV file of daily temperature, rainfall, humidity.
    Find the hottest and coldest day.
    Plot temperature trends over time.
    Compare average temperature per month using a bar chart.
'''

data = pd.read_csv('weather_data.csv')

print(data[data['temp_max']==data['temp_max'].max()])
print(data[data['temp_min']==data['temp_min'].min()])


date = data['date'].head(6)
temperature = data['temp_max'].head(6)


# Plot of Temperature over Time
plt.plot(date,temperature,color='blue')
plt.title("Daily Temperature Trend ")
plt.xlabel("Date")
plt.ylabel("Temperature (.C)")
plt.grid()
plt.show()

#Avg Temperature per month
data['date'] = pd.to_datetime(data['date'],format='%d-%m-%Y')
data['Month'] = data["date"].dt.month
monthly_avg = data.groupby('Month')['temp_max'].mean()
plt.bar(monthly_avg.index,monthly_avg.values)
plt.title("Average Temperature per month")
plt.xlabel("Month")
plt.ylabel("Avg. Temperature (.C)")
plt.show()