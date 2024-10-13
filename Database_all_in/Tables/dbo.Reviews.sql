CREATE TABLE Reviews (
  Review_id INT IDENTITY(1,1) PRIMARY KEY,
  Movie_id INT,
  review_text VARCHAR(MAX),
  CONSTRAINT key_Movie FOREIGN KEY (Movie_id) REFERENCES Movies(Movie_id)
);  