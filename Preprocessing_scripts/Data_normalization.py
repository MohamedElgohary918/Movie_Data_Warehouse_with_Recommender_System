import pandas as pd
from datetime import datetime
import os 

def normalized_directors(file):
    # Load the CSV
    df = pd.read_csv(file)

    # Split and strip director names
    df['directedBy'] = df['directedBy'].str.split(',').apply(lambda x: [d.strip() for d in x] if isinstance(x, list) else [])

    # Create the directors DataFrame
    directors = pd.DataFrame(df['directedBy'].explode().unique(), columns=['director_name'])
    directors['director_id'] = range(1, len(directors) + 1)

    # Create output folder path with today's date if it does not exist
    today_date = datetime.now().strftime('%Y-%m-%d')
    output_folder = os.path.join('Transformed_Data', today_date)
    os.makedirs(output_folder, exist_ok=True)

    # Save the CSV
    directors.to_csv(os.path.join(output_folder, 'director.csv'), index=False)

    # Create the Item_directors relationship
    df_exploded = df.explode('directedBy')  
    items_directors = pd.merge(df_exploded, directors, left_on='directedBy', right_on='director_name')[['item_id', 'director_id']]

    # Save the CSV
    items_directors.to_csv(os.path.join(output_folder, 'items_directors.csv'), index=False)
    
    return "Director Normalization complete!"

def normalize_starring(file):
    # Create output folder path with today's date
    today_date = datetime.now().strftime('%Y-%m-%d')
    output_dir = os.path.join('Transformed_Data', today_date)
    df = pd.read_csv(file)

    df['starring'] = df['starring'].str.split(',').apply(lambda x: [a.strip() for a in x] if isinstance(x, list) else [])

    actors = pd.DataFrame(df['starring'].explode().unique(), columns=['actor_name'])
    actors['actor_id'] = range(1, len(actors) + 1)

    # Save the CSV
    actors.to_csv(os.path.join(output_dir, 'actors.csv'), index=False)

    # Create the MovieActor relationship
    df_exploded = df.explode('starring')
    movie_actors = pd.merge(df_exploded, actors, left_on='starring', right_on='actor_name')[['item_id', 'actor_id']]

    # Save the CSV
    movie_actors.to_csv(os.path.join(output_dir, 'movie_actors.csv'), index=False)

    return "Normalization complete!"

def normalize_ratings(file):
    # Create output folder path with today's date
    today_date = datetime.now().strftime('%Y-%m-%d')
    output_dir = os.path.join('Transformed_Data', today_date)
    
    # Create the output folder if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Load the CSV
    df = pd.read_csv(file)

    # DF with unique user IDs
    users = df[['user_id']].copy().drop_duplicates().reset_index(drop=True)

    # Save the users CSV
    users.to_csv(os.path.join(output_dir, 'users.csv'), index=False)

    return "Normalization complete!!"

today_date = datetime.now().strftime('%Y-%m-%d')

# Call the functions with the specified input paths
normalized_directors(os.path.join('Raw_Data', 'csv', today_date, 'directed_by.csv'))
normalize_starring(os.path.join('Raw_Data', 'csv', today_date, 'starring_actors.csv'))
normalize_ratings(os.path.join('Raw_Data', 'csv', today_date, 'ratings.csv'))
