import streamlit as st
from recommend import get_recommendations

st.title("Orbit")
st.write("Music that revolves around you")

num_songs = st.number_input("How many songs would you like to enter: ", min_value = 1)

song_names = []
artists = []

for i in range(num_songs):
    song_name = st.text_input(f"Song {i+1} Name")
    artist_name = st.text_input(f"Artist {i+1} name(s) : ")
    song_names.append(song_name)
    artists.append(artist_name)

if st.button("Recommend"):
    result = get_recommendations(song_names, artists)
    if result is None:
        st.error("Song not found :(")
    else:
        recommendations, distances = result
        recommendations = recommendations.copy()
        recommendations['distance'] = distances[0].round(3)
        st.dataframe(recommendations[["track_name","artists","distance"]])
        