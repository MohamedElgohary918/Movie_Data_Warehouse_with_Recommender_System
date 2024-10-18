# Movies-DEPI-Grad-Project
Movies-DEPI-Grad-Project
![Movie Recommender](https://i.ibb.co/2j6d1Tw/Screenshot-2024-10-18-114330.png)  


## Table of Contents
- [Overview](#overview)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [MLFlow Integration](#mlflow-integration)
- [Deployment](#deployment)
  - [Azure Deployment](#option-1-azure-deployment)
  - [Docker Deployment](#option-2-docker-deployment)
- [Techniques and Potential Enhancements](#techniques-and-potential-enhancements)
- [Future Work](#future-work)

## Overview
This project is a **Movie Recommendation System** that leverages a content-based filtering approach. It uses **Sentence Transformers** for generating movie embeddings based on metadata like title, genres, starring, and directors. The system indexes these embeddings using **Faiss** for fast similarity searches, providing users with movie recommendations. The project is integrated with **MLflow** for experiment tracking and versioning and is designed for deployment using **Azure App Services** or Docker containers.

## Technologies Used
The following technologies were used to build this project:
- **Python 3.8**
- **Sentence Transformers** for generating embeddings
- **Faiss** for similarity search
- **MLflow** for model tracking and experiment logging
- **Streamlit** for building the user interface
- **SQLAlchemy** for database interaction with SQL Server
- **Azure App Services** for deployment (or Docker for containerization)
- **Poetry** for dependency management


## Installation
1. Clone the Repository:
```bash
git clone https://github.com/your-repo/movie-recommender.git
cd movie-recommender
```
2. Install Dependencies: This project uses Poetry for dependency management. Install it if you don’t have it already:
```sh
curl -sSL https://install.python-poetry.org | python3 -
poetry install
```
3. Set Up Environment Variables: Create a .env file in the root directory and add the following variables:
```makefile
MOVIE_DATA_PATH=metadata_with_imdb_metadata.csv
EMBEDDING_MODEL=all-MiniLM-L6-v2
MODEL_PATH=models/
FAISS_INDEX_FILE=faiss_index.bin
EMBEDDINGS_FILE=movie_embeddings.pkl
MLFLOW_TRACKING_URI=http://localhost:5000
MLFLOW_EXPERIMENT_NAME=movie_recommender
MLFLOW_RUN_NAME=faiss_recommender
```

## Running the Application
1. Train the Model: Train the model by running the Streamlit app:
```sh
poetry run streamlit run app.py
```

2. Interact with the App: Open http://localhost:8501 in your browser to interact with the app. You can select a movie and get recommendations based on its metadata.

## MLFlow Integration
MLFlow Integration
The project is fully integrated with MLflow for tracking experiments. All model training sessions and related metrics are logged automatically.

1. Run MLFlow Server:
```sh
mlflow ui
```
2. Track Model Versions: After training the model, logs will be saved in the mlruns folder and can be accessed through the MLflow UI.


## Deployment

### Option 1: Azure Deployment
1. Set up Azure CLI:
Ensure that you have the [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli) installed.
2. Deploy using the following script:
```sh
#!/bin/bash
RESOURCE_GROUP="your-resource-group"
SERVER_NAME="your-server-name"
DATABASE_NAME="your-database-name"
APP_SERVICE_PLAN_NAME="your-app-service-plan-name"
WEB_APP_NAME="your-web-app-name"

az group create --name $RESOURCE_GROUP --location "East US"
az sql server create --name $SERVER_NAME --resource-group $RESOURCE_GROUP --location "East US" --admin-user yourAdminUser --admin-password yourAdminPassword
az sql db create --resource-group $RESOURCE_GROUP --server $SERVER_NAME --name $DATABASE_NAME --service-objective S0
az appservice plan create --name $APP_SERVICE_PLAN_NAME --resource-group $RESOURCE_GROUP --sku B1 --is-linux
az webapp create --resource-group $RESOURCE_GROUP --plan $APP_SERVICE_PLAN_NAME --name $WEB_APP_NAME --runtime "PYTHON|3.8"
```


### Option 2: Docker Deployment
1. Build the Docker image:
```sh
docker build -t movie-recommender-app .
```
2. Run the Docker container:
```sh
docker run -p 8501:8501 movie-recommender-app
```

## Techniques and Potential Enhancements

This project currently uses a **content-based filtering** technique with **Faiss** for similarity search and **SentenceTransformers** for embedding movie metadata into a numerical format. There are several other recommendation techniques that could be explored, each with its own advantages and drawbacks:

### 1. Collaborative Filtering
Collaborative filtering recommends items based on user behavior and preferences. It uses either user-item interaction matrices or item-based collaborative filtering.

- **Advantages**:
  - Works well when there is rich user interaction data.
  - No need for feature engineering based on the item’s metadata.

- **Drawbacks**:
  - **Cold Start Problem**: It struggles with recommending items to new users or recommending new items since no interaction history exists.
  - **Sparsity**: In large systems, the interaction matrix can be very sparse, leading to poor recommendations.
  - Does not consider the content of items (e.g., movie metadata).

### 2. Matrix Factorization (SVD or ALS)
This is a popular technique for collaborative filtering that decomposes the user-item interaction matrix into low-dimensional latent factors. **SVD (Singular Value Decomposition)** and **ALS (Alternating Least Squares)** are common approaches.

- **Advantages**:
  - Efficient with large datasets.
  - Captures hidden structures between users and items.

- **Drawbacks**:
  - Requires regular retraining as new interactions are introduced.
  - Struggles with cold-start problems similar to collaborative filtering.

### 3. Hybrid Systems
Combines collaborative filtering and content-based filtering to get the best of both worlds.

- **Advantages**:
  - Can alleviate the cold-start problem by combining user preferences with metadata.
  - More flexible as it utilizes both behavioral and content-based data.

- **Drawbacks**:
  - Complex to implement and requires more computation.
  - Requires proper balancing between the two approaches.

### 4. Deep Learning-Based Recommendation Systems
Using techniques like **autoencoders**, **neural collaborative filtering (NCF)**, or **convolutional neural networks (CNNs)**, this approach leverages deep neural networks to generate recommendations.

- **Advantages**:
  - Can model complex user-item interactions and nonlinear relationships.
  - Highly flexible in terms of integrating side information (e.g., user demographics or movie metadata).

- **Drawbacks**:
  - Requires extensive computational resources and tuning.
  - Requires large datasets to perform well.
  - Hard to interpret the models and recommendations.

### 5. Knowledge Graph-Based Recommendations
Utilizes a **knowledge graph** where relationships between users, items, genres, and actors are explicitly modeled to make recommendations based on the graph structure.

- **Advantages**:
  - Provides more explainable recommendations.
  - Can incorporate many diverse types of information (e.g., genre, actors, directors).

- **Drawbacks**:
  - Complex and requires significant setup.
  - Performance can degrade if the graph becomes too large or dense.

>### Conclusion

>>The **Movie Recommendation System** implemented in this project is a content-based system leveraging **SentenceTransformers** and **Faiss** for fast similarity searches. While this approach works well for this application, future enhancements could include experimenting with **collaborative filtering**, **hybrid systems**, and **deep learning-based techniques** to improve recommendation accuracy and user satisfaction.

## Future Work
- **Adding User Interaction:** Implement user login and track preferences for collaborative filtering.
- **Improved UI:** Enhance the Streamlit interface for better user experience, with more interactive elements.
- **Deployment Scaling:** Use Azure Kubernetes Service (AKS) for scaling the application to handle higher loads.