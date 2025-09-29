import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import os

# --- 1. Setup and Data Loading ---

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)

# Construct a path to the data file relative to this script
# This is a robust way to make sure Vercel finds the file
data_path = os.path.join(os.path.dirname(__file__), 'q-vercel-latency.json')
df = pd.read_json(data_path)


# --- 2. Define the Request Body Model ---

class RequestModel(BaseModel):
    regions: List[str]
    threshold_ms: int


# --- 3. Create the API Endpoint ---

@app.post("/api") # Using /api as the endpoint path
async def get_telemetry_metrics(request: RequestModel):
    response_data = {}
    
    for region in request.regions:
        region_df = df[df['region'] == region]

        if region_df.empty:
            continue

        avg_latency = region_df['latency_ms'].mean()
        p95_latency = region_df['latency_ms'].quantile(0.95)
        avg_uptime = region_df['uptime_pct'].mean()
        breaches = int((region_df['latency_ms'] > request.threshold_ms).sum())
        
        response_data[region] = {
            "avg_latency": float(avg_latency),
            "p95_latency": float(p95_latency),
            "avg_uptime": float(avg_uptime),
            "breaches": breaches
        }

    return response_data