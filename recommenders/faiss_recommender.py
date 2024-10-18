import os
import faiss
import joblib
import mlflow
import streamlit as st
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.exc import SQLAlchemyError
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from recommenders.recommender import MovieRecommenderBase
from config.base_config import BASE_CONFIG

class FaissRecommender(MovieRecommenderBase):
    def __init__(self, data_path, model_path):
        super().__init__(data_path)
        self.model_path = model_path
        self.model = SentenceTransformer(BASE_CONFIG['embedding_model'])
        self.movies = None
        self.index = None
        self.movie_embeddings = None
        self.csv_file = BASE_CONFIG['data_path']
        self.sql_connection = BASE_CONFIG['sqlalchemy_connection_string']
        self.engine = create_engine(self.sql_connection)
        self.metadata = MetaData()
        self.movies_table = Table('Movies', self.metadata, autoload_with=self.engine)
        self.starring_table = Table('actors', self.metadata, autoload_with=self.engine)
        self.directors_table = Table('director', self.metadata, autoload_with=self.engine)


    def load_data_from_sql(self):
        """Fetch movie data including genres, directors, and starring, then save it to a CSV file."""
        try:
            # Delete existing CSV file if it exists
            if os.path.exists(self.csv_file):
                os.remove(self.csv_file)

            # Query to fetch the data
            query = """
            SELECT m.title, 
                    GROUP_CONCAT(DISTINCT s.name) AS starring, 
                    GROUP_CONCAT(DISTINCT d.name) AS directedBy, 
                    m.genres, m.total_rating, m.votes, m.cover_url_better
            FROM Movies m
            LEFT JOIN MovieActor sm ON m.movie_id = sm.movie_id
            LEFT JOIN actors s ON sm.starring_id = s.starring_id
            LEFT JOIN MovieDirector dm ON m.movie_id = dm.movie_id
            LEFT JOIN director d ON dm.director_id = d.director_id
            GROUP BY m.title, m.genres, m.total_rating, m.votes, m.cover_url_better;
            """

            # Execute the query and fetch the data
            result = pd.read_sql(query, self.engine)
            
            # Save the result to a CSV file
            result.to_csv(self.csv_file, index=False)
            print("Movie data saved to CSV successfully.")
        except SQLAlchemyError as e:
            print(f"An error occurred while fetching movie data: {e}")
    
    def load_movies(self):
        """Load movie data from CSV or SQL."""
        # Check if the CSV file exists
        if not os.path.exists(self.csv_file):
            # If CSV doesn't exist, load from SQL and save
            self.load_data_from_sql()
        print("Loading movie data from CSV...")
        # Load the CSV data
        self.movies = pd.read_csv(self.csv_file)

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
        # Load and preprocess data
        self.load_data()
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
  
        
        # Ensure the model is loaded before making recommendations
        if self.movie_embeddings is None or self.index is None:
            st.warning("Model not loaded. Loading now...")
            self.load_model()

        # Check if the movie exists
        if title not in self.movies['title'].values:
            st.error(f"Movie '{title}' not found in the dataset.")
            return None

        movie_idx = self.movies[self.movies['title'] == title].index[0]
        movie_vector = self.movie_embeddings[movie_idx].reshape(1, -1).astype(np.float32)

        _, I = self.index.search(movie_vector, top_n + 1)

        return self.movies.iloc[I[0][1:]]  # Skip the first result (itself)
