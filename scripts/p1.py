import pandas as pd

df = pd.read_csv("data/raw/02_nav_history.csv")

print(df["date"].isna().sum())
print(len(df))
import pandas as pd

files = [
    "data/raw/HDFC_Top100_NAV.csv",
    "data/raw/SBI_Bluechip.csv",
    "data/raw/ICICI_Bluechip.csv",
    "data/raw/Nippon_LargeCap.csv",
    "data/raw/Axis_Bluechip.csv",
    "data/raw/Kotak_Bluechip.csv"
]

for file in files:
    try:
        df = pd.read_csv(file)
        print("\n", file)
        print(df.head())
        print(df.columns.tolist())
    except Exception as e:
        print(file, e)