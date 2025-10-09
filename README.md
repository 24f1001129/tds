# Project Repository

This repository contains two distinct projects: a FastAPI service for deployment observability and a telemetry metrics API.

## HF Docker Project

This project is a simple FastAPI service that provides a "Deployment Observability API." It's designed to be run in a Docker container.

### Running the Project

1.  **Build the Docker image:**
    ```bash
    docker build -t deployment-observability-api .
    ```
2.  **Run the Docker container:**
    ```bash
    docker run -p 7473:7473 -e GA2_TOKEN_2918="your-secret-token" deployment-observability-api
    ```

The API will be available at `http://localhost:7473`.

## FastAPI Vercel Project

This project is a FastAPI service designed for deployment on Vercel. It calculates and returns telemetry metrics based on latency data.

### Running the Project Locally

1.  **Navigate to the project directory:**
    ```bash
    cd fastapi-vercel
    ```
2.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the application using Uvicorn:**
    ```bash
    uvicorn app.index:app --reload
    ```

### Deploying to Vercel

The project is configured for Vercel deployment. You can deploy it by connecting your Git repository to Vercel and following the on-screen instructions.

## Conclusion

This repository serves as a container for two independent FastAPI projects, each with a specific purpose and deployment strategy.
