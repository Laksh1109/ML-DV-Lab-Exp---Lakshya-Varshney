# Exp_04: Interactive-style dashboard filters/slicers (Pandas filtering + plots)
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Region": ["East", "West", "East", "North", "West", "North"],
    "Category": ["Tech", "Furniture", "Furniture", "Tech", "Tech", "Furniture"],
    "Date": pd.to_datetime(["2026-01-01","2026-01-02","2026-02-01","2026-02-05","2026-03-01","2026-03-02"]),
    "Sales": [300, 250, 180, 420, 380, 210]
})

# Demonstration of filters (similar to dashboard slicers)
selected_region = "West"
selected_category = "Tech"
filtered = df[(df["Region"] == selected_region) & (df["Category"] == selected_category)]
print("Filtered records:\n", filtered)

df.groupby("Region")["Sales"].sum().plot(kind="bar", title="Sales by Region")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()
