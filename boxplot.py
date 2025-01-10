import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_excel('boxplot_data.xlsx')
print (data.head())

plt.figure(figsize=(10,8))
sns.boxplot(x='Task Completion Rates', y='churned', data=data)
plt.title('median Task Completion Rates ')
plt.xlabel('The label of the x-axis')
plt.show()