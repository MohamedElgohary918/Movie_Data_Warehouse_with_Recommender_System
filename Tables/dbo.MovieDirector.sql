CREATE TABLE Directors (
  Director_id INT IDENTITY(1,1) PRIMARY KEY,
  Director_name VARCHAR(500)
);

CREATE TABLE MovieDirector (
  Movie_id INT,
  Director_id INT,
  CONSTRAINT K_Movie FOREIGN KEY (Movie_id) REFERENCES Movies(Movie_id),
  CONSTRAINT FK_Director FOREIGN KEY (Director_id) REFERENCES Directors(Director_id)
);