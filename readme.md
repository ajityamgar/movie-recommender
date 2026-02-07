# 🎬 Movie Recommendation System (Machine Learning Project)

A **Machine Learning–based Movie Recommendation System** built with Python and Streamlit.
This project focuses on **similarity-based recommendations** and the **end-to-end journey** of taking an ML model from local experiments to a deployed, usable web application.

> The system is functional but intentionally not perfect — because the real learning came from iteration, debugging, and deployment challenges.

---

## 🚀 Live Demo

🔗 **Live App:** https://lnkd.in/dqxvPUr
🔗 **GitHub Repository:** https://lnkd.in/duYYVCwc

---

## 📌 Project Overview

This application recommends movies based on **content similarity**.
Users select a movie, and the system suggests **top 5 similar movies** along with their posters, fetched dynamically from the **TMDB API**.

The focus of this project is:

* Practical Machine Learning
* Clean data handling
* Performance-aware deployment
* Real-world engineering constraints

---

## 🧠 How the Recommendation System Works

1. **Movie Metadata Processing**
   Movie data is preprocessed and stored as a serialized file (`movies.pkl`).

2. **Similarity Matrix**
   A precomputed similarity matrix (`similarity.pkl`) is used to calculate how closely movies are related.

3. **Similarity-Based Recommendation**

   * The selected movie index is identified
   * Cosine similarity scores are used
   * Top 5 most similar movies are returned

4. **Poster Fetching**
   Movie posters are fetched in real time using the **TMDB API**.

---

## 🛠️ Tech Stack

* **Programming Language:** Python
* **Web Framework:** Streamlit
* **Machine Learning:** Similarity-based recommendation
* **Data Handling:** Pandas, NumPy
* **Model Storage:** Pickle (`.pkl` files)
* **External API:** TMDB API (movie posters)
* **File Hosting:** Google Drive (via `gdown`)

---

## 📂 Project Structure

```text
movie-recommender/
│
├── apps.py              # Streamlit application
├── requirements.txt     # Project dependencies
├── data/
│   ├── movies.pkl       # Movie dataset
│   └── similarity.pkl   # Similarity matrix
└── README.md            # Project documentation
```

> Large `.pkl` files are downloaded automatically from Google Drive to avoid GitHub size limits.

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/harshadk-3107/movie-recommender.git
cd movie-recommender
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application

```bash
streamlit run apps.py
```

The app will open automatically in your browser.

---

## 📦 Dependencies

```txt
streamlit
pandas
numpy
scikit-learn
gdown
requests
```

---

## 🎯 Key Learnings from This Project

* How **similarity-based ML recommendation systems** work internally
* Cleaning and structuring **real-world movie datasets**
* Converting an ML model into a **usable web application**
* Managing **large ML files**, GitHub limits, and deployment constraints
* Understanding why **deployment often teaches more than model building**
* Realizing that **Machine Learning is not just about models — it’s about shipping usable systems**

---

## ⚠️ Current Limitations

* Cold-start problem for new users
* No user personalization
* Precomputed similarity matrix (no real-time training)
* Limited explainability of recommendations

These limitations are **intentional learning points** and will be addressed in future iterations.

---

## 🔮 Future Improvements

* Hybrid recommendation system (Content + Collaborative)
* Explainable recommendations ("Why this movie?")
* User preference profiling
* API-based recommendation service
* Improved UI/UX
* Dockerized deployment

---

## 🧪 Why This Project Matters

This project demonstrates **real-world ML engineering**, not just algorithms:

* Practical trade-offs
* Deployment constraints
* Iterative improvement mindset

> Still iterating. Still improving. Still learning.
---

⭐ If you found this project useful, consider starring the repository.
