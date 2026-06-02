import pandas as pd

files = [
    "08_investor_transactions.csv",
    "07_scheme_performance.csv",
    "03_aum_by_fund_house.csv"
]

for file in files:
    print("\n" + "="*80)
    print(file)

    df = pd.read_csv(f"data/raw/{file}")

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nShape:")
    print(df.shape)

    print("\nFirst 3 Rows:")
    print(df.head(3))