import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "sqlite:///data/db/bluestock_mf.db"
)

# Load datasets
fund_master = pd.read_csv(
    "data/raw/01_fund_master.csv"
)

nav = pd.read_csv(
    "data/processed/02_nav_history_cleaned.csv"
)

transactions = pd.read_csv(
    "data/processed/08_investor_transactions_cleaned.csv"
)

performance = pd.read_csv(
    "data/processed/07_scheme_performance_cleaned.csv"
)

aum = pd.read_csv(
    "data/raw/03_aum_by_fund_house.csv"
)

# Save tables
fund_master.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

transactions.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

performance.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

aum.to_sql(
    "fact_aum",
    engine,
    if_exists="replace",
    index=False
)

print("SQLite database loaded successfully")