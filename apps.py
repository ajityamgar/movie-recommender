import streamlit as st
import pickle
import pandas as pd
import requests
import os

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Movie Recommendation System", layout="wide")

# ---------------- LOAD DATA ----------------
@st.cache_resource
def load_data():
    movies = pickle.load(open("data/movies.pkl", "rb"))
    similarity = pickle.load(open("data/similarity.pkl", "rb"))
    return movies, similarity

movies, similarity = load_data()

# ---------------- SAFETY CHECK ----------------
assert movies.shape[0] == similarity.shape[0], "Movies & similarity size mismatch"

# ---------------- POSTER FETCH (BY TITLE) ----------------
TMDB_API_KEY = "8265bd1679663a7ea12ac168da84d2e8"

def fetch_poster(movie_title):
    url = f"https://api.themoviedb.org/3/search/movie"
    params = {
        "api_key": TMDB_API_KEY,
        "query": movie_title
    }

    response = requests.get(url, params=params)
    data = response.json()

    if data.get("results"):
        poster_path = data["results"][0].get("poster_path")
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path

    return "https://via.placeholder.com/300x450?text=No+Poster"

# ---------------- RECOMMEND FUNCTION ----------------
def recommend(movie_title):
    index = movies[movies["title"] == movie_title].index[0]

    distances = list(enumerate(similarity[index]))
    distances = sorted(distances, key=lambda x: x[1], reverse=True)[1:6]

    recommended_names = []
    recommended_posters = []

    for i in distances:
        title = movies.iloc[i[0]]["title"]
        recommended_names.append(title)
        recommended_posters.append(fetch_poster(title))

    return recommended_names, recommended_posters

# ---------------- UI ----------------
st.title("🎬 Movie Recommendation System")
st.write(f"Total movies loaded: **{movies.shape[0]}**")

selected_movie = st.selectbox(
    "Select a movie you like:",
    movies["title"].values
)

if st.button("Recommend 🍿"):
    names, posters = recommend(selected_movie)

    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i])


