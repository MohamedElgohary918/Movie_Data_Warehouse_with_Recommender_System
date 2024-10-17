from sqlalchemy.orm import Session
from models import Movie, Actor, Director

# Check if a movie exists by name
def get_movie_by_name(db: Session, movie_name: str):
    return db.query(Movie).filter(Movie.movie_name == movie_name).first()

# Check if an actor exists by name
def get_actor_by_name(db: Session, actor_name: str):
    return db.query(Actor).filter(Actor.actor_name == actor_name).first()

# Check if a director exists by name
def get_director_by_name(db: Session, director_name: str):
    return db.query(Director).filter(Director.director_name == director_name).first()
