import pandas as pd

df = pd.read_csv("2.csv")
print(df.columns)
print(df.shape)
del df["Unnamed: 0"]
print(df.shape)
df.to_csv("main.csv")
