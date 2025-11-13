'''
    Use Streamlit to Display the Salary Prediction Algorithm.
'''
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
import streamlit as st

data = pd.read_csv('data_set.csv')

X = data[["ExperienceYears"]]
y = data["Salaries"]

reg = LinearRegression()
reg.fit(X, y)
data["Predicted_salary"] = reg.predict(X)

st.title("Salary Predictor depending on work experience.")
st.write("Enter your Years of experience to predict salary: ")
exp = st.number_input("Years of experience.", 0.0, 50.0, step=0.5)

if exp:
    predicted_salary = reg.predict([[exp]])[0]
    st.success(f'Your estimated salary is {round(predicted_salary, 2)} $')


fig, ax = plt.subplots()

ax.scatter(X, y, color='blue', label='Actual Data', s=10, alpha=0.6)
ax.plot(X, data['Predicted_salary'], color='red', label='Line of Regression')
ax.set_xlabel('Experience (Years)')
ax.set_ylabel('Salary ($)')
ax.set_title("Salary vs Experience")
ax.legend()


st.pyplot(fig)
