import os
import faiss
import joblib
import mlflow
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from recommenders.recommender import MovieRecommenderBase

class FaissRecommender(MovieRecommenderBase):
    def __init__(self, data_path, model_path):
        super().__init__(data_path)
        self.model_path = model_path
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.movies = pd.read_csv(self.data_path)
        self.index = None
        self.movie_embeddings = None

    def preprocess_data(self):
        self.movies['combined_features'] = (
            self.movies['title'].fillna('') + " " +
            self.movies['genres'].fillna('') + " " +
            self.movies['directedBy'].fillna('') + " " +
            self.movies['starring'].fillna('')
        )

    def train_model(self):
        """Train model and save embeddings with Faiss."""
        mlflow.start_run()
        
        self.preprocess_data()
        self.movie_embeddings = self.model.encode(self.movies['combined_features'].tolist(), show_progress_bar=True)
        
        # Save embeddings
        joblib.dump(self.movie_embeddings, os.path.join(self.model_path, "movie_embeddings.pkl"))

        # FAISS Index
        self.index = faiss.IndexFlatL2(self.movie_embeddings.shape[1])
        self.index.add(self.movie_embeddings.astype(np.float32))

        # Save FAISS index
        faiss.write_index(self.index, os.path.join(self.model_path, "faiss_index.bin"))

        # Log model and parameters with MLflow
        mlflow.log_param("model_type", "Faiss")
        mlflow.log_artifact(os.path.join(self.model_path, "movie_embeddings.pkl"))
        mlflow.log_artifact(os.path.join(self.model_path, "faiss_index.bin"))
        
        mlflow.end_run()

    def load_model(self):
        self.movie_embeddings = joblib.load(os.path.join(self.model_path, "movie_embeddings.pkl"))
        self.index = faiss.read_index(os.path.join(self.model_path, "faiss_index.bin"))

    def get_recommendations(self, title, top_n=5):
        if self.movie_embeddings is None or self.index is None:
            self.load_model()

        movie_idx = self.movies[self.movies['title'] == title].index[0]
        movie_vector = self.movie_embeddings[movie_idx].reshape(1, -1).astype(np.float32)

        _, I = self.index.search(movie_vector, top_n + 1)

        return self.movies.iloc[I[0][1:]]  # Skip the first result (itself)
