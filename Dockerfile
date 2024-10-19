# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies and dependencies for Poetry
RUN apt-get update && apt-get install -y \
    curl \
    && curl -sSL https://install.python-poetry.org | python3 -

# Add Poetry to PATH
ENV PATH="/root/.local/bin:$PATH"

# Copy pyproject.toml and poetry.lock into the container
COPY pyproject.toml ./

# Install dependencies using Poetry
RUN poetry install --only main --no-interaction --no-ansi

RUN poetry add pyodbc sqlalchemy streamlit fastapi uvicorn mlflow
# Copy the current directory contents into the container at /app
COPY . .
# Install system dependencies for ODBC and Microsoft ODBC Driver 17 for SQL Server
RUN apt-get update && apt-get install -y \
    curl \
    apt-transport-https \
    gnupg \
    unixodbc \
    unixodbc-dev \
    libpq-dev \
    && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql17 \
    && rm -rf /var/lib/apt/lists/*

# Streamlit-specific environment variables
ENV STREAMLIT_SERVER_HEADLESS=true
ENV STREAMLIT_SERVER_PORT=8501

# Make the run.sh script executable
RUN chmod 777 run.sh

# Expose the ports for MLflow, Streamlit, and FastAPI
EXPOSE 5000 8501 8000

# Run the app using Streamlit
# CMD ["poetry", "run", "streamlit", "run", "app.py"]
# Use CMD to run the commands directly
# Use CMD to run the commands directly within the Poetry environment
CMD ["sh", "-c", "\
    . $(poetry env info --path)/bin/activate && \
    poetry shell && \
    echo 'Starting MLflow...' && \
    poetry run mlflow ui --host 0.0.0.0 --port 5000 & \
    echo 'Starting Streamlit app...' && \
    poetry run streamlit run app.py & \
    echo 'Starting FastAPI server...' && \
    poetry run uvicorn app:app --host 0.0.0.0 --port 8000 \
"]
