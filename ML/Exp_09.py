# Exp 09: K-Means Clustering
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

X, _ = make_blobs(n_samples=250, centers=4, cluster_std=1.2, random_state=42)
X_scaled = StandardScaler().fit_transform(X)
model = KMeans(n_clusters=4, random_state=42, n_init=10)
labels = model.fit_predict(X_scaled)
print("First 20 labels:", labels[:20])
print("Centres:", model.cluster_centers_)
print("Inertia:", model.inertia_)
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=labels)
plt.scatter(model.cluster_centers_[:, 0], model.cluster_centers_[:, 1], marker="X", s=200)
plt.show()
