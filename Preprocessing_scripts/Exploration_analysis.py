import pandas as pd
import glob

def load_csv_files(directory_path):
    return glob.glob(directory_path)

def print_column_data_types(df, csv_file):
    print(f"Column data types for {csv_file}:")
    print(df.dtypes)
    print("\n")

def print_summary_statistics(df, csv_file):
    print(f"Summary statistics for {csv_file}:")
    print(df.describe(include='all'))
    print("\n")

def print_missing_values(df, csv_file):
    print(f"Missing values count for {csv_file}:")
    print(df.isnull().sum())
    print("\n")

def print_unique_values(df, csv_file):
    print(f"Unique values count for {csv_file}:")
    for col in df.select_dtypes(include=['object']).columns:
        print(f"{col}: {df[col].nunique()}")
    print("\n")


def analyze_csv_files(directory_path):
    csv_files = load_csv_files(directory_path)
    
    for csv_file in csv_files:
        df = pd.read_csv(csv_file)
        print_column_data_types(df, csv_file)
        print_summary_statistics(df, csv_file)
        print_missing_values(df, csv_file)
        print_unique_values(df, csv_file)

# directory_path = 'Raw_Data/Raw_data_transformed/*.csv'
# analyze_csv_files(directory_path)
