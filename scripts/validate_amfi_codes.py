import pandas as pd

# Load datasets
fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

# Unique AMFI codes
master_codes = set(fund_master["amfi_code"].unique())
nav_codes = set(nav_history["amfi_code"].unique())

# Validation
missing_codes = master_codes - nav_codes

print("=" * 60)
print("AMFI CODE VALIDATION")
print("=" * 60)

print(f"Codes in Fund Master : {len(master_codes)}")
print(f"Codes in NAV History : {len(nav_codes)}")

print(f"\nMissing Codes: {len(missing_codes)}")

if len(missing_codes) > 0:
    print("\nSample Missing Codes:")
    print(list(missing_codes)[:20])
else:
    print("\n✅ All AMFI codes exist in NAV History")