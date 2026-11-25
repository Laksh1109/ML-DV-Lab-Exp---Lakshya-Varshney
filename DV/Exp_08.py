# Exp_08: Time-series trends, moving average, trendline and simple forecast
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.DataFrame({
    "Month": pd.date_range("2025-01-01", periods=12, freq="MS"),
    "Sales": [100, 110, 115, 120, 125, 130, 135, 140, 150, 155, 160, 170]
})
df["Moving Average (3)"] = df["Sales"].rolling(3).mean()

plt.plot(df["Month"], df["Sales"], marker="o", label="Sales")
plt.plot(df["Month"], df["Moving Average (3)"], label="3-month moving average")
# Simple linear trendline
x = np.arange(len(df))
slope, intercept = np.polyfit(x, df["Sales"], 1)
plt.plot(df["Month"], slope*x + intercept, linestyle="--", label="Trendline")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Linear extrapolation: simple illustrative forecast for next 3 periods
future_x = np.arange(len(df), len(df)+3)
forecast = slope*future_x + intercept
print("Illustrative next 3-month forecast:", forecast.round(2))
