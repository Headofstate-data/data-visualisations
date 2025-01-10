import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

prac_data=pd.read_excel('practice_data.xlsx')
print(prac_data.head())

numeric_col =['Days Present', 'Sales Revenue Generated']
fig, axes = plt.subplots( 1, 2, figsize=(12 ,6))

for index,column in enumerate(numeric_col):
    sns.kdeplot(prac_data[column],ax = axes[index])
    axes[index].set_title(f'KDE plot of { column}')

plt.tight_layout()
plt.show()