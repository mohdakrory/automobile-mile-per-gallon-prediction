from keras.models import load_model
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error, mean_absolute_percentage_error
import numpy as np
from pickle import load
import json
import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(project_root))

def load_test_data(data_path='data/processed/train_test_data.pkl'):
    """Load test data from pickle file."""
    with open(data_path, 'rb') as file:
        data = load(file)
        x_test = data['x_test']
        y_test = data['y_test']
    return x_test, y_test


def calculate_metrics(y_true, y_pred):
    """Calculate regression metrics."""
    metrics = {
        'mse': float(mean_squared_error(y_true, y_pred)),
        'rmse': float(np.sqrt(mean_squared_error(y_true, y_pred))),
        'mae': float(mean_absolute_error(y_true, y_pred)),
        'mape': float(mean_absolute_percentage_error(y_true, y_pred)),
        'r2': float(r2_score(y_true, y_pred)),
        'test_samples': int(len(y_true))
    }
    return metrics


def save_metrics_to_json(metrics, output_path='results/metrics.json'):
    """Save metrics to JSON file."""
    with open(output_path, 'w') as f:
        json.dump(metrics, f, indent=4)
    print(f"Metrics saved to {output_path}")


def evaluate(model_path='src/saved_weights/best_model.h5', 
             data_path='data/processed/train_test_data.pkl',
             output_path='src/model/training_artifacts/metrics.json'):
    """
    Complete evaluation pipeline: load model, load data, calculate metrics, save to JSON.
    
    Parameters:
    -----------
    model_path : str
        Path to the H5 model file
    data_path : str
        Path to the pickle file with test data
    output_path : str
        Path to save the JSON metrics file
        
    Returns:
    --------
    dict : Dictionary containing all calculated metrics
    """
    # Load model
    model = load_model(model_path)
    
    # Load test data
    x_test, y_test = load_test_data(data_path)
    
    # Make predictions
    y_pred = model.predict(x_test, verbose=0)
    
    # Calculate metrics
    metrics = calculate_metrics(y_test, y_pred)
    
    # Save to JSON
    save_metrics_to_json(metrics, output_path)
    
    # Print metrics
    print("\nEvaluation Results:")
    print(json.dumps(metrics, indent=4))
    return metrics


# # Usage - just call evaluate():
# if __name__ == "__main__":
#     metrics = evaluate()
