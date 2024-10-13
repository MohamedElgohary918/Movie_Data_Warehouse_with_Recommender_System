import pandas as pd
import os
from datetime import datetime

def get_data_folder():
    """create the data folder with today's date."""
    today_date = datetime.now().strftime('%Y-%m-%d')
    data_folder = os.path.join('Raw_Data', 'raw', today_date)
    os.makedirs(data_folder, exist_ok=True) 
    return data_folder

def get_csv_output_folder():
    """create the output folder for csv files with today's date."""
    today_date = datetime.now().strftime('%Y-%m-%d')
    csv_output_folder = os.path.join('Raw_Data', 'csv', today_date)
    os.makedirs(csv_output_folder, exist_ok=True)
    return csv_output_folder


def convert_file_to_csv(data_path, csv_output_path):
    """Convert various file types from a specific path to CSV format."""
    for file_name in os.listdir(data_path):
        file_path = os.path.join(data_path, file_name)

        if os.path.isfile(file_path):
            file_name_without_ext, file_extension = os.path.splitext(file_name)
            file_type = file_extension[1:].lower()

            try:
                if file_type == 'json':
                    # Remove lines=True to handle standard JSON arrays
                    df = pd.read_json(file_path)
                elif file_type in ['xlsx', 'xls']:
                    df = pd.read_excel(file_path, engine='openpyxl') if file_type == 'xlsx' else pd.read_excel(file_path, engine='xlrd')
                elif file_type == 'txt':
                    df = pd.read_csv(file_path, sep='\t')
                elif file_type == 'csv':
                    df = pd.read_csv(file_path)
                else:
                    print(f"Unsupported file type: {file_name}")
                    continue 

                # Save DataFrame as CSV
                csv_file = f"{file_name_without_ext}.csv"
                csv_path = os.path.join(csv_output_path, csv_file)
                df.to_csv(csv_path, index=False)
                print(f"{file_name} has been converted to CSV.")
                print(df.head())  #
            except Exception as e:
                print(f"Error processing {file_name}: {e}")
                
data_path = get_data_folder()
csv_output_path = get_csv_output_folder()

# print(data_path)
# print(csv_output_path)

convert_file_to_csv(data_path, csv_output_path)

# convert_file_to_csv('metadata.json', data_path, csv_output_path)
# convert_file_to_csv('ratings.json', data_path, csv_output_path)
# convert_file_to_csv('reviews.json', data_path, csv_output_path)
# convert_file_to_csv('survey_answers.json', data_path, csv_output_path)
# convert_file_to_csv('tag_count.json', data_path, csv_output_path)
# convert_file_to_csv('tags.json', data_path, csv_output_path)
