from pydantic import BaseModel, Field
from typing import List, Optional

class Actor(BaseModel):
    actor_name: str = Field(..., example="Robert Downey Jr.")

class Director(BaseModel):
    director_name: str = Field(..., example="Christopher Nolan")

class MovieCreate(BaseModel):
    movie_name: str = Field(..., example="Inception")
    release_year: int = Field(..., example=2010)
    actors: List[Actor]
    director: Director

class Rating(BaseModel):
    movie_id: int
    user_id: int
    rating: int = Field(..., ge=1, le=5, example=4)  # Ensures the rating is between 1 and 5
