import os
from datetime import datetime

def debug_paths(metadata_path, output_folder):
    """Debug function to check file and folder paths."""
    
    # Step 1: Print file paths
    print(f"Debug Mode: Checking paths...\n")
    
    print(f"Metadata file path: {metadata_path}")
    print(f"Output folder path: {output_folder}")
    
    # Step 2: Check if the file exists
    if not os.path.exists(metadata_path):
        print(f"Error: Metadata file does not exist at {metadata_path}")
    else:
        print(f"Success: Metadata file found at {metadata_path}")

    # Step 3: Check if the output folder exists or needs to be created
    if not os.path.exists(output_folder):
        print(f"Output folder does not exist. It will be created: {output_folder}")
    else:
        print(f"Output folder already exists: {output_folder}")


def get_output_folder():

    today_date = datetime.now().strftime('%Y-%m-%d') 
    output_folder = os.path.join('Transformed_Data', today_date)
    return output_folder


# Get paths for debugging
today_date = datetime.now().strftime('%Y-%m-%d')
METADATA_PATH = os.path.join('Raw_Data', 'csv', today_date, 'metadata.csv')
OUTPUT_FOLDER = get_output_folder()

# Run the debug function to print paths
debug_paths(METADATA_PATH, OUTPUT_FOLDER)