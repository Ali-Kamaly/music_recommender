import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv('data/processed/processed_dataset.csv')
similarity_features = ['danceability','energy','loudness','speechiness','acousticness','instrumentalness',
                'liveness','valence','tempo']

song_vectors = df[similarity_features].values

k_values = range(2,51)
inertias = []

for k in k_values:
    kmeans = KMeans(n_clusters = k, random_state = 217, n_init = 10)
    kmeans.fit(song_vectors)
    inertias.append(kmeans.inertia_)

plt.plot(k_values, inertias, marker = 'o')
plt.xlabel("Number of clusters (K)")
plt.ylabel("Inertia")
plt.title("Elbow Method for K-Means")
plt.show()

