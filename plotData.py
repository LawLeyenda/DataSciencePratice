import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


df = pd.read_csv('FilteredNewIncome.csv')
x = df['State_ab'].values
y = df['Mean'].values/1000
plt.style.use('classic')
fig = plt.figure()

ax = plt.axes()
plt.title("Mean Income per State")
plt.xlabel("State")
plt.ylabel("Moonie ($ in thousands)")
ax.bar(x,y, align='edge', width= 1)
ax.tick_params(axis = 'x', which = 'major', labelsize = 6)
plt.tight_layout()
plt.show()
