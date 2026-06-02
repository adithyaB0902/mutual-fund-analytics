import sqlite3

conn = sqlite3.connect(
    "bluestock_mf.db"
)

tables = [
    "dim_fund",
    "fact_nav",
    "fact_transactions",
    "fact_performance",
    "fact_aum"
]

for table in tables:

    count = conn.execute(
        f"SELECT COUNT(*) FROM {table}"
    ).fetchone()[0]

    print(f"{table}: {count}")