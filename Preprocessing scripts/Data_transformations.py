import pandas as pd
import os

def movie_title_transformation(metadata_path, title_col, name_col, year_col, output_folder):
    metadata_csv = pd.read_csv(metadata_path)

    metadata_csv[name_col] = metadata_csv[title_col].str.replace(r'\s*\(\d{4}\)', '', regex=True).str.strip()
    metadata_csv[year_col] = metadata_csv[title_col].str.extract(r'\((\d{4})\)')
    metadata_csv = metadata_csv.drop(columns=[title_col])  

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    output_file_path = os.path.join(output_folder, 'Transformed_metadata.csv')
    metadata_csv.to_csv(output_file_path, index=False)
    print(metadata_csv.head()) 
    print(f"Transformed data saved to {output_file_path}")

    return metadata_csv


# File paths
METADATA_PATH = os.path.join('Raw_Data', 'csv', 'metadata.csv')
OUTPUT_FOLDER = os.path.join('Raw_Data', 'Raw_data_transformed')

metadata_df = movie_title_transformation(METADATA_PATH, 'title', 'names', 'year', OUTPUT_FOLDER)


def extract_starring_actors(metadata_df, output_file_path):
    starring_df = metadata_df[['item_id', 'starring']].copy()

    # Split the 'starring' column, handling NaN values
    starring_df['starring'] = starring_df['starring'].apply(lambda x: x.split(',') if isinstance(x, str) else [])
    starring_df['starring'] = starring_df['starring'].apply(lambda x: [actor.strip() for actor in x])
    starring_dff = starring_df.explode('starring')

    starring_dff.to_csv(output_file_path, index=False)
    print("Starring actors saved to CSV:")
    print(starring_dff.head())
    
    return starring_dff

OUTPUT_STARRING_ACTORS_PATH = os.path.join('Raw_Data', 'Raw_data_transformed', 'starring_actors.csv')
starring_actors_df = extract_starring_actors(metadata_df, OUTPUT_STARRING_ACTORS_PATH)




def extract_director(input_file_path, output_file_path):

    df = pd.read_csv(input_file_path)

    # Only select the required columns
    directed_by_df = df[['item_id', 'directedBy']]

    # Save to new csv
    directed_by_df.to_csv(output_file_path, index=False)
    print("Directors saved to CSV:")
    print(f"Transformed data saved to {output_file_path}")


output_file = 'Raw_Data/Raw_data_transformed/directed_by.csv'
extract_director(METADATA_PATH, output_file)

def remove_directors(input_file_path):

    df = pd.read_csv(input_file_path)

    # Check if the column exist and remove itt
    if 'directedBy' in df.columns:
        df.drop(columns=['directedBy'], inplace=True)

    # Save the updated DataFrame in the same location
    df.to_csv(input_file_path, index=False)

    print(f"'directedBy' column removed from {input_file_path} successfully")

input_file = 'Raw_Data/Raw_data_transformed/Transformed_metadata.csv'
remove_directors(input_file)


def remove_starring(input_file_path):
    df = pd.read_csv(input_file_path)

    if 'starring' in df.columns:
        df.drop(columns=['starring'], inplace=True)

    df.dropna(axis=1, how='all', inplace=True)

    df.to_csv(input_file_path, index=False)

    print(f"'starring' column removed from {input_file_path}")

remove_starring(input_file)

def read_transformed_metadata(input_file_path):
    df = pd.read_csv(input_file_path)
    return df

# Example usage
input_file = 'Raw_Data/Raw_data_transformed/Transformed_metadata.csv'
transformed_metadata = read_transformed_metadata(input_file)

print(transformed_metadata)