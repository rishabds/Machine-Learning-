import matplotlib.pyplot as plt
import seaborn as sns ; sns.set()
import numpy as np
from sklearn.cluster import KMeans



from sklearn.datasets.samples_generator import make_blobs
X,y_true = make_blobs(n_samples = 400, centers = 4, cluster_std = 0.60,random_state =0)

kmeans = KMeans(n_clusters=4)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)

plt.scatter(X[:, 0], X[:,1], s=100, c = y_kmeans, cmap='winter');
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c = 'black', s = 30, alpha =0.9);
plt.show()