from fastapi import FastAPI, HTTPException
from recommender import MovieRecommender
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import faiss
import mlflow

app = FastAPI()
recommender = MovieRecommender('metadata_with_imdb_metadata.csv')


@app.on_event("startup")
def load_model():
    recommender.movie_embeddings = joblib.load("movie_embeddings.pkl")
    recommender.index = faiss.read_index("faiss_index.bin")

class MovieRequest(BaseModel):
    title: str
    top_n: int = 5

@app.post("/movies/recommendations/") 
def get_recommendations(request: MovieRequest):
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
