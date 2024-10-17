# Movie Recommendation API

This project utilizes FastAPI to provide an API for movie recommendations.

## Usage

1. Install the requirements:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```
## APIs

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
- **Response**: Returns a list of recommended movies.


