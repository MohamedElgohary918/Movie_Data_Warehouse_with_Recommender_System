#!/bin/bash

# Set variables
RESOURCE_GROUP="recommendation-app-rg"
SERVER_NAME="ALIEN-DB-SERVER"
DATABASE_NAME="MoveiesDB"
APP_SERVICE_PLAN_NAME="azure-for-students"
WEB_APP_NAME="recommendation-app"

# Create Resource Group
az group create --name $RESOURCE_GROUP --location "East US"

# Create SQL Server
az sql server create --name $SERVER_NAME --resource-group $RESOURCE_GROUP --location "East US" --admin-user yourAdminUser --admin-password yourAdminPassword

# Create SQL Database
az sql db create --resource-group $RESOURCE_GROUP --server $SERVER_NAME --name $DATABASE_NAME --service-objective S0

# Create App Service Plan
az appservice plan create --name $APP_SERVICE_PLAN_NAME --resource-group $RESOURCE_GROUP --sku B1 --is-linux

# Create Web App with Python 3.8
az webapp create --resource-group $RESOURCE_GROUP --plan $APP_SERVICE_PLAN_NAME --name $WEB_APP_NAME --runtime "PYTHON|3.8"

# Configure App Service with environment variables
az webapp config appsettings set --resource-group $RESOURCE_GROUP --name $WEB_APP_NAME --settings \
    MOVIE_DATA_PATH='metadata_with_imdb_metadata.csv' \
    EMBEDDING_MODEL='all-MiniLM-L6-v2' \
    MODEL_PATH='models/' \
    FAISS_INDEX_FILE='faiss_index.bin' \
    EMBEDDINGS_FILE='movie_embeddings.pkl' \
    MLFLOW_TRACKING_URI='http://localhost:5000' \
    MLFLOW_EXPERIMENT_NAME='movie_recommender' \
    MLFLOW_RUN_NAME='faiss_recommender'

# Setup local Git deployment
git init
git add .
git commit -m "Deploying movie recommendation app"

# Set up deployment with Poetry
az webapp deployment source config-local-git --name $WEB_APP_NAME --resource-group $RESOURCE_GROUP

# Create a requirements.txt from poetry.lock (needed for Azure to install dependencies)
poetry export -f requirements.txt --output requirements.txt --without-hashes



echo "Deployment Complete! Access your app at: https://$WEB_APP_NAME.azurewebsites.net"
