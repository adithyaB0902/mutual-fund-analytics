import pandas as pd

df = pd.read_csv("data/raw/02_nav_history.csv")

df["date"] = pd.to_datetime(
    df["date"],
    errors="coerce"
)

print("Missing dates:", df["date"].isna().sum())
print(df["date"].head())

# Sort
df = df.sort_values(
    ["amfi_code", "date"]
)

# Remove duplicates
df = df.drop_duplicates()

# Forward fill NAV within each fund
df["nav"] = (
    df.groupby("amfi_code")["nav"]
      .ffill()
)

# Keep only positive NAV values
df = df[df["nav"] > 0]

# Save
df.to_csv(
    "data/processed/02_nav_history_cleaned.csv",
    index=False
)

print(df.shape)
print("NAV History cleaned successfully")