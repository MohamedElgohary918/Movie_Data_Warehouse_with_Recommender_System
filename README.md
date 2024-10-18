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


## Future Work
- **Adding User Interaction:** Implement user login and track preferences for collaborative filtering.
- **Improved UI:** Enhance the Streamlit interface for better user experience, with more interactive elements.
- **Deployment Scaling:** Use Azure Kubernetes Service (AKS) for scaling the application to handle higher loads.