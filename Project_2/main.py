import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./movies.csv')

# 1. Most Popular Genre (by count of movies)
popular_genre = df["genre"].value_counts()
mtype = popular_genre.index
mcount = popular_genre.values
plt.bar(mtype,mcount,color='skyblue')
plt.xlabel("Movie Type")
plt.ylabel("Count")
plt.title("Movie Genre & Count")
plt.show()

