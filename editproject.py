
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:\\Users\\HP\\Desktop\\python\\matplotlib\\netflix_titles.csv')
df = df.dropna(subset=['type', 'release_year', 'rating', 'country', 'duration'])


# 1. Movies vs TV Shows

type_counts = df['type'].value_counts()
plt.figure(figsize=(6,4))
plt.bar(type_counts.index, type_counts.values, color=['red', 'orange'])
plt.title("Number of Movies VS TV Shows on Netflix")
plt.xlabel("Type")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig('movies_vs_tvshows.png')
plt.show()

# 2. Percentage of Content Ratings
rating_counts = df['rating'].value_counts()
plt.figure(figsize=(8,6))
plt.pie(rating_counts, labels=rating_counts.index, autopct='%1.1f%%', startangle=90)
plt.title("Percentage of Content Ratings on Netflix")
plt.tight_layout()
plt.savefig('Ratings.png')
plt.show()

# ----------------------------------------
# 3. Release Year vs Number of Shows (Scatter)
# ----------------------------------------
release_counts = df['release_year'].value_counts().sort_index()
plt.figure(figsize=(10,6))
plt.scatter(release_counts.index, release_counts.values, color='green', alpha=0.7)
plt.title("Release Year VS Number of Shows")
plt.xlabel("Release Year")
plt.ylabel("Number of Shows")
plt.tight_layout()
plt.savefig("release_year_scatter.png")
plt.show()

# ----------------------------------------
# 4. Top 10 Countries Producing Shows
# ----------------------------------------
top_countries = df['country'].value_counts().head(10)
plt.figure(figsize=(8,6))
plt.barh(top_countries.index, top_countries.values, color='violet')
plt.title('Top 10 Countries Producing Content on Netflix')
plt.xlabel("Number of Shows")
plt.ylabel("Country")
plt.tight_layout()
plt.savefig("Countries.png")
plt.show()

# ----------------------------------------
# 5. Content Released Per Year by Type (Line Plot)
# ----------------------------------------
per_year = df.groupby(['release_year', 'type']).size().unstack().fillna(0)
per_year.plot(kind='line', figsize=(10,6))
plt.title("Content Added per Year by Type")
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.savefig("Content_By_Year_Line.png")
plt.show()

# ----------------------------------------
# 6. Word Cloud of Netflix Titles
# ----------------------------------------
# text = ' '.join(df['title'].dropna())
# wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
# plt.figure(figsize=(10,5))
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis('off')
# plt.title("Most Common Words in Netflix Titles")
# plt.tight_layout()
# plt.savefig("wordcloud_titles.png")
# plt.show()

# ----------------------------------------
# 6. Top 10 Genres
# ----------------------------------------
genres = df['listed_in'].dropna().str.split(', ', expand=True).stack().value_counts().head(10)
plt.figure(figsize=(8,6))
plt.barh(genres.index, genres.values, color='skyblue')
plt.title("Top 10 Genres on Netflix")
plt.xlabel("Count")
plt.ylabel("Genre")
plt.tight_layout()
plt.savefig("Top_Genres.png")
plt.show()

# ----------------------------------------
# 7. Top 10 Directors
# ----------------------------------------
top_directors = df['director'].dropna().str.split(', ', expand=True).stack().value_counts().head(10)
plt.figure(figsize=(8,6))
plt.bar(top_directors.index, top_directors.values, color='lightgreen')
plt.title("Top 10 Netflix Directors")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Top_Directors.png")
plt.show()

# ----------------------------------------
# 8. Movie Duration Distribution
# ----------------------------------------
movies = df[df['type'] == 'Movie'].copy()
movies['minutes'] = movies['duration'].str.replace(' min', '').astype(int)

plt.figure(figsize=(8,6))
plt.hist(movies['minutes'], bins=30, color='coral', edgecolor='black')
plt.title("Distribution of Movie Durations")
plt.xlabel("Duration (minutes)")
plt.ylabel("Number of Movies")
plt.tight_layout()
plt.savefig("Movie_Durations.png")
plt.show()

# ----------------------------------------
# 9. Export Cleaned Data
# ----------------------------------------
df.to_csv("cleaned_netflix_data.csv", index=False)
print("✅ Cleaned dataset exported to 'cleaned_netflix_data.csv'")
