from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from keras.models import load_model
from pickle import load
import uvicorn
import asyncio
from concurrent.futures import ThreadPoolExecutor
import logging
import os
import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load model and scaler at startup with error handling
try:
    model_path = 'src/saved_weights/best_model.h5'
    scaler_path = 'src/saved_weights/x_scaler.pkl'
    
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at {model_path}")
    if not os.path.exists(scaler_path):
        raise FileNotFoundError(f"Scaler file not found at {scaler_path}")
    
    model = load_model(model_path)
    with open(scaler_path, 'rb') as f:
        scaler = load(f)
    logger.info("Model and scaler loaded successfully")
except Exception as e:
    logger.error(f"Error loading model or scaler: {str(e)}")
    raise

app = FastAPI()

# Thread pool for running blocking operations
executor = ThreadPoolExecutor(max_workers=10)


class CarFeatures(BaseModel):
    cylinders: int
    displacement: float
    horsepower: float
    weight: float
    acceleration: float
    modelyear: int
    origin: str


def predict_sync(sample_scaled):
    """Synchronous prediction function to run in thread pool."""
    return model.predict(sample_scaled, verbose=0)[0][0]


@app.post("/predict")
async def predict(features: CarFeatures):
    """Predict MPG for a car - async for handling multiple requests."""
    try:
        # Construct sample
        sample = [
            features.cylinders,
            features.displacement,
            features.horsepower,
            features.weight,
            features.acceleration,
            features.modelyear,
            features.origin
        ]
        
        # One-hot encode origin
        is_usa = int(sample[-1] == 'USA')
        is_europe = int(sample[-1] == 'Europe')
        sample = sample[:-1]
        sample.extend([is_usa, is_europe])
        
        # Scale
        sample_scaled = scaler.transform([sample])
        
        # Run prediction in thread pool to avoid blocking
        loop = asyncio.get_event_loop()
        prediction = await loop.run_in_executor(executor, predict_sync, sample_scaled)
        
        logger.info(f"Prediction successful: {prediction}")
        return {"predicted_mpg": float(prediction)}
    
    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run("fast-api:app", host="127.0.0.1", port=8000, reload=True)
