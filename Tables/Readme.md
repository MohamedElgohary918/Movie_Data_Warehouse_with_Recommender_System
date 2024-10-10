# Movie Database schema 

This project contains a set of tables about movies

## Tables 

1. **Users**  
   Contains users ids. Create this table first.

2. **Movies**  
   Stores information about movies. Should be created after the Users table.

3. **Ratings**  
   contains ratings for movies. Depends on the Movies and Users tables.

4. **Reviews**  
   Contains user reviews for movies. Depends on the Movies table.

5. **Tags**  
   Stores tags for categorizing movies.

6. **TagsApplications**  
   Links movies, users, and tags with a score for each application.

7. **Actors**  
   Contains basic information about actors. Must be created before the MovieActors table.

8. **MovieActors**  
   Links movies to actors. Depends on the Movies and Actors tables.

9. **Directors**  
   Contains information about directors. Must be created before the MovieDirector table.

10. **MovieDirector**  
    Links movies to directors. Depends on the Movies and Directors tables.

### How to Create the Tables

Run the following files in this order:

1. `Users.sql`
2. `Movies.sql`
3. `Ratings.sql`
4. `Reviews.sql`
5. `Tags.sql`
6. `TagsApplications.sql`
7. `Actors.sql`
8. `MovieActors.sql`
9. `Directors.sql`
10. `MovieDirector.sql`




