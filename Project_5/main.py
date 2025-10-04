import matplotlib.pyplot as plt
import pandas as pd

# Load and explore the dataset
df = pd.read_csv("sales.csv")
print(df.info())

# Total Revenue by Region

# region_sales = df.groupby('Region')['Revenue'].sum().sort_values(ascending=False)
# print(region_sales)
region_sales = df.groupby('Region')['Revenue'].sum()
# print(region_sales)
region_sales.plot(kind='bar',color='orange')
plt.title("Total Revenue By Region")
plt.xlabel("Region")
plt.ylabel("Revenue Generated")
plt.show()


# Best-Selling Products
best_product = df.groupby('Product')['Revenue'].sum().sort_values(ascending=False)
best_product.plot(kind='bar',color='skyblue')
plt.xticks(rotation=45)
plt.xlabel("Products")
plt.ylabel("Sales of Product")
plt.title("Best-Selling Products")
plt.show()

# Revenue Over Time
df["Date"] = pd.to_datetime(df['Date'])
daily_sales = df.groupby('Date')['Revenue'].sum()
plt.figure(figsize=(10,5))
plt.plot(daily_sales.index,daily_sales.values,color='blue',marker='^')
plt.xlabel("Dates")
plt.ylabel("Sales per Day")
plt.title("Sales per day")
plt.grid()
plt.show()

# Revenue Share by Product Category
plt.pie(best_product.values, labels=best_product.index, autopct='%1.1f%%', startangle=140)
plt.title("Revenue Share by Product")
plt.show()







