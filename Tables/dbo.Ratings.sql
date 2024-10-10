CREATE TABLE Ratings (
  Movie_id INT,
  User_id INT,
  rating FLOAT,
  CONSTRAINT F_Movie FOREIGN KEY (Movie_id) REFERENCES Movies(Movie_id),
  CONSTRAINT FK_User FOREIGN KEY (User_id) REFERENCES Users(User_id)
);
