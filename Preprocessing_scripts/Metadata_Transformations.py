import pandas as pd
import os
from datetime import datetime

def movie_title_transformation(metadata_path, title_col, name_col, year_col, output_folder):
    """Transform movie titles to extract names and years."""
    
    metadata_csv = pd.read_csv(metadata_path)

    # Transform title col to name col and year col
    metadata_csv[name_col] = metadata_csv[title_col].str.replace(r'\s*\(\d{4}\)', '', regex=True).str.strip()
    metadata_csv[year_col] = metadata_csv[title_col].str.extract(r'\((\d{4})\)')

    # Drop original column
    metadata_csv = metadata_csv.drop(columns=[title_col])

    # Create output folder if not exist
    os.makedirs(output_folder, exist_ok=True)

    # Save transformed data to CSV 
    output_file_path = os.path.join(output_folder, 'Movies.csv')
    metadata_csv.to_csv(output_file_path, index=False)
    
    print(metadata_csv.head()) 
    print(f"Transformed data saved to {output_file_path}")

    return metadata_csv


def extract_starring_actors(metadata_df, output_file_path):
    """Extract and save starring actors from the metadata DataFrame."""

    starring_df = metadata_df[['item_id', 'starring']].copy()

    # Split the 'starring' column, handling NaN values
    starring_df['starring'] = starring_df['starring'].apply(lambda x: x.split(',') if isinstance(x, str) else [])
    starring_df['starring'] = starring_df['starring'].apply(lambda x: [actor.strip() for actor in x])
    starring_dff = starring_df.explode('starring')

    # Save starring actors to CSV
    starring_dff.to_csv(output_file_path, index=False)
    print("Starring actors saved to CSV:")
    print(starring_dff.head())
    
    return starring_dff


def extract_director(input_file_path, output_file_path):
    """Extract and save director information from the input file."""

    df = pd.read_csv(input_file_path)

    # Only select the required columns and Save it
    directed_by_df = df[['item_id', 'directedBy']]
    directed_by_df.to_csv(output_file_path, index=False)

    print(f"Transformed data saved to {output_file_path}")


def remove_column(input_file_path, column_name):
    """Remove a specified column from the CSV file."""
    
    df = pd.read_csv(input_file_path)

    if column_name in df.columns:
        df.drop(columns=[column_name], inplace=True)

    # Drop any columns that are completely empty
    df.dropna(axis=1, how='all', inplace=True)

    df.to_csv(input_file_path, index=False)
    print(f"'{column_name}' column removed from {input_file_path} successfully")



def read_transformed_metadata(input_file_path):
    """Read the transformed metadata from the CSV file."""
    
    df = pd.read_csv(input_file_path)
    return df


def get_output_folder():
    """Create the output folder with today's date."""
    today_date = datetime.now().strftime('%Y-%m-%d') 
    output_folder = os.path.join('Transformed_Data', today_date)
    os.makedirs(output_folder, exist_ok=True) 
    return output_folder

todays_date = datetime.now().strftime('%Y-%m-%d')

# Define paths
METADATA_PATH = os.path.join('Raw_Data', 'csv', todays_date, 'metadata.csv') 
OUTPUT_FOLDER = get_output_folder()  


# Run transformations
metadata_df = movie_title_transformation(METADATA_PATH, 'title', 'names', 'year', OUTPUT_FOLDER)

try:
    metadata_df = movie_title_transformation(METADATA_PATH, 'title', 'names', 'year', OUTPUT_FOLDER)

    OUTPUT_STARRING_ACTORS_PATH = os.path.join(OUTPUT_FOLDER, 'starring_actors.csv')
    starring_actors_df = extract_starring_actors(metadata_df, OUTPUT_STARRING_ACTORS_PATH)

    DIRECTORS_OUTPUT_PATH = os.path.join(OUTPUT_FOLDER, 'directed_by.csv')
    extract_director(METADATA_PATH, DIRECTORS_OUTPUT_PATH)

    # Remove columns
    remove_column(os.path.join(OUTPUT_FOLDER, 'Movies.csv'), 'directedBy')
    remove_column(os.path.join(OUTPUT_FOLDER, 'Movies.csv'), 'starring')

    # Read transformed metadata
    transformed_metadata = read_transformed_metadata(os.path.join(OUTPUT_FOLDER, 'Movies.csv'))
    print(transformed_metadata)

except FileNotFoundError as e:
    print(f"File not found: {e}")
except Exception as e:
    print(f"An error occurred: {e}")



