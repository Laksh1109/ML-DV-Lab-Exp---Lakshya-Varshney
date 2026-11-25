# Exp_01: Getting Started with Power BI/Tableau concepts using Pandas
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Category": ["Furniture", "Technology", "Office Supplies"],
    "Sales": [1200, 1800, 900]
})
print(df)  # Table view

df.plot(kind="bar", x="Category", y="Sales", title="Sales by Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

# Simple line view (ordered example)
df.plot(kind="line", x="Category", y="Sales", marker="o", title="Sales by Category")
plt.tight_layout()
plt.show()
