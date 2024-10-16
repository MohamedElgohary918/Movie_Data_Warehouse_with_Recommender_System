# import streamlit as st
# from recommender import MovieRecommender

# # Initialize the MovieRecommender
# recommender = MovieRecommender('metadata_with_imdb_metadata.csv')

# # Streamlit app title
# st.title("Movie Recommendation System")

# # Button to train the model
# if st.button("Train Model"):
#     with st.spinner("Training model..."):
#         recommender.train_model()  # Train the model
#     st.success("Model trained successfully!")

# # Movie selection by user
# movie_choice = st.selectbox("Choose a movie", recommender.movies['title'])


# # Button to get recommendations
# if st.button("Get Recommendations"):
#     # Show recommendations when a movie is selected
#     if movie_choice:
#         recommendations = recommender.get_recommendations(movie_choice)
#         st.write(f"Movies similar to: {movie_choice}")

#         # Split the recommendations into chunks to create a carousel-like effect
#         chunk_size = 5  # Number of movies per row
#         for i in range(0, len(recommendations), chunk_size):
#             row_movies = recommendations.iloc[i:i + chunk_size]  # Get the current chunk of movies

#             # Create a row of movie posters
#             cols = st.columns(chunk_size)  # Create columns for each movie in the row
#             for col, (_, movie) in zip(cols, row_movies.iterrows()):
#                 with col:
#                     st.image(movie['cover_url_better'], caption=movie['title'])
#                     # st.write(f"Genres: {movie['genres']}")
#                     # st.write(f"Rating: {movie['total_rating']}")
#     else:
#         st.warning("Please select a movie first!")




# # # Button to get recommendations
# # if st.button("Get Recommendations"):
# #     # Show recommendations when a movie is selected
# #     if movie_choice:
# #         recommendations = recommender.get_recommendations(movie_choice, top_n=10)
# #         st.write("Movies similar to:", movie_choice)
# #         # st.dataframe(recommendations)

# #         # Optionally display movie posters (if available in your dataset)
# #         for _, movie in recommendations.iterrows():
# #             st.image(movie['cover_url_better'], width=150, caption=movie['title'])
# #     else:
# #         st.warning("Please select a movie first!")

import streamlit as st
from recommenders.model_interface import RecommenderFactory
from config.base_config import BASE_CONFIG


# Initialize Recommender
recommender = RecommenderFactory.get_recommender(BASE_CONFIG['recommender_type'], BASE_CONFIG)

# Streamlit app title
st.title("Movie Recommendation System")

# Train model
if st.button("Train Model"):
    with st.spinner("Training model..."):
        recommender.train_model()
    st.success("Model trained successfully!")

# Get movie recommendations
movie_choice = st.selectbox("Choose a movie", recommender.movies['title'])
# Button to get recommendations
if st.button("Get Recommendations"):
    # Show recommendations when a movie is selected
    if movie_choice:
        recommendations = recommender.get_recommendations(movie_choice)
        st.write(f"Movies similar to: {movie_choice}")

        # Split the recommendations into chunks to create a carousel-like effect
        chunk_size = 5  # Number of movies per row
        for i in range(0, len(recommendations), chunk_size):
            row_movies = recommendations.iloc[i:i + chunk_size]  # Get the current chunk of movies

            # Create a row of movie posters
            cols = st.columns(chunk_size)  # Create columns for each movie in the row
            for col, (_, movie) in zip(cols, row_movies.iterrows()):
                with col:
                    st.image(movie['cover_url_better'], caption=movie['title'])
                    # st.write(f"Genres: {movie['genres']}")
                    # st.write(f"Rating: {movie['total_rating']}")
    else:
        st.warning("Please select a movie first!")
