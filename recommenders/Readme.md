# Movie Recommendation System

## Model

The recommendation model uses `SentenceTransformer` to generate embeddings for movie features such as title, genres, directors, and cast. These embeddings are then indexed using `Faiss` for efficient similarity searches, allowing the model to recommend movies based on their content features.
## Transformer Model Explanation

In this project, the **`SentenceTransformer`** model from the `sentence-transformers` library is used to convert textual movie metadata into numerical embeddings. These embeddings capture semantic meaning, allowing us to compute similarities between movies based on their descriptions or metadata.

### How Transformers Work

1. **Input Embedding**: 
   - Transformers take in raw text as input (e.g., movie titles, genres, or descriptions). In our case, this would be the metadata fields from the movies dataset.
   - The text is tokenized (split into smaller units, typically words or subwords) and converted into numerical vectors known as embeddings.

2. **Attention Mechanism**:
   - The core of the transformer model is the *self-attention mechanism*. This allows the model to focus on different parts of the input text dynamically. For example, when processing a movie description, the model can pay attention to words like "action" or "thriller" to understand the genre or mood of the movie.
   - Self-attention helps the model understand relationships between words in a sentence regardless of their positions. For instance, in a description like "This movie, starring a famous actor, is a thrilling action adventure," the model can connect "actor" with "movie" and "action" with "thrilling."

3. **Multi-Headed Attention**:
   - Transformers use *multi-headed attention*, meaning that the model can look at different parts of the text in parallel to capture multiple relationships at once. This leads to a richer understanding of the text's meaning.

4. **Contextual Embeddings**:
   - After applying attention, the model generates *contextual embeddings*, which are vector representations of the text where the meaning of each word is informed by the surrounding words. This means the same word can have different vector representations depending on its context.

5. **Sentence/Document Embeddings**:
   - `SentenceTransformer` fine-tunes pre-trained transformer models (like BERT or RoBERTa) to generate embeddings for entire sentences or documents (like movie metadata in this case). These embeddings capture the overall meaning of the text.
   - In our case, these embeddings are used to represent movies, allowing the recommendation system to compute the similarity between different movies based on their semantic content.

### Why Use Transformers for Recommendations?

- **Semantic Understanding**: Unlike traditional vector representations (like one-hot encoding or TF-IDF), transformer embeddings capture the meaning and context of the text. This allows for more accurate comparisons between movies.
- **Transfer Learning**: The `SentenceTransformer` model builds on large, pre-trained language models that have been trained on massive amounts of text data. This means we can leverage this pre-trained knowledge to understand movie metadata better without having to train a model from scratch.
- **Scalability**: These embeddings can be efficiently indexed using techniques like FAISS (used in this project) for fast similarity search, making it scalable even for large datasets.

### Limitations

- **Computationally Expensive**: Transformer models, particularly for large datasets, can be computationally intensive during both the embedding process and similarity search.

By using `SentenceTransformer`, we are able to generate meaningful embeddings of movie metadata, enabling the system to recommend movies that are semantically similar to the ones a user has already watched or searched for.


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
