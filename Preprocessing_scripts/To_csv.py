import pandas as pd
import os

def convert_file_to_csv(file_name, data_path, csv_output_path):
    file_path = os.path.join(data_path, file_name)

    file_name, file_extension= os.path.splitext(file_name)
    file_type = file_extension[1:].lower() 

    if file_type == 'json':
        df = pd.read_json(file_path, lines=True)
    elif file_type in ['xlsx', 'xls']:
        if file_type == 'xlsx':
            df = pd.read_excel(file_path, engine='openpyxl')
        else:
            df = pd.read_excel(file_path, engine='xlrd')
    elif file_type == 'txt':
        df = pd.read_csv(file_path, sep='\t') 
    elif file_type == 'csv':
        df = pd.read_csv(file_path)
    else:
        print(f"Unsupported file type: {file_name}")
        return

    csv_file = f"{file_name}.csv"  
    csv_path = os.path.join(csv_output_path, csv_file)
    df.to_csv(csv_path, index=False)

    print(f"{file_name} has been converted to CSV.")
    print(df.head())

data_path = 'Raw_Data\\movie_dataset_public_final\\raw'
csv_output_path = 'Raw_Data\\movie_dataset_public_final\\csv'

convert_file_to_csv('metadata.json', data_path, csv_output_path)
convert_file_to_csv('ratings.json', data_path, csv_output_path)
convert_file_to_csv('reviews.json', data_path, csv_output_path)
convert_file_to_csv('survey_answers.json', data_path, csv_output_path)
convert_file_to_csv('tag_count.json', data_path, csv_output_path)
convert_file_to_csv('tags.json', data_path, csv_output_path)

