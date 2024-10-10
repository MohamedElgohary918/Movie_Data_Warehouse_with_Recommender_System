## Metadata Transformations

1. **Movie Title Transformation**: 
   - Extracts movie names by removing the release year from the title.
   - Saves the release year as a separate column.

2. **Extract Starring Actors**: 
   - Splits the starring actors' names into separate entries.

3. **Extract Director**: 
   - Saves the director's names into a separate CSV file.

4. **Remove Directors**: 
   - Removes the director column from the transformed metadata.

5. **Remove Starring**: 
   - Removes the starring column from the transformed metadata.

6. **Read Transformed Metadata**: 
   - Reads the transformed metadata from a CSV file.

7. **Drop First Column**: 
   - Drops the first column from the CSV file to clean up the data.


## Actor Transformations

1. **Normalize Starring**: 
   - Splits the starring actors' names into a list and normalizes them by removing extra spaces.
   - Creates a unique list of actors with an assigned `actor_id` and saves it to `actors.csv`.
   - Establishes a relationship between movies and their actors, saving this information to `movie_actors.csv`.


## Rating Transformations

1. **Normalize Ratings**: 
   - Loads the ratings data and creates a DataFrame with unique user IDs.
   - Saves the unique user IDs to a `users.csv` file for further analysis.

## Director Transformations

1. **Normalize Directors**: 
   - Loads the directed data and splits the director names into a list, removing extra spaces.
   - Creates a unique list of directors with an assigned `director_id` and saves it to `director.csv`.
   - Establishes a relationship between items and their directors, saving this information to `items_directors.csv`.

## Data Conversion Transformations

1. **Convert Metadata**: 
   - Loads `metadata.json` and converts it to `metadata.csv`.

2. **Convert Ratings**: 
   - Loads `ratings.json` and converts it to `ratings.csv`.

3. **Convert Reviews**: 
   - Loads `reviews.json` and converts it to `reviews.csv`.

4. **Convert Survey Answers**: 
   - Loads `survey_answers.json` and converts it to `survey_answers.csv`.

5. **Convert Tag Count**: 
   - Loads `tag_count.json` and converts it to `tag_count.csv`.

6. **Convert Tags**: 
   - Loads `tags.json` and converts it to `tags.csv`.
