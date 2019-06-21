import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from scipy.stats import norm
from scipy.stats import expon
from scipy.stats import binom
from scipy.stats import poisson

df = pd.read_csv('bigmartsalestrain.csv')
#train = pd.read_csv('bigmartsalestrain.csv')

#df = pd.concat([train, test], ignore_index=True, sort=True)

df.head()

df.describe()

df.isnull().sum()

df.columns

##Target Variable: Item_Outlet_Sales
##

#Removing null values
avg_weight = df.['Item_Weight'].mean()
Item_Weight_missing = df.['Item_Weight'].isnull()
df.loc[Item_Weight_missing, 'Item_Weight'] = avg_weight


missing = df['Outlet_Size'].isnull()
Outlet_Size_missing = df.['Outlet_Size'].isnull()
df.loc[Outlet_Size_missing, 'Outlet_Size'] = missing

df['Item_Fat_Content'] = df['Item_Fat_Content'].replace({'LF':'Low Fat', 'reg':'Regular', 'low fat':'Low Fat'})

#Outlet sizes are medium, true, small and high **Needs to be changed, doesn't make sense
#Outlet_types are Grocery store, supermarkets 1, 2, and 3, this is fine for now

pd.crosstab(df['Outlet_Location_Type'], df['Outlet_Size'], margins=True)

df['Item_Real_Type'] = df['Item_Identifier'].apply(lambda x: x[0:2])
df['Item_Real_Type'] = df['Item_Real_Type'].map({'NC':'Non-Consumables', 'FD':'Food', 'DR':'Drink'})

