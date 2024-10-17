from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Movie, Actor, Director, MovieActor, MovieDirector, Rating
from crud import get_movie_by_name, get_actor_by_name, get_director_by_name
from schemas import MovieCreate, Actor as ActorSchema, Director as DirectorSchema, Rating as RatingSchema

app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint to add a movie along with actors and directors
@app.post("/add_movie")
def add_movie(movie: MovieCreate, db: Session = Depends(get_db)):
    # Check if the movie already exists
    db_movie = get_movie_by_name(db, movie.movie_name)
    if db_movie:
        raise HTTPException(status_code=400, detail="Movie already exists")

    # Add new movie
    new_movie = Movie(
        movie_name=movie.movie_name,
        release_year=movie.release_year,
        imdbId=movie.imdbId
    )
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)

    # Check and add actors
    for actor in movie.actors:
        db_actor = get_actor_by_name(db, actor.actor_name)
        if not db_actor:
            new_actor = Actor(actor_name=actor.actor_name)
            db.add(new_actor)
            db.commit()
            db.refresh(new_actor)
            db_actor = new_actor

        # Add the relationship to MovieActor
        new_movie_actor = MovieActor(movie_id=new_movie.movie_id, actor_id=db_actor.actor_id)
        db.add(new_movie_actor)

    # Check and add director
    db_director = get_director_by_name(db, movie.director.director_name)
    if not db_director:
        new_director = Director(director_name=movie.director.director_name)
        db.add(new_director)
        db.commit()
        db.refresh(new_director)
        db_director = new_director

    # Add the relationship to MovieDirector
    new_movie_director = MovieDirector(movie_id=new_movie.movie_id, director_id=db_director.director_id)
    db.add(new_movie_director)

    db.commit()

    return {"message": "Movie added successfully"}

# Endpoint to add a rating for a movie
@app.post("/ratings/")
def add_rating(rating: RatingSchema, db: Session = Depends(get_db)):
    # Check if the movie exists
    db_movie = db.query(Movie).filter(Movie.movie_id == rating.movie_id).first()
    if not db_movie:
        raise HTTPException(status_code=404, detail="Movie not found")

    # Add the rating
    new_rating = Rating(
        movie_id=rating.movie_id,
        user_id=rating.user_id,
        rating=rating.rating
    )
    db.add(new_rating)
    db.commit()
    db.refresh(new_rating)

    return {"message": "Rating added successfully"}

# Endpoint to get ratings for a specific movie
@app.get("/ratings/{movie_id}")
def get_ratings(movie_id: int, db: Session = Depends(get_db)):
    ratings = db.query(Rating).filter(Rating.movie_id == movie_id).all()
    if not ratings:
        raise HTTPException(status_code=404, detail="No ratings found for this movie")
    
    return ratings

# CRUD functions to get movie, actor, and director by name
@app.get("/movies/{movie_name}")
def get_movie_by_name_endpoint(movie_name: str, db: Session = Depends(get_db)):
    db_movie = get_movie_by_name(db, movie_name)
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return db_movie

@app.get("/actors/{actor_name}")
def get_actor_by_name_endpoint(actor_name: str, db: Session = Depends(get_db)):
    db_actor = get_actor_by_name(db, actor_name)
    if db_actor is None:
        raise HTTPException(status_code=404, detail="Actor not found")
    return db_actor

@app.get("/directors/{director_name}")
def get_director_by_name_endpoint(director_name: str, db: Session = Depends(get_db)):
    db_director = get_director_by_name(db, director_name)
    if db_director is None:
        raise HTTPException(status_code=404, detail="Director not found")
    return db_director
