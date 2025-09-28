import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./movies.csv')
print(df.head())

# 1. Most Popular Genre (by count of movies)
popular_genre = df["genre"].value_counts()
mtype = popular_genre.index
mcount = popular_genre.values
plt.bar(mtype,mcount,color='skyblue')
plt.xlabel("Movie Type")
plt.ylabel("Count")
plt.title("Movie Genre & Count")
plt.show()

# 2. Average Rating by Genre
avg_rating_genre = df.groupby('genre')['rating'].mean()
plt.bar(avg_rating_genre.index,avg_rating_genre.values,color='orange')
plt.xlabel("Genre")
plt.ylabel("Avg. Rating")
plt.title("Average Rating")
plt.show()

# 3. Top 10 Highest Rated Movies
top_movies = df.sort_values(by='rating',ascending=False).head(10)
plt.barh(top_movies['title'],top_movies["rating"],color='orange')
plt.xlabel("IMDb Rating")
plt.ylabel("Movies Name")
plt.title("Top 10 Highest Rated Movies")
plt.show()

# 4. Ratings Over Years
avg_rating_year = df.groupby('year')['rating'].mean()
plt.plot(avg_rating_year.index,avg_rating_year.values,color='skyblue')
plt.xlabel("Years")
plt.ylabel("Average Rating")
plt.grid()
plt.title("Rating Over Years")
plt.show()










