import pandas as pd


data = "e_t_Data/scrubbed.csv/scrubbed.csv"

df = pd.read_csv(data, low_memory=False)

print(df.head())

print(df.tail())

print(df.shape)

print(df.columns)

print(df.info())

