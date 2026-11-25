# Exp_05: Geo-Visualization with a simple symbol map (latitude/longitude)
import pandas as pd
import matplotlib.pyplot as plt

places = pd.DataFrame({
    "City": ["Delhi", "Mumbai", "Kolkata", "Chennai"],
    "Latitude": [28.61, 19.07, 22.57, 13.08],
    "Longitude": [77.20, 72.87, 88.36, 80.27],
    "Sales": [500, 700, 450, 600]
})

plt.scatter(places["Longitude"], places["Latitude"], s=places["Sales"], alpha=0.6)
for _, row in places.iterrows():
    plt.annotate(row["City"], (row["Longitude"], row["Latitude"]))
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("City Sales Symbol Map (coordinate plot)")
plt.tight_layout()
plt.show()

# For Power BI/Tableau, use Latitude and Longitude fields in a map visual.
