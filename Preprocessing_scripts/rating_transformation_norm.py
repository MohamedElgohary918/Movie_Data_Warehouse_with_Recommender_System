import pandas as pd
import os

def normalize_ratings(file):
    output_dir = 'Raw_Data/Raw_data_transformed/'
    
    # Load the CSV
    df = pd.read_csv(file)

    # DF with unique user IDs
    users = df[['user_id']].copy().drop_duplicates().reset_index(drop=True)

    # Save the CSV
    users.to_csv(os.path.join(output_dir, 'users.csv'), index=False)

    return "Normalization complete!!"

normalize_ratings('Raw_Data/csv/ratings.csv')



'Just to double check the count of the unique userids'

####################3
# df = pd.read_csv('Raw_Data/csv/ratings.csv')

# unique_user_count = df['user_id'].nunique()

# print(f"Count of unique user_id values: {unique_user_count}")
