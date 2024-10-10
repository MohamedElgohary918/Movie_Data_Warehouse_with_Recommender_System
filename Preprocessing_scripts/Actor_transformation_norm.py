import pandas as pd
import os

def normalize_starring(file):
    output_dir = 'Raw_Data/Raw_data_transformed/'
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

normalize_starring('Raw_Data/Raw_data_transformed/starring_actors.csv')
