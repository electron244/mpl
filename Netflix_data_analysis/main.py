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
plt.show()

#Content rating Pie chart
rating_counts = data['rating'].value_counts()
plt.figure(figsize=(8,6))
plt.pie(rating_counts,labels=rating_counts.index,autopct='%1.1f%%',startangle=90)
plt.title("Percentage of Content Rating")
plt.show()

# Duration histograph of Movies
movie_df = data[data['type']=='Movie'].copy()
movie_df['duration'] = movie_df['duration'].str.replace('min','').astype(int)
plt.hist(movie_df['duration'],bins=30,color='purple',edgecolor='black')
plt.title("Distribution of Movies duration")
plt.xlabel('Duration (in min)')
plt.ylabel('Number of Movies')
plt.show()


release_counts = data['release_year'].value_counts().sort_index()
plt.figure(figsize=(10,6))
plt.scatter(release_counts.index,release_counts.values,color='red')
plt.title("Release year vs Number of Shows")
plt.xlabel("Release Year")
plt.ylabel("Number of Shows")
plt.grid(axis='y')
plt.show()