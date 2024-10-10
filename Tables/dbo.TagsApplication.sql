CREATE TABLE Tags (
  Tag_id INT PRIMARY KEY,
  Tag VARCHAR(1000)
);

CREATE TABLE TagApplication (
  Movie_id INT,
  User_id INT,
  Tag_id INT,
  Score INT,
  CONSTRAINT ke_Movie FOREIGN KEY (Movie_id) REFERENCES Movies(Movie_id),
  CONSTRAINT K_User FOREIGN KEY (User_id) REFERENCES Users(User_id),
  CONSTRAINT FK_Tag FOREIGN KEY (Tag_id) REFERENCES Tags(Tag_id)
);