import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#print("All libraries imported successfully!")

data = pd.read_excel('heatmap_data.xlsx')
print (data.head())

correl = round (data [['Task Completion Rates','Decision-Making Skills Rating','Sales Revenue Generated']].corr(),3)
print(correl)

plt.figure(figsize=(10,6))
sns.heatmap(correl, annot=True)
plt.title('The correlation btw Task Completion Rates Decision-Making Skills Rating & Sales Revenue Generated')
plt.show()
