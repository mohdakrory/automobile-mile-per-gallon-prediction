"""
Prediction Module for Automobile MPG Model
-------------------------------------------
This module loads a trained model and makes predictions on new samples.
"""

from keras.models import load_model
from pickle import load
import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(project_root))

class MPGPredictor:
    def __init__(self, model_path='src/saved_weights//best_model.h5', 
                 scaler_path='src/saved_weights/x_scaler.pkl'):
        """
        Initialize the predictor with model and scaler paths.
        
        Parameters:
        -----------
        model_path : str
            Path to the saved Keras model (.h5 file)
        scaler_path : str
            Path to the saved scaler (.pkl file)
        """
        self.model = load_model(model_path)
        with open(scaler_path, 'rb') as f:
            self.scaler = load(f)
    
    def predict(self, cylinders, displacement, horsepower, weight, 
                acceleration, model_year, origin):
        """
        Make a prediction for a new automobile sample.
        
        Parameters:
        -----------
        cylinders : int
            Number of cylinders (e.g., 4, 6, 8)
        displacement : float
            Engine displacement in cubic inches
        horsepower : float
            Engine horsepower
        weight : float
            Vehicle weight in pounds
        acceleration : float
            Time to accelerate from 0 to 60 mph in seconds
        model_year : int
            Model year (e.g., 70 for 1970, 80 for 1980)
        origin : str
            Origin of the car ('USA', 'Europe', or 'Japan')
        
        Returns:
        --------
        float : Predicted miles per gallon (MPG)
        """
        # Construct the sample array in the correct order
        sample = [cylinders, displacement, horsepower, weight, 
                  acceleration, model_year, origin]
        
        # One-hot encoding for origin
        is_usa = int(sample[-1] == 'USA')
        is_europe = int(sample[-1] == 'Europe')
        
        # Remove origin from sample
        sample = sample[:-1]
        
        # Add one-hot encoded features
        sample.extend([is_usa, is_europe])
        
        # Scale the sample
        sample_scaled = self.scaler.transform([sample])
        
        # Make prediction
        prediction = self.model.predict(sample_scaled, verbose=0)[0][0]
        
        return prediction
    


# if __name__ == "__main__":
#     # Example usage
#     predictor = MPGPredictor()
    
#     # Single prediction
#     mpg = predictor.predict(
#         cylinders=8,
#         displacement=307.0,
#         horsepower=130.0,
#         weight=3504,
#         acceleration=12.0,
#         model_year=70,
#         origin='USA'
#     )
#     print(f"Predicted MPG: {mpg:.2f}")
    
