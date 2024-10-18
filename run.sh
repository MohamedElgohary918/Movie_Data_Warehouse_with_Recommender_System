#!/bin/bash

# Start MLflow
echo "Starting MLflow..."
mlflow ui --host 0.0.0.0 --port 5000 &

# Start Streamlit
echo "Starting Streamlit app..."
streamlit run app.py &

# Start FastAPI with Uvicorn
echo "Starting FastAPI server..."
uvicorn app:app --host 0.0.0.0 --port 8000