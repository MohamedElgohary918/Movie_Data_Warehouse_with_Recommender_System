CREATE TABLE Actor (
  Actor_id INT IDENTITY(1,1) PRIMARY KEY,
  Actor_name VARCHAR(500)
);

CREATE TABLE MovieActor (
  Movie_id INT,
  Actor_id INT,
  CONSTRAINT FK_Movie FOREIGN KEY (Movie_id) REFERENCES Movies(Movie_id),
  CONSTRAINT FK_Actor FOREIGN KEY (Actor_id) REFERENCES Actor(Actor_id)
);