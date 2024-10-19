## Overview

This project contains two key Python scripts designed for handling a movie rating and database system. These scripts manage the backend of a FastAPI-based application, handle CSV data storage for movies and ratings, and allow interaction with a SQL Server database for persistent data storage. 


### Adding a New Movie
The following image illustrates the interface for adding a new movie.
![Adding a new movie](Imgs/lm.jpeg)

### Adding a New Movie Rating
The following image shows the interface for adding a new movie rating.
![Adding a new movie rating](Imgs/lm2.jpeg)

Below is a brief description of the key components and functionality of each file:


### 1. `main.py`
This script defines a FastAPI application to handle movie and rating data. It includes the following key features:

- **FastAPI Application**: The API is structured with CORS middleware to allow cross-origin requests.

### 2. `models.py`
This script manages the connection to a SQL Server database and handles the migration of data from CSV files to the SQL Server. 

It reads movie, actor, director, and rating data from CSV files and inserts them into corresponding database tables.


#### Data Insertion:
- **`to_sql()` Method**: The Pandas DataFrames are inserted into the database using the `to_sql()` method, appending new data to the `movies`, `movie_actors`, `movie_director`, and `ratings` tables.

#### Truncation Operation:
- **Truncation** (commented out): There is an option to clear all data from the CSV files while keeping the column headers intact by saving empty DataFrames back to the CSV files.

---

## Usage Instructions

1. **Run the FastAPI server**:
   ```bash
   uvicorn API_Project.Project.main:app --reload
   ```
   - Use `/add-rating/` to submit a rating.
   - Use `/add-movie/` to add a new movie, along with associated actors and the director.

2. **Data Migration to SQL Server**:
   - Run `models.py` to read data from the CSV files and load them into the SQL Server database.
   - Ensure the connection to the database is properly configured in the `connection_string` variable.

