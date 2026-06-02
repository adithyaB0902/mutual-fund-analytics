import pandas as pd

df = pd.read_csv(
    "data/processed/07_scheme_performance_cleaned.csv"
)

recommended = df[
    (df["expense_ratio_pct"] < 1.0)
    &
    (df["return_3yr_pct"] > 10)
]

recommended = recommended.sort_values(
    "return_3yr_pct",
    ascending=False
)

print("\nTop Recommended Funds:\n")

print(
    recommended[
        [
            "scheme_name",
            "fund_house",
            "return_3yr_pct",
            "expense_ratio_pct"
        ]
    ].head(10)
)