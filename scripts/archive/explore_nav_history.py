import pandas as pd

df = pd.read_csv("data/raw/02_nav_history.csv")

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 Rows:")
print(df.head())