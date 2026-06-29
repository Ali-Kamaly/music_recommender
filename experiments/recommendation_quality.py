import pandas as pd
import numpy as np
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.recommend import find_closest_songs


similarity_features = ['danceability','energy','loudness','speechiness','acousticness','instrumentalness',
                    'liveness','valence','tempo']
df = pd.read_csv('data/processed/clustered_dataset.csv')

def get_recommendation_set(recommendations):
    rec_set = set()
    for _, row in recommendations.iterrows():
        rec_set.add((row['track_name'], row['artists']))
    return rec_set

def get_jaccard_score(normal_recs, clustered_recs):
    normal_set = get_recommendation_set(normal_recs)
    clustered_set = get_recommendation_set(clustered_recs)

    intersection = normal_set & clustered_set
    union = normal_set | clustered_set

    if len(union) == 0:
        return 0
    
    return len(intersection)/len(union)

#normal KNN recommendations
indices_tested = []
default_song_vectors = df[similarity_features].values
scores = []

for _ in range(1000):
    query_index = np.random.randint(0, len(df))
    while query_index in indices_tested:
        query_index = np.random.randint(0, len(df))
    indices_tested.append(query_index)

    query_vector = df.loc[[query_index], similarity_features].values
    normal_recs, distances = find_closest_songs(query_vector, default_song_vectors, df)

    #print(f"Query: {df.loc[query_index, 'track_name']} | {df.loc[query_index, 'artists']}")

    #print(f"--- Normal KNN Recommendations ---")

    #print(f"--- Random query index: {query_index}---")
    #print(normal_recs)

#clustered KNN recommendations
    query_cluster = df.loc[query_index, 'cluster']

    cluster_df = df[df['cluster'] == query_cluster]
    cluster_vectors = cluster_df[similarity_features].values
    clustered_recs, distances = find_closest_songs(query_vector, cluster_vectors, cluster_df)
    #print(f"--- Clustered KNN Recommendations ---")

    #print(f"--- Random query index: {query_index}---")
    #print(clustered_recs)

    score = get_jaccard_score(normal_recs, clustered_recs)
    #print(score)
    scores.append(score)

print(f"Mean Jaccard score: {np.mean(scores)}")
print(f"Median Jaccard score: {np.median(scores)}")
print(f"Max Jaccard score: {np.max(scores)}")
print(f"Min Jaccard score: {np.min(scores)}")


