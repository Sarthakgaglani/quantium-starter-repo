import pandas as pd
from pathlib import Path

data_path = Path("data")
csv_files = list(data_path.glob("*.csv"))

dfs = []

for file in csv_files:
    df = pd.read_csv(file)

    # Normalize product names
    df["product"] = df["product"].str.strip().str.lower()

    # Filter pink morsel
    df = df[df["product"] == "pink morsel"]

    # Clean price column ($3.00 → 3.00)
    df["price"] = df["price"].str.replace("$", "", regex=False).astype(float)

    # Create Sales column
    df["Sales"] = df["quantity"] * df["price"]

    # Keep required columns
    df = df[["Sales", "date", "region"]]
    df.columns = ["Sales", "Date", "Region"]

    dfs.append(df)

# Combine all files
final_df = pd.concat(dfs, ignore_index=True)

# Save output
final_df.to_csv("processed_sales_data.csv", index=False)

print("✅ Data processing complete. Rows:", len(final_df))
