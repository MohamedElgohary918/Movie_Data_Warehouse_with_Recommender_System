import os
import pandas as pd
import numpy as np
import streamlit as st
from sentence_transformers import SentenceTransformer
import faiss
import joblib  # Import joblib to save and load the embeddings

class MovieRecommender:
    def __init__(self, movie_data_path):
        self.movies = pd.read_csv(movie_data_path)
        self.model = SentenceTransformer('all-MiniLM-L6-v2')  # Load pre-trained sentence transformer
        self.movie_embeddings = None
        self.index = None
        self.embeddings_file = "models/movie_embeddings.pkl"  # Filename to save embeddings

    def preprocess_data(self):
        # Combine relevant features for content-based filtering
        self.movies['combined_features'] = (
            self.movies['title'].fillna('') + " " +
            self.movies['genres'].fillna('') + " " +
            self.movies['directedBy'].fillna('') + " " +
            self.movies['starring'].fillna('')
        )

    def train_model(self):
        """Train the recommendation model and create the Faiss index."""
        # Preprocess data
        self.preprocess_data()
        
        # Generate embeddings for combined features
        self.movie_embeddings = self.model.encode(self.movies['combined_features'].tolist(), show_progress_bar=True)
        
        # Save embeddings to disk
        joblib.dump(self.movie_embeddings, self.embeddings_file)

        # Create Faiss index
        self.index = faiss.IndexFlatL2(self.movie_embeddings.shape[1])  # Use L2 distance
        self.index.add(np.array(self.movie_embeddings).astype(np.float32))  # Add data to the index

        # Save the Faiss index to a file
        faiss_index_file = "models/faiss_index.bin"
        faiss.write_index(self.index, faiss_index_file)

    def load_model(self):
        """Load the saved model artifacts."""
        # Load the embeddings
        self.movie_embeddings = joblib.load(self.embeddings_file)

        # Create the Faiss index
        self.index = faiss.read_index("models/faiss_index.bin")

    def get_recommendations(self, title, top_n=5):
        """Get movie recommendations based on the trained model."""
        # Ensure the model is loaded before making recommendations
        if self.movie_embeddings is None or self.index is None:
            st.warning("Model not loaded. Loading now...")
            self.load_model()

        # Check if the movie exists
        if title not in self.movies['title'].values:
            st.error(f"Movie '{title}' not found in the dataset.")
            return None

        # Get the index of the movie
        movie_idx = self.movies[self.movies['title'] == title].index[0]

        # Get the embedding of the chosen movie
        movie_vector = self.movie_embeddings[movie_idx].reshape(1, -1).astype(np.float32)

        # Search for similar movies in the Faiss index
        D, I = self.index.search(movie_vector, top_n + 1)  # Get top N + 1 to exclude the movie itself

        # Return the recommended movie titles and their corresponding data
        recommended_movies = self.movies.iloc[I[0][1:]]  # Skip the first one (the movie itself)
        return recommended_movies
