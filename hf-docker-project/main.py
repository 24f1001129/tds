from fastapi import FastAPI
import os

app = FastAPI()

# Read the secret token from environment variables
# This demonstrates how to access secrets set in the Space settings
secret_token = os.getenv("GA2_TOKEN_2918", "Token not found")

@app.get("/")
def read_root():
    return {
        "message": "Deployment observability API is running.",
        "secret_status": "Token loaded successfully" if secret_token != "Token not found" else "Token not loaded"
    }