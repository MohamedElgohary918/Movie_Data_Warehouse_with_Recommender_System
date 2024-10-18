# Movie Recommendation System

## Model

The recommendation model uses `SentenceTransformer` to generate embeddings for movie features such as title, genres, directors, and cast. These embeddings are then indexed using `Faiss` for efficient similarity searches, allowing the model to recommend movies based on their content features.

## MLflow Integration

The system integrates with `MLflow` to log parameters and metrics during the recommendation process. Specifically, it logs:
- The requested movie title.
- The number of recommendations requested.
- The number of recommendations returned.

This enables tracking and monitoring of model performance over time.

## API

### Movie Recommendation API
- **Endpoint**: `/movies/recommendations/`
- **Method**: POST
- **Request Body**:
    ```json
    {
      "title": "Movie Title",
      "top_n": 5
    }
    ```
- **Response**: Returns a list of recommended movies with details like title, genres, directors, and cover image.

## Usage

1. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```
2. Start the MLFlow ui:
   ```bash
   mlflow ui
   ```
