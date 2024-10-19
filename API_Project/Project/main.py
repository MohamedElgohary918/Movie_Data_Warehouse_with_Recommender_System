import csv
import random
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Define the Rating model (Request Body)
class Rating(BaseModel):
    movie_id: int
    user_id: int
    rating: float

# Function to append rating to CSV file
def write_rating_to_csv(rating_data: Rating):
    file_path = 'ratings.csv'
    
    # Open the file in append mode
    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        
        # Check if file is empty (no header) to write the header
        file_empty = file.tell() == 0
        if file_empty:
            writer.writerow(['movie_id', 'user_id', 'rating'])  # Write header if file is empty
        
        # Write the rating data
        writer.writerow([rating_data.movie_id, rating_data.user_id, rating_data.rating])

@app.post("/add-rating/")
async def add_rating(rating: Rating):
    # Validation: Ensure rating is between 0 and 5
    if rating.rating < 0 or rating.rating > 5:
        raise HTTPException(status_code=400, detail="Rating must be between 0 and 5")
    
    # Store rating data in the CSV
    write_rating_to_csv(rating)
    return {"message": "Rating added successfully!"}

# Define the Movie model (Request Body)
class Movie(BaseModel):
    imdbId: str
    movie_name: str
    release_year: int
    actor_ids: list[int]
    director_id: int
'''
# Function to get the next available movie_id
def get_next_movie_id():
    try:
        with open('movies.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            rows = list(reader)
            return len(rows)  # assuming movie_id is just the row number (not counting header)
    except FileNotFoundError:
        return 1  # Start from 1 if file doesn't exist
'''
def get_next_movie_id():
    try:
        with open('movies.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            rows = list(reader)
            if len(rows) > 1:  # Ensure there is at least one movie
                return random.randint(250000,10000000)  # Generate a random movie_id
            else:
                return 240000+random.randint(1,100000) # If file is empty, start from 1
    except FileNotFoundError:
        return 239314+random.randint(1,100000)  # Start from 1 if file doesn't exist


    
# Function to append movie data to CSV files
def write_movie_to_csv(movie_data: Movie):
    movie_file_path = 'movies.csv'
    actors_file_path = 'movie_actors.csv'
    director_file_path = 'movie_director.csv'

    # Get next available movie_id
    movie_id = get_next_movie_id()

    # Write to movies.csv
    with open(movie_file_path, mode='a', newline='') as movie_file:
        movie_writer = csv.writer(movie_file)

        # Check if file is empty (no header) to write the header
        file_empty = movie_file.tell() == 0
        if file_empty:
            movie_writer.writerow(['imdbId', 'movie_id', 'movie_name', 'release_year'])  # Write header if file is empty
        
        # Write the movie data
        movie_writer.writerow([movie_data.imdbId, movie_id, movie_data.movie_name, movie_data.release_year])

    # Write to movie_actors.csv (for multiple actors)
    with open(actors_file_path, mode='a', newline='') as actors_file:
        actors_writer = csv.writer(actors_file)

        # Check if file is empty (no header) to write the header
        file_empty = actors_file.tell() == 0
        if file_empty:
            actors_writer.writerow(['movie_id', 'actor_id'])  # Write header if file is empty
        
        # Write the movie-actor relationships
        for actor_id in movie_data.actor_ids:
            actors_writer.writerow([movie_id, actor_id])

    # Write to movie_director.csv (for movie-director relationships)
    with open(director_file_path, mode='a', newline='') as director_file:
        director_writer = csv.writer(director_file)

        # Check if file is empty (no header) to write the header
        file_empty = director_file.tell() == 0
        if file_empty:
            director_writer.writerow(['movie_id', 'director_id'])  # Write header if file is empty
        
        # Write the movie-director relationship
        director_writer.writerow([movie_id, movie_data.director_id])

@app.post("/add-movie/")
async def add_movie(movie: Movie):
    # Validation: Ensure all fields are filled
    if not movie.imdbId or not movie.movie_name or not movie.release_year or not movie.director_id or not movie.actor_ids:
        raise HTTPException(status_code=400, detail="All fields are required for the movie")

    # Store movie and actors data in the CSV files
    write_movie_to_csv(movie)
    return {"message": "Movie added successfully!"}
