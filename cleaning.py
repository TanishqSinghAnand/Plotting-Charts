  
import pandas as pd
import csv
df = pd.read_csv('total_stars.csv')
print(df.head())


df.drop(["Unnamed: 0"],axis=1,inplace=True)
df.drop(["Unnamed: 5"],axis=1,inplace=True)
df.drop(["Star_name"], axis=1, inplace=True)
df.drop(["Distance"], axis=1, inplace=True)
df.drop(["Mass"], axis=1, inplace=True)
df.drop(["Radius"], axis=1, inplace=True)
print(df.head())


df.to_csv('Final.csv')
