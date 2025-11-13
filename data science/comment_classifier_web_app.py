'''
    Comment Classifier Web Application.
    Use streamlit.    
'''
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
import streamlit as st

@st.cache_resource
def load_model():
    df = pd.read_csv('youtube_comments.csv')

    model = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('clf', LogisticRegression(max_iter=1000))
    ])

    model.fit(df['Text'], df['IsToxic'])
    return model

model = load_model()
st.title("Youtube comment classifier")
st.write("Classifies your comment as Toxic or Acceptable.")
comment = st.text_input("Enter your comment here ....")

if comment:
    prediction = model.predict([comment])[0]
    if prediction:
        st.error(f'Your comment is likely Toxic')
    else:
        st.success(f'Your comment is likely Acceptable')
