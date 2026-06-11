
import pandas as pd

funds = pd.read_csv("07_scheme_performance_cleaned.csv")

def recommend_funds(risk_level):

    recommendations = (
        funds[
            funds["risk_grade"] == risk_level
        ]
        .sort_values(
            "sharpe_ratio",
            ascending=False
        )
        .head(3)
    )

    return recommendations[
        [
            "scheme_name",
            "fund_house",
            "risk_grade",
            "sharpe_ratio",
            "return_3yr_pct"
        ]
    ]

print(recommend_funds("Moderate"))
