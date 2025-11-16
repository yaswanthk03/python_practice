'''
    Book recommendation program.
    Create a program to recommend books based on the users favorite book.
'''
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

books = pd.read_csv('books.csv')

books = books.dropna(subset=['title'])
books['description'] = books['description'].fillna("")

books['title'] = (
    books['title']
    .str.strip()
    .str.lower()
    .str.replace(r'\s+', ' ', regex=True)
    .str.replace(r'[^\w\s]', '', regex=True)
    )

books['combined'] = books['title'] + ' ' + books['description']

vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(books['combined'])

cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# indexes = pd.Series(books.index, index=books['title'])
indexes = books.reset_index().set_index('title')['index']

input_book_name = input("Enter the book for recommendations: ")

input_book_name = input_book_name.strip().lower()
input_book_name = re.sub(r'\s+', ' ', input_book_name) 
input_book_name = re.sub(r'[^\w\s]', '', input_book_name)

idx = indexes.get(input_book_name)


if idx is not None:    
    arr = sorted(enumerate(cosine_sim[idx]), key=lambda x:x[1], reverse=True)[1:6]

    print('These might be moe suitable for you: ')
    for idx, match in arr:
        title = books.loc[idx, 'title'].title()
        print(f"--> {title:<30} -- {round(match * 100, 2)} % match")
else:
    print("Sorry! the book is not in our database.\nTry another")
