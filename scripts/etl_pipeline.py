from pathlib import Path
import pandas as pd

RAW_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")

PROCESSED_DIR.mkdir(exist_ok=True)

print("Starting ETL Pipeline...\n")


def clean_nav_history():

    print("Cleaning NAV History...")

    df = pd.read_csv(
        RAW_DIR / "02_nav_history.csv"
    )

    df["date"] = pd.to_datetime(
        df["date"],
        format="%d-%m-%Y",
        errors="coerce"
    )

    df = df.sort_values(
        ["amfi_code", "date"]
    )

    df = df.drop_duplicates()

    df["nav"] = (
        df.groupby("amfi_code")["nav"]
          .ffill()
    )

    df = df[df["nav"] > 0]

    df.to_csv(
        PROCESSED_DIR /
        "02_nav_history_cleaned.csv",
        index=False
    )

    print("✓ NAV History Done")


def clean_transactions():

    print("Cleaning Transactions...")

    df = pd.read_csv(
        RAW_DIR /
        "08_investor_transactions.csv"
    )

    df["transaction_date"] = pd.to_datetime(
        df["transaction_date"],
        errors="coerce"
    )

    df = df[df["amount_inr"] > 0]

    df.to_csv(
        PROCESSED_DIR /
        "08_investor_transactions_cleaned.csv",
        index=False
    )

    print("✓ Transactions Done")


def clean_performance():

    print("Cleaning Scheme Performance...")

    df = pd.read_csv(
        RAW_DIR /
        "07_scheme_performance.csv"
    )

    return_cols = [
        "return_1yr_pct",
        "return_3yr_pct",
        "return_5yr_pct"
    ]

    for col in return_cols:
        df[col] = pd.to_numeric(
            df[col],
            errors="coerce"
        )

    df.to_csv(
        PROCESSED_DIR /
        "07_scheme_performance_cleaned.csv",
        index=False
    )

    print("✓ Performance Done")


def process_remaining():

    files = [
        "01_fund_master.csv",
        "03_aum_by_fund_house.csv",
        "04_monthly_sip_inflows.csv",
        "05_category_inflows.csv",
        "06_industry_folio_count.csv",
        "09_portfolio_holdings.csv",
        "10_benchmark_indices.csv"
    ]

    for file in files:

        df = pd.read_csv(
            RAW_DIR / file
        )

        df = df.drop_duplicates()

        output = file.replace(
            ".csv",
            "_cleaned.csv"
        )

        df.to_csv(
            PROCESSED_DIR / output,
            index=False
        )

        print(f"✓ {output}")


try:

    clean_nav_history()

    clean_transactions()

    clean_performance()

    process_remaining()

    print("\nETL Pipeline Completed Successfully!")

except Exception as e:

    print(
        f"Pipeline Failed: {e}"
    )