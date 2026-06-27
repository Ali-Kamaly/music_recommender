import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

df = pd.read_csv('data/processed/processed_dataset.csv')
similarity_features = ['danceability','energy','loudness','speechiness','acousticness','instrumentalness',
                'liveness','valence','tempo']

song_vectors = df[similarity_features].values

k_values = [3,7,10,25]

for k in k_values:
    print(f"\n ------K: {k}------")
    kmeans = KMeans(n_clusters = k, random_state = 217, n_init = 10)

    cluster_labels = kmeans.fit_predict(song_vectors)

    score = silhouette_score(
        song_vectors,
        cluster_labels,
        sample_size = 10000,
        random_state = 217
    )

    print(f"Silhouette score: {score}")