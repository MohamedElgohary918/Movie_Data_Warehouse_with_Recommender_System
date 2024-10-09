import pandas as pd

# Load and convert metadata.json
metadata_df = pd.read_json('Raw_Data\\movie_dataset_public_final\\raw\\metadata.json', lines=True)
metadata_df.to_csv('Raw_Data\\movie_dataset_public_final\\csv\\metadata.csv', index=False)
print("Metadata saved to CSV:")
print(metadata_df.head())
print()

# Load and convert ratings.json
ratings_df = pd.read_json('Raw_Data\\movie_dataset_public_final\\raw\\ratings.json', lines=True)
ratings_df.to_csv('Raw_Data\\movie_dataset_public_final\\csv\\ratings.csv', index=False)
print("Ratings saved to CSV:")
print(ratings_df.head())
print()

# Load and convert reviews.json
reviews_df = pd.read_json('Raw_Data\\movie_dataset_public_final\\raw\\reviews.json', lines=True)
reviews_df.to_csv('Raw_Data\\movie_dataset_public_final\\csv\\reviews.csv', index=False)
print("Reviews saved to CSV:")
print(reviews_df.head())
print()

# Load and convert survey_answers.json
survey_answers_df = pd.read_json('Raw_Data\\movie_dataset_public_final\\raw\\survey_answers.json', lines=True)
survey_answers_df.to_csv('Raw_Data\\movie_dataset_public_final\\csv\\survey_answers.csv', index=False)
print("Survey Answers saved to CSV:")
print(survey_answers_df.head())
print()

# Load and convert tag_count.json
tag_count_df = pd.read_json('Raw_Data\\movie_dataset_public_final\\raw\\tag_count.json', lines=True)
tag_count_df.to_csv('Raw_Data\\movie_dataset_public_final\\csv\\tag_count.csv', index=False)
print("Tag Count saved to CSV:")
print(tag_count_df.head())
print()

# Load and convert tags.json
tags_df = pd.read_json('Raw_Data\\movie_dataset_public_final\\raw\\tags.json', lines=True)
tags_df = tags_df.to_csv('Raw_Data\\movie_dataset_public_final\\csv\\tags.csv', index=False)
print(f"wow {tags_df.head()}")

