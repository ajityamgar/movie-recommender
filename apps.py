import streamlit as st
import pickle
import pandas as pd
import requests
import os
import gdown

st.set_page_config(page_title="Movie Recommendation System", layout="wide")

MOVIES_URL = "https://drive.google.com/uc?id=1Qds9RT2G-dk1-2pfUVAGsfmacI-XeoqB"
SIMILARITY_URL = "https://drive.google.com/uc?id=15o3_xq2TpRlGnaNTJgCknYieUb9F31EU"

os.makedirs("data", exist_ok=True)

if not os.path.exists("data/movies.pkl"):
    st.write("Downloading movies data...")
    gdown.download(MOVIES_URL, "data/movies.pkl", quiet=False)

if not os.path.exists("data/similarity.pkl"):
    st.write("Downloading similarity data...")
    gdown.download(SIMILARITY_URL, "data/similarity.pkl", quiet=False)

with open("data/movies.pkl", "rb") as f:
    movies = pickle.load(f)

with open("data/similarity.pkl", "rb") as f:
    similarity = pickle.load(f)

st.title("🎬 Movie Recommendation System")
st.write(f"Total movies loaded: **{movies.shape[0]}**")

TMDB_API_KEY = "8265bd1679663a7ea12ac168da84d2e8"

def fetch_poster(movie_title):
    url = "https://api.themoviedb.org/3/search/movie"
    params = {"api_key": TMDB_API_KEY, "query": movie_title}
    data = requests.get(url, params=params).json()
    if data.get("results") and data["results"][0].get("poster_path"):
        return "https://image.tmdb.org/t/p/w500/" + data["results"][0]["poster_path"]
    return "https://via.placeholder.com/300x450?text=No+Poster"

def recommend(movie_title):
    idx = movies[movies["title"] == movie_title].index[0]
    distances = sorted(list(enumerate(similarity[idx])), key=lambda x: x[1], reverse=True)[1:6]
    return [(movies.iloc[i]["title"], fetch_poster(movies.iloc[i]["title"])) for i, _ in distances]

selected_movie = st.selectbox("Select a movie:", movies["title"].values)

if st.button("Recommend 🍿"):
    recs = recommend(selected_movie)
    cols = st.columns(5)
    for col, (name, poster) in zip(cols, recs):
        with col:
            st.text(name)
            st.image(poster)

