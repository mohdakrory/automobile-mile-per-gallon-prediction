# Automobile Miles Per Gallon (MPG) Prediction

<img width="8000" height="3137" alt="car" src="https://github.com/user-attachments/assets/22dee727-b9a6-437b-9a85-e383436aa7b1" />

## Introduction

This project implements a deep learning solution for predicting the fuel efficiency (miles per gallon) of automobiles based on various vehicle characteristics. The model uses a neural network built with Keras/TensorFlow to predict MPG values from features such as number of cylinders, engine displacement, horsepower, weight, acceleration, model year, and country of origin.

The project provides multiple interfaces for interaction:
- **Command-Line Interface (CLI)** for data processing, training, evaluation, and prediction
- **REST API** for real-time predictions via HTTP requests
- **Python Module** for programmatic integration

## Features

- **Data Preprocessing**: Handles missing values, one-hot encoding, and feature scaling
- **Model Training**: Automatic checkpoint saving for best model
- **Model Evaluation**: Comprehensive metrics (MSE, RMSE, MAE, MAPE, R²)
- **CLI Interface**: Easy-to-use command-line tools for all operations
- **REST API**: Production-ready FastAPI server with async support
- **Logging**: Comprehensive logging for debugging and monitoring
- **Visualization**: Training curves and performance plots

## Project Structure

```
Automobile mile per gallon prediction
├─ api
│  ├─ fast-api.py
│  └─ __init__.py
├─ car.png
├─ cli
│  ├─ project_cli.py
│  └─ __init__.py
├─ data
│  ├─ processed
│  │  └─ train_test_data.pkl
│  └─ raw
│     └─ auto-mpg.csv
├─ data_description_visualization.md
├─ LICENSE
├─ notebooks
│  ├─ automobile-mile-per-gallon-prediction.ipynb
│  ├─ best_model.h5
│  ├─ Data description and visualization
│  │  ├─ categorical_combined (1).png
│  │  ├─ categories_bar_plots.png
│  │  ├─ categories_box_plots .png
│  │  ├─ categories_violin_plots.png
│  │  ├─ continous_combined.png
│  │  ├─ continous_density_plot.png
│  │  ├─ continous_hist_kde_plot.png
│  │  ├─ continous_hist_plot (1).png
│  │  ├─ corr_heatmap.png
│  │  ├─ description of numeric features.csv
│  │  ├─ pair_plot.png
│  │  └─ variable information.png
│  ├─ framework diagram
│  │  ├─ framework diagram.drawio
│  │  └─ framework diagram.png
│  ├─ model.jpg
│  ├─ profile_report.html
│  ├─ Train-Validation_Curves.png
│  └─ x_scaler.pkl
├─ README.md
├─ requirements.txt
└─ src
   ├─ data_preprocessing.py
   ├─ model
   │  ├─ build_model.py
   │  ├─ evaluate_model.py
   │  ├─ predict.py
   │  ├─ training_artifacts
   │  │  ├─ metrics.json
   │  │  ├─ training_log.txt
   │  │  └─ training_metrics_plot.png
   │  ├─ train_model.py
   │  └─ __init__.py
   ├─ saved_weights
   │  ├─ best_model.h5
   │  └─ x_scaler.pkl
   └─ __init__.py

```

## Installation Guide

### Prerequisites
- Python 3.9 or higher
- pip package manager

### Setup Instructions

1. **Clone or download the project**
   ```powershell
   git clone https://github.com/mohdakrory/automobile-mile-per-gallon-prediction.git
   ```

2. **Create a virtual environment (recommended)**
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. **Install required dependencies**
  Install from requirements file:
   ```powershell
   pip install -r requirements.txt
   ```

## Usage Using CLI

The project provides a comprehensive command-line interface through `project_cli.py` for all major operations.

### 1. Data Processing

Preprocess the raw data, split into train/test sets, and save for training:

```powershell
python cli/project_cli.py --task process_data --test_size 0.2
```

**Parameters:**
- `--task`: Set to `process_data`
- `--test_size`: Fraction of data to use for testing (e.g., 0.2 for 20%)

**Output:**
- Saves preprocessed data to `data/processed/train_test_data.pkl`
- Saves feature scaler to `src/saved_weights/x_scaler.pkl`

### 2. Model Training

Train the neural network model:

```powershell
python cli/project_cli.py --task train --batch_size 32 --epochs 150
```

**Parameters:**
- `--task`: Set to `train`
- `--batch_size`: Number of samples per training batch (default: 32)
- `--epochs`: Number of training epochs (default: 150)

**Output:**
- Saves best model to `src/saved_weights/best_model.h5`
- Saves training log to `src/model/training_artifacts/training_log.txt`
- Saves training curves plot to `src/model/training_artifacts/training_metrics_plot.png`

### 3. Model Evaluation

Evaluate the trained model on test data:

