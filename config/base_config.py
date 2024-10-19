import os
from dotenv import load_dotenv

load_dotenv()

# Base configuration for all recommenders
BASE_CONFIG = {
    'data_path': os.getenv('MOVIE_DATA_PATH', "data/metadata_with_imdb_metadata.csv"),
    'embedding_model': os.getenv('EMBEDDING_MODEL', 'all-MiniLM-L6-v2'),
    'model_path': os.getenv('MODEL_PATH', 'models/'),
    'faiss_index_file': os.getenv('FAISS_INDEX_FILE', 'faiss_index.bin'),
    'embeddings_file': os.getenv('EMBEDDINGS_FILE', 'movie_embeddings.pkl'),
    'top_n': int(os.getenv('TOP_N', 5)),
    'recommender_type': os.getenv('RECOMMENDER_TYPE', 'faiss_recommender'),
    'mlflow_tracking_uri': os.getenv('MLFLOW_TRACKING_URI', 'http://localhost:5000'),
    'mlflow_experiment_name': os.getenv('MLFLOW_EXPERIMENT_NAME', 'movie_recommender'),
    'mlflow_run_name': os.getenv('MLFLOW_RUN_NAME', 'faiss_recommender'),
    'sql_server_connection': os.getenv('SQL_SERVER_CONNECTION', 'Driver={SQL Server};Server=ALIEN;Database=newMovieDB;Trusted_Connection=yes;'),
    'sqlalchemy_connection_string': os.getenv(
            'SQLALCHEMY_DATABASE_URI',
            'mssql+pyodbc://ALIEN/newMoviesDB?driver=ODBC+Driver+17+for+SQL+Server'
        )
}
