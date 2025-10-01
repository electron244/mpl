import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./covid.csv")

#converting date to datetime
df['date'] = pd.to_datetime(df['date'])

# Filter data for India
india = df[df['country'] == "India" ]

# Plot confirmed cases over time
plt.plot(india['date'],india['confirmed'],color='blue',marker='o')
plt.xlabel("Dates")
plt.ylabel("Confirmed Cases")
plt.title("COVID-19 Cases in India")
plt.grid()
plt.show()


# Compare India vs USA

