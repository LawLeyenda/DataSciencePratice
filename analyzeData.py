import numpy as np
import pandas as pd


df = pd.read_csv('newIncome.csv')
badDataBefore = df[df['Mean'] == 0]
df = df[df['Mean'] != 0]
df = df[df['Median'] != 0]
df = df.drop(columns = ['Median'])
df = df.groupby(['State_ab']).mean()
df = df.sort_values(['Mean'], ascending = False)

## df.to_csv("FilteredNewIncome.csv")
