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