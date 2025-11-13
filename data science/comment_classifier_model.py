'''
    Comment Classifier
    Write a program to Classify comments as Toxic or Acceptable in general based on trained model.
    Use Tf-Idf Vectorizer.
'''
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

df = pd.read_csv('youtube_comments.csv')

X_train, X_test, y_train, y_test = train_test_split(df['Text'], df['IsToxic'], test_size=0.2, random_state=70)

model = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english')),
    ('clf', LogisticRegression())
])

model.fit(X_train, y_train)
acc = model.score(X_test, y_test)

predict = model.predict(["This is waste of time"])[0]

print(f'The accuracy of the model is {round(acc, 4) * 100} %')
