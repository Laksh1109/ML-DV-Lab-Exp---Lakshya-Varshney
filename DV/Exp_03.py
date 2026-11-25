# Exp_03: Bar and Line Charts for category comparison and time series
import pandas as pd
import matplotlib.pyplot as plt

sales = pd.DataFrame({
    "Category": ["Furniture", "Technology", "Office Supplies"],
    "Sales": [1250, 2100, 900]
})
sales.plot(kind="bar", x="Category", y="Sales", title="Category-wise Sales", legend=False)
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

trend = pd.DataFrame({
    "Date": pd.date_range("2026-01-01", periods=6, freq="MS"),
    "Sales": [120, 150, 140, 180, 220, 210]
})
plt.plot(trend["Date"], trend["Sales"], marker="o", label="Sales")
plt.title("Monthly Sales Trend")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
