import streamlit as st
from recommenders.model_interface import RecommenderFactory
from config.base_config import BASE_CONFIG
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mlflow


app = FastAPI()

# Initialize Recommender
recommender = RecommenderFactory.get_recommender(BASE_CONFIG['recommender_type'], BASE_CONFIG)

# Streamlit app title
st.title("Movie Recommendation System")

# Train model
# if st.button("Train Model"):
#     with st.spinner("Training model..."):
#         recommender.train_model()
#     st.success("Model trained successfully!")

recommender.load_movies()
# Get movie recommendations
movie_choice = st.selectbox("Choose a movie", recommender.movies['title'])
# Button to get recommendations
if st.button("Get Recommendations"):
    # Show recommendations when a movie is selected
    if movie_choice:
        recommendations = recommender.get_recommendations(movie_choice)
        st.write(f"Movies similar to: {movie_choice}")

        # Split the recommendations into chunks to create a carousel-like effect
        chunk_size = 5  # Number of movies per row
        for i in range(0, len(recommendations), chunk_size):
            row_movies = recommendations.iloc[i:i + chunk_size]  # Get the current chunk of movies

            # Create a row of movie posters
            cols = st.columns(chunk_size)  # Create columns for each movie in the row
            for col, (_, movie) in zip(cols, row_movies.iterrows()):
                with col:
                    st.image(movie['cover_url_better'], caption=movie['title'])
                    # st.write(f"Genres: {movie['genres']}")
                    # st.write(f"Rating: {movie['total_rating']}")
    else:
        st.warning("Please select a movie first!")







# API endpoint to get recommendations =================================================
class MovieRequest(BaseModel):
    title: str
    top_n: int = 5

@app.post("/movies/recommendations/") 
def get_recommendations(request: MovieRequest):
    with mlflow.start_run(nested=True):
        
        mlflow.log_param("requested_title", request.title)
        mlflow.log_param("requested_top_n", request.top_n)
        
        recommendations = recommender.get_recommendations(request.title, request.top_n)

        if recommendations is None:
            raise HTTPException(status_code=404, detail="Movie not found")

        recommendations_output = recommendations[['title', 'genres', 'directedBy', 'cover_url_better']].to_dict(orient='records')
        
        mlflow.log_metric("number_of_recommendations", len(recommendations_output))
        
        return {
            "movie": request.title,
            "recommendations": recommendations_output
        }


# create api of train model
@app.post("/train_model/")
def train_model():
    recommender.train_model()
    # st.success("Model trained successfully!")