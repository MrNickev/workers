import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('/content/works (1).csv', delimiter=',', encoding = 'utf8')

print(len(df))
print("Men count: ", len(df[df['gender'] == 'Мужской']))
print("Women count: ", len(df[df['gender'] == 'Женский']))
print("No gender count: ", len(df[(df['gender'] != 'Мужской') & (df['gender'] != 'Женский')]))
print(len(df[df['skills'].notnull()]))
print(df[df['skills'].notnull()]['skills'])
df1 = df[df['skills'].notnull()]
print(df1[df1['skills'].str.contains('Python')]['salary'])
print("Max men salary: ", df[df['gender'] == 'Мужской']['salary'].max())
print("Max men salary: ", df[df['gender'] == 'Женский']['salary'].max())