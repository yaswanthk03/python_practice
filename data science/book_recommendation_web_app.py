'''
    Book recommendation program.
    Create a program to recommend books based on the users favorite book.
    Create a web interface using streamlit
'''
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re
import streamlit as st

@st.cache_resource
def load_data():
    books = pd.read_csv('books.csv')

    books = books.dropna(subset=['title']).drop_duplicates(subset=['title'])
    books['description'] = books['description'].fillna("")

    books['combined'] = books['title'] + ' ' + books['description']

    indexes = pd.Series(books.index,index=books['title']
                                            .str.strip()
                                            .str.lower()
                                            .str.replace(r'\s+', ' ', regex=True)
                                            .str.replace(r'[^\w\s]', '', regex=True)
                                            )
    # indexes = books.reset_index().set_index('title')['index']
    
    return books, indexes

@st.cache_resource
def train(books):
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(books['combined'])

    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    return cosine_sim

df, indexes = load_data()
cosine_sim = train(df)

def recommend(title):
    
    title = title.strip().lower()
    title = re.sub(r'\s+', ' ', title) 
    title = re.sub(r'[^\w\s]', '', title)

    idx = indexes.get(title)

    if idx is not None:    
        sim_scores = sorted(
            enumerate(cosine_sim[idx]), 
            key=lambda x:x[1], reverse=True
            )[1:6]
        
        book_indices = [i[0] for i in sim_scores]
        return df[['title', 'authors']].iloc[book_indices]
    return None

st.title("Book Recommendation Engine.")
st.write('Enter a book title and get recommendations: ')

input_book_name = st.text_input('Book Title')

if input_book_name:
    results = recommend(input_book_name)

    if isinstance(results, pd.DataFrame):
        st.table(results)
    else:
        st.error("The title is not in our database.\nTry another")
