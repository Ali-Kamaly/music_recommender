import streamlit as st
from recommend import get_recommendations

st.title("Orbit")
st.write("Music that revolves around you")

song_name = st.text_input("Song Name")
artist_name = st.text_input("Artist name(s): ")

if st.button("Recommend"):
    recommendations, distances = get_recommendations([song_name], [artist_name])
    st.dataframe(recommendations[["track_name","artists"]])