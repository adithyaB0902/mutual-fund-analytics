import pandas as pd
import os

DATA_PATH = "data/raw"

csv_files = sorted([
    file for file in os.listdir(DATA_PATH)
    if file.endswith(".csv")
])

print(f"\nFound {len(csv_files)} CSV files\n")

for file in csv_files:

    print("\n" + "=" * 80)
    print(f"FILE: {file}")
    print("=" * 80)

    try:
        df = pd.read_csv(os.path.join(DATA_PATH, file))

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

    except Exception as e:
        print(f"Error reading {file}: {e}")