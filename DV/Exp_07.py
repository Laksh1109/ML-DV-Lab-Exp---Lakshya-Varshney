# Exp_07: Heatmap and Treemap (correlation + category hierarchy)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.DataFrame({
    "Sales": [100, 150, 180, 220, 260],
    "Profit": [20, 35, 40, 55, 65],
    "Quantity": [2, 3, 4, 5, 6],
    "Discount": [0.1, 0.2, 0.1, 0.05, 0.15]
})
sns.heatmap(data.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

# Treemap needs squarify: pip install squarify
try:
    import squarify
    sizes = [500, 300, 200, 150]
    labels = ["Tech\n500", "Furniture\n300", "Office Supplies\n200", "Accessories\n150"]
    squarify.plot(sizes=sizes, label=labels, alpha=0.8)
    plt.axis("off")
    plt.title("Category Sales Treemap")
    plt.show()
except ImportError:
    print("Treemap optional dependency missing: pip install squarify")
