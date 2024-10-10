import pandas as pd

def normalized_directors(file):
    # Load the CSV
    df = pd.read_csv(file)

    # Split and strip director names
    df['directedBy'] = df['directedBy'].str.split(',').apply(lambda x: [d.strip() for d in x] if isinstance(x, list) else [])

    # Create the directors DataFrame
    directors = pd.DataFrame(df['directedBy'].explode().unique(), columns=['director_name'])
    directors['director_id'] = range(1, len(directors) + 1)

    # Save the CSV
    directors.to_csv('Raw_Data/Raw_data_transformed/director.csv', index=False)

    # Create the Item_directors relationship
    df_exploded = df.explode('directedBy')  
    items_directors = pd.merge(df_exploded, directors, left_on='directedBy', right_on='director_name')[['item_id', 'director_id']]

    # Save the CSV
    items_directors.to_csv('Raw_Data/Raw_data_transformed/items_directors.csv', index=False)
    
    return "Normalization complete!"

# Call the function
normalized_directors('Raw_Data/Raw_data_transformed/directed_by.csv')