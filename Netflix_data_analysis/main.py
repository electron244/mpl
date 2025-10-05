import pandas as pd
import matplotlib.pyplot as plt

#load data
data = pd.read_csv('netflix_titles.csv')

#clean data
data = data.dropna(subset=['type','title','director','cast','country','release_year','rating','duration','listed_in','description'])

#Tv show vs Movies
type_count = data['type'].value_counts()
plt.figure(figsize=(6,4))
plt.bar(type_count.index,type_count.values,color=['skyblue','orange'])
plt.title("Number of Movies vs TV Shows on Netflix")
plt.xlabel("Type")
plt.ylabel("Count")
plt.savefig("tv_show_vs_movies.png")
plt.show()

#Content rating Pie chart
rating_counts = data['rating'].value_counts()
plt.figure(figsize=(8,6))
plt.pie(rating_counts,labels=rating_counts.index,autopct='%1.1f%%',startangle=90)
plt.title("Percentage of Content Rating")
plt.savefig("content_rating.png")
plt.show()

# Duration histograph of Movies
movie_df = data[data['type']=='Movie'].copy()
movie_df['duration'] = movie_df['duration'].str.replace('min','').astype(int)
plt.hist(movie_df['duration'],bins=30,color='purple',edgecolor='black')
plt.title("Distribution of Movies duration")
plt.xlabel('Duration (in min)')
plt.ylabel('Number of Movies')
plt.savefig("duration_of_movies.png")
plt.show()

# release year vs Number of shows
release_counts = data['release_year'].value_counts().sort_index()
plt.figure(figsize=(10,6))
plt.scatter(release_counts.index,release_counts.values,color='red')
plt.title("Release year vs Number of Shows")
plt.xlabel("Release Year")
plt.ylabel("Number of Shows")
plt.grid(axis='y')
plt.savefig("release_year_vs_number_of_shows.png")
plt.show()

# Top 10 Countries by Number of shows
country_counts = data['country'].value_counts().head(10)
plt.figure(figsize=(8,6))
plt.barh(country_counts.index,country_counts.values,color='teal')
plt.xlabel("Number of Shows")
plt.title("Top 10 Countries by Number of Shows")
plt.ylabel("Country Name")
plt.savefig("Top_10_Countries.png")
plt.show()

# Comparison of movies and tvshows in subplot
content_by_year = data.groupby(['release_year','type']).size().unstack().fillna(0)
fig,ax = plt.subplots(1,2,figsize=(12,5))

#first subplot
ax[0].plot(content_by_year.index,content_by_year['Movie'],color='blue')
ax[0].set_title('Movies Released per year')
ax[0].set_xlabel("Year")
ax[0].set_ylabel("Number of Movies")

#Second subplot
ax[0].plot(content_by_year.index,content_by_year['TV Show'],color='orange')
ax[0].set_title('TV Show Released per year')
ax[0].set_xlabel("Year")
ax[0].set_ylabel("Number of TV Show")

fig.suptitle('Comparison of movies and TV show released Over years')
plt.tight_layout()
plt.savefig("compare_movies_and_tvshows.png")
plt.show()

































