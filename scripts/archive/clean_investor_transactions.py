import pandas as pd

df = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

# Date conversion
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"],
    errors="coerce"
)

# Standardize transaction types
df["transaction_type"] = (
    df["transaction_type"]
      .astype(str)
      .str.strip()
      .str.upper()
)

mapping = {
    "SIP": "SIP",
    "SYSTEMATIC INVESTMENT PLAN": "SIP",
    "LUMPSUM": "Lumpsum",
    "LUMP SUM": "Lumpsum",
    "REDEMPTION": "Redemption"
}

df["transaction_type"] = (
    df["transaction_type"]
    .replace(mapping)
)

# Amount validation
df = df[df["amount_inr"] > 0]

# KYC validation
valid_kyc = [
    "VERIFIED",
    "PENDING",
    "REJECTED"
]

df["kyc_status"] = (
    df["kyc_status"]
    .astype(str)
    .str.upper()
)

invalid_kyc = df[
    ~df["kyc_status"].isin(valid_kyc)
]

print("\nInvalid KYC Records:")
print(len(invalid_kyc))

# Save
df.to_csv(
    "data/processed/08_investor_transactions_cleaned.csv",
    index=False
)

print(df.shape)
print("Investor Transactions cleaned")