from sqlalchemy import create_engine
import pandas as pd

# Connection string for SQL Server (with Windows Authentication)
server = 'MOHAMED'  # Your server name
database = 'Movies_db'  # Your database name

# Create an engine using SQLAlchemy
connection_string = f'mssql+pyodbc://{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server'
engine = create_engine(connection_string)

# Test connection
try:
    with engine.connect() as conn:
        print("Connection successful!")
except Exception as e:
    print(f"Error: {e}")

# Read CSV files into pandas DataFrames
movies_df = pd.read_csv('Project/movies.csv')
movie_actors_df = pd.read_csv('Project/movie_actors.csv')
movie_director_df = pd.read_csv('Project/movie_director.csv')
ratings_df = pd.read_csv('Project/ratings.csv')

# Clean column names by stripping any leading/trailing spaces
movies_df.columns = movies_df.columns.str.strip()
movie_actors_df.columns = movie_actors_df.columns.str.strip()
movie_director_df.columns = movie_director_df.columns.str.strip()
ratings_df.columns = ratings_df.columns.str.strip()


try:
    with engine.connect() as connection:
        # Load the movies data into the database
        movies_df.to_sql('movies', con=engine, if_exists='append', index=False)
        # Load the movie actors data
        movie_actors_df.to_sql('movie_actors', con=engine, if_exists='append', index=False)
        # Load the movie directors data
        movie_director_df.to_sql('movie_director', con=engine, if_exists='append', index=False)
        # Load the ratings data
        ratings_df.to_sql('ratings', con=engine, if_exists='append', index=False)
    print("Data successfully inserted into SQL Server.")
except Exception as e:
    print(f"Error: {e}")
    print("Could NOt inserted into SQL Server.")

''' 
# Truncate (delete all data) in the CSV files by saving empty DataFrames with column names
movies_df.iloc[0:0].to_csv('Project/movies.csv', index=False)
movie_actors_df.iloc[0:0].to_csv('Project/movie_actors.csv', index=False)
movie_director_df.iloc[0:0].to_csv('Project/movie_director.csv', index=False)
ratings_df.iloc[0:0].to_csv('Project/ratings.csv', index=False)

print("CSV files truncated, keeping only the column names.")
'''