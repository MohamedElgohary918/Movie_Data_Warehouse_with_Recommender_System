
# Movie Dataset

This dataset contains raw movie data from MovieLens, providing a comprehensive overview of movies, reviews, tags, ratings, and user survey responses.

## File Structure

### raw/metadata.json
- Contains information about movies from MovieLens with **84,661 lines** of JSON objects.
- Fields:
  - **title**: Movie title (84,484 unique titles).
  - **directedBy**: Directors separated by a comma.
  - **starring**: Actors separated by a comma.
  - **dateAdded**: Date when the movie was added to MovieLens.
  - **avgRating**: Average rating of a movie on MovieLens.
  - **imdbId**: Movie ID on the IMDb website (84,661 unique IDs).
  - **item_id**: Movie ID, consistent across files (84,661 unique IDs).
- Example line:
  ```json
  {"title": "Toy Story (1995)", "directedBy": "John Lasseter", "starring": "Tim Allen, Tom Hanks, ...", "dateAdded": null, "avgRating": 3.89146, "imdbId": "0114709", "item_id": 1}
  ```

### raw/reviews.json
- Contains **2,624,608 lines** of movie reviews collected from the IMDb website.
- Fields:
  - **item_id**: Movie ID (52,081 unique IDs).
  - **txt**: Review text.
- Example line:
  ```json
  {"item_id": 172063, "txt": "one-shot record of a belly dancer; ..."}
  ```

### raw/tags.json
- Contains **1,094 lines** of JSON objects.
- Fields:
  - **tag**: Tag string.
  - **id**: Tag ID (1,094 unique IDs).
- Example line:
  ```json
  {"tag": "whitewash", "id": 1}
  ```

### raw/tag_count.json
- Contains **212,704 lines** of JSON objects.
- Fields:
  - **item_id**: Movie ID (39,685 unique IDs).
  - **tag_id**: Tag ID (1,094 unique IDs).
  - **num**: Number of times users have attached the tag to the movie.
- Example line:
  ```json
  {"item_id": 1, "tag_id": 2198, "num": 2}
  ```

### raw/ratings.json
- Contains **28,490,116 lines** of JSON objects.
- Fields:
  - **item_id**: Movie ID (67,873 unique IDs).
  - **user_id**: User ID (247,383 unique IDs).
  - **rating**: Number of stars (0.5 to 5).
- Example line:
  ```json
  {"item_id": 5, "user_id": 997206, "rating": 3.0}
  ```

### raw/survey_answers.json
- Contains **58,903 lines** of JSON objects.
- Fields:
  - **user_id**: User ID (679 unique IDs).
  - **item_id**: Movie ID (5,546 unique IDs).
  - **tag_id**: Tag ID (1,094 unique IDs).
  - **score**: Movie-tag rating (1 to 5 or -1 for unsure).
- Example line:
  ```json
  {"user_id": 978707, "item_id": 3108, "tag_id": 50126, "score": 3}
  ```


