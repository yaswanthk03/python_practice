'''
    Generate Salary and Experience Dummy data using numpy.
'''
import numpy as np
import pandas as pd

np.random.seed(42)

years = np.random.uniform(0.5, 10, 1000).round(2)

salaries = (30000 + years * 2000 + np.random.normal(0, 5000, 1000)).round(2)

exp = pd.DataFrame({
    'ExperienceYears': years,
    'Salaries': salaries
})

exp.to_csv('data_set.csv', index=True, index_label='No.')