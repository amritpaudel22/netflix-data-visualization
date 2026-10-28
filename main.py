import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('netflix_titles.csv')


#cleaning the data
df=df.dropna(subset=['show_id','type','title','director','cast','country','date_added','release_year','rating','duration','listed_in','description'])
type_counts=df['type'].value_counts()
print(type_counts)
plt.figure(figsize=(6, 4))
plt.bar(type_counts.index,type_counts.values,color=['skyblue','brown'])
plt.title('Movies vs tv shows)')
plt.xlabel('Type')
plt.ylabel('Frequency')
plt.tight_layout()

rating_counts = df['rating'].value_counts()

plt.figure(figsize=(8, 6))

print(rating_counts)

plt.pie(
    rating_counts,
    labels=rating_counts.index,
    autopct='%1.1f%%',
    startangle=90
)

plt.title('Content Ratings')
plt.tight_layout()
plt.show()

movies_df=df[df['type']=='Movies'].copy()


