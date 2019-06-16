import numpy as np
import pandas as pd
import csv

df = pd.read_csv('kaggle_income.csv', encoding = "ISO-8859-1")

print(df.columns)

# print(df[['State_ab', 'Mean']])
print(df.iloc[0,5])

for index, row in df.head(5).iterrows():
    print(index,row['Mean'])

print(df.loc[df['State_ab'] == 'AL'])


print(df.sort_values('State_Code', ascending =True))

df['Total'] = df['Mean'] + df['Median']
print(df.head(5))

df = df.drop(columns = ['Total'])
print(df)

df['Total'] = df.iloc[:, 14:16].sum(axis=1)
print(df.head(5))
arr = np.ones((3,3))

df = df[['State_ab', 'Mean', 'Median']]
print(df.head(5))
cols = list(df.columns.values)
df = df[[cols[0]] + [cols[2]] + [cols[1]]]
print(df.head(5))

df.to_csv('newIncome.csv', index=False)