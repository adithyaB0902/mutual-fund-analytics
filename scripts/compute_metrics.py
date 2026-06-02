from pathlib import Path
import pandas as pd

DATA_DIR = Path("data/processed")

print("Computing Performance Metrics...")

df = pd.read_csv(
    DATA_DIR /
    "07_scheme_performance_cleaned.csv"
)

metrics = df[[
    "amfi_code",
    "scheme_name",
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "expense_ratio_pct"
]]

output_file = (
    DATA_DIR /
    "performance_metrics.csv"
)

metrics.to_csv(
    output_file,
    index=False
)

print(metrics.head())

print(
    f"\nSaved: {output_file}"
)