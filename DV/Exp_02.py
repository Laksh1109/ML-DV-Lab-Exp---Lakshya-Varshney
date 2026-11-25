# Exp_02: Data Cleaning and Transformation (Pandas / Power Query concepts)
import pandas as pd

df = pd.DataFrame({
    "Customer Name": ["Asha", "Ravi", None, "Neha"],
    "Sales Amount": [250, None, 450, 300],
    "Order Date": ["2026-01-02", "2026-01-05", "bad-date", "2026-01-10"]
})

df = df.drop_duplicates()
df["Customer Name"] = df["Customer Name"].fillna("Unknown")
df["Sales Amount"] = df["Sales Amount"].fillna(df["Sales Amount"].mean())
df.rename(columns={"Sales Amount": "Sales"}, inplace=True)
df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")
df["Sales Band"] = df["Sales"].apply(lambda x: "High" if x >= 350 else "Low")
print(df)
