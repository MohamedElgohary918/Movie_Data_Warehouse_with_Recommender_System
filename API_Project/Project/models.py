from sqlalchemy import Column,String ,Integer, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

# SQLAlchemy base
Base = declarative_base()

class Movie(Base):
    __tablename__ = "Movies"
    movie_id = Column(Integer, primary_key=True, index=True)
    movie_name = Column(String, nullable=False)
    release_year = Column(Integer)
    imdbId = Column(String, unique=True)

    # Relationships
    actors = relationship("MovieActor", back_populates="movie")
    director = relationship("MovieDirector", back_populates="movie")
    ratings = relationship("Rating", back_populates="movie")

class Actor(Base):
    __tablename__ = "Actors"
    actor_id = Column(Integer, primary_key=True, index=True)
    actor_name = Column(String, nullable=False, unique=True)

class Director(Base):
    __tablename__ = "Directors"
    director_id = Column(Integer, primary_key=True, index=True)
    director_name = Column(String, nullable=False, unique=True)

class MovieActor(Base):
    __tablename__ = "Movie_Actors"
    movie_id = Column(Integer, ForeignKey("Movies.movie_id"), primary_key=True)
    actor_id = Column(Integer, ForeignKey("Actors.actor_id"), primary_key=True)
    
    movie = relationship("Movie", back_populates="actors")
    actor = relationship("Actor")

class MovieDirector(Base):
    __tablename__ = "Movie_Director"
    movie_id = Column(Integer, ForeignKey("Movies.movie_id"), primary_key=True)
    director_id = Column(Integer, ForeignKey("Directors.director_id"), primary_key=True)
    
    movie = relationship("Movie", back_populates="director")
    director = relationship("Director")

class Rating(Base):
    __tablename__ = "Ratings"
    rating_id = Column(Integer, primary_key=True, index=True)
    movie_id = Column(Integer, ForeignKey("Movies.movie_id"))
    user_id = Column(Integer, nullable=False)
    rating = Column(Integer, nullable=False)

    # Relationships
    movie = relationship("Movie", back_populates="ratings")


