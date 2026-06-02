import pandas as pd

df = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

returns_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct"
]

for col in returns_cols:

    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

# Expense ratio check
anomalies = df[
    (df["expense_ratio_pct"] < 0.1)
    |
    (df["expense_ratio_pct"] > 2.5)
]

print("\nExpense Ratio Anomalies:")
print(len(anomalies))

# Save
df.to_csv(
    "data/processed/07_scheme_performance_cleaned.csv",
    index=False
)

print(df.shape)
print("Scheme Performance cleaned")