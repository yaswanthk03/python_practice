'''
    Create a salary prediction Algorithm.
'''
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv('data_set.csv')

X = data[["ExperienceYears"]]
y = data["Salaries"]

reg = LinearRegression()
reg.fit(X, y)

data["Predicted_salary"] = reg.predict(X)

# model.coef_ gives the slope of the line. It indicates how much the salary increases for each additional year of experience.
print(f"Model coefficient (slope) {round(reg.coef_[0], 2)}")
print(f"Model intercept (base salary) {round(reg.intercept_, 2)}")

plt.scatter(X, y, color='blue', label='Actual Data', s=10, alpha=0.6)
plt.plot(X, data['Predicted_salary'], color='red', label='Line of Regression')
plt.xlabel('Experience (Years)')
plt.ylabel('Salary ($)')
plt.title("Salary vs Experience")
plt.legend()
plt.grid()
plt.show()
