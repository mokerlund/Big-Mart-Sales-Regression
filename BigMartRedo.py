import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

df = pd.read_csv('bigmartsalestest.csv')
#train = pd.read_csv('bigmartsalestrain.csv')

#df = pd.concat([train, test], ignore_index=True, sort=True)

df.head()

df.describe()

df.isnull().sum()

df.columns

##Target Variable: Item_Outlet_Sales

#Removing null values
avg_weight = df.Item_Weight.mean()
Item_Weight_missing = df.Item_Weight.isnull()
df.loc[Item_Weight_missing, 'Item_Weight'] = avg_weight


missing = df.Outlet_Size.isnull()
Outlet_Size_missing = df.Outlet_Size.isnull()
df.loc[Outlet_Size_missing, 'Outlet_Size'] = missing

df.Item_Fat_Content.rename(columns={'LF':'Low Fat', 'reg':'Regular', 'low fat':'Low Fat'}, inplace=True)
