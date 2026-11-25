# Exp_06: Pie and Donut charts for category proportions
import matplotlib.pyplot as plt

countries = ["USA", "China", "India", "Japan"]
medals = [40, 32, 25, 18]

plt.pie(medals, labels=countries, autopct="%1.1f%%", startangle=90)
plt.title("Olympic Medal Share")
plt.tight_layout()
plt.show()

# Donut chart: pie with a hole
plt.pie(medals, labels=countries, autopct="%1.1f%%", startangle=90,
        wedgeprops={"width": 0.45})
plt.title("Olympic Medal Share (Donut)")
plt.tight_layout()
plt.show()