```powershell
python cli/project_cli.py --task evaluate
```

**Parameters:**
- `--task`: Set to `evaluate`

**Output:**
- Displays metrics: MSE, RMSE, MAE, MAPE, R²
- Saves metrics to `src/model/training_artifacts/metrics.json`

### 4. Making Predictions

Predict MPG for a specific automobile:

```powershell
python cli/project_cli.py --task predict --cylinders 8 --displacement 307.0 --horsepower 130.0 --weight 3504 --acceleration 12.0 --model_year 70 --origin USA
```

**Parameters:**
- `--task`: Set to `predict`
- `--cylinders`: Number of cylinders (e.g., 4, 6, 8)
- `--displacement`: Engine displacement in cubic inches
- `--horsepower`: Engine horsepower
- `--weight`: Vehicle weight in pounds
- `--acceleration`: Time to accelerate from 0 to 60 mph (seconds)
- `--model_year`: Model year (e.g., 70 for 1970, 82 for 1982)
- `--origin`: Country of origin (choices: USA, Europe, Japan)

**Output:**
- Displays predicted MPG value

**Example:**
```powershell
python cli/project_cli.py --task predict --cylinders 8 --displacement 307.0 --horsepower 130.0 --weight 3504 --acceleration 12.0 --model_year 70 --origin USA
```

## How to Invoke the API

The project includes a FastAPI-based REST API for real-time predictions.

### Starting the API Server

```powershell
python api/fast-api.py
```

Or using uvicorn directly:
```powershell
uvicorn api.fast-api:app --host 127.0.0.1 --port 8000 --reload
```

The API will be available at: `http://127.0.0.1:8000`

### API Documentation

Once the server is running, access the interactive API documentation at:
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

### Making Predictions via API

#### Using cURL (PowerShell)

```powershell
curl -X POST "http://127.0.0.1:8000/predict" `
  -H "Content-Type: application/json" `
  -d '{
    "cylinders": 8,
    "displacement": 307.0,
    "horsepower": 130.0,
    "weight": 3504.0,
    "acceleration": 12.0,
    "modelyear": 70,
    "origin": "USA"
  }'
```

#### Using Python requests

```python
import requests
import json

url = "http://127.0.0.1:8000/predict"

# Sample car data
car_data = {
    "cylinders": 8,
    "displacement": 307.0,
    "horsepower": 130.0,
    "weight": 3504.0,
    "acceleration": 12.0,
    "modelyear": 70,
    "origin": "USA"
}

response = requests.post(url, json=car_data)
result = response.json()

print(f"Predicted MPG: {result['predicted_mpg']:.2f}")
```

#### Using PowerShell Invoke-RestMethod

```powershell
$body = @{
    cylinders = 8
    displacement = 307.0
    horsepower = 130.0
    weight = 3504.0
    acceleration = 12.0
    modelyear = 70
    origin = "USA"
} | ConvertTo-Json

$response = Invoke-RestMethod -Uri "http://127.0.0.1:8000/predict" -Method Post -Body $body -ContentType "application/json"
Write-Host "Predicted MPG: $($response.predicted_mpg)"
```

### Sample Input Examples

#### Economy Car (European Origin)
```json
{
  "cylinders": 4,
  "displacement": 97.0,
  "horsepower": 88.0,
  "weight": 2130.0,
  "acceleration": 14.5,
  "modelyear": 80,
  "origin": "Europe"
}
```
Expected: High MPG (~30-40)

#### Mid-Size Sedan (Japanese Origin)
```json
{
  "cylinders": 4,
  "displacement": 120.0,
  "horsepower": 97.0,
  "weight": 2489.0,
  "acceleration": 15.0,
  "modelyear": 74,
  "origin": "Japan"
}
```
Expected: Moderate MPG (~25-30)

#### Large American Sedan (USA Origin)
```json
{
  "cylinders": 8,
  "displacement": 400.0,
  "horsepower": 175.0,
  "weight": 4464.0,
  "acceleration": 11.5,
  "modelyear": 71,
  "origin": "USA"
}
```
Expected: Low MPG (~12-18)

### API Response Format

**Success Response:**
```json
{
  "predicted_mpg": 18.45
}
```

**Error Response:**
```json
{
  "detail": "Error message describing what went wrong"
}
```

## Model Architecture

The neural network consists of:
- Input layer: 8 features (cylinders, displacement, horsepower, weight, acceleration, model_year, is_USA, is_Europe)
- Hidden layer 1: 64 neurons with linear activation
- Hidden layer 2: 64 neurons with linear activation
- Output layer: 1 neuron (MPG prediction)

**Optimizer:** Adam  
**Loss Function:** Mean Squared Error (MSE)  
**Metrics:** Mean Absolute Error (MAE)

![model](https://github.com/user-attachments/assets/28586d6c-454e-4d19-a7f3-813922ca9c1a)

## License

MIT License



