import argparse
import sys
from pathlib import Path
import yaml

project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

# Load configuration
config_path = project_root / 'config.yaml'
with open(config_path, 'r') as file:
    config = yaml.safe_load(file)

parser = argparse.ArgumentParser(description="Main code for processing data, building, training, and evaluating a model for automobile mile per galon prediction")

# Main task argument
parser.add_argument('--task', type=str, required=True, 
                    choices=['process_data', 'train', 'evaluate', 'predict'],
                    help='Specify a task in the pipeline. Options: process_data, train, evaluate, predict')

# Data processing arguments
parser.add_argument('--test_size', type=float, required=False,
                    help='The percentage of test data for data splitting, from 0.0 to 1.0 (required for process_data task)')

# Training arguments
parser.add_argument('--batch_size', type=int, required=False,
                    help='Batch size for training the model (required for train task)')

parser.add_argument('--epochs', type=int, required=False,
                    help='Number of training epochs (required for train task)')

# Prediction arguments
parser.add_argument('--cylinders', type=int, required=False,
                    help='Number of cylinders (required for predict task)')

parser.add_argument('--displacement', type=float, required=False,
                    help='Engine displacement in cubic inches (required for predict task)')

parser.add_argument('--horsepower', type=float, required=False,
                    help='Engine horsepower (required for predict task)')

parser.add_argument('--weight', type=float, required=False,
                    help='Vehicle weight in pounds (required for predict task)')

parser.add_argument('--acceleration', type=float, required=False,
                    help='Time to accelerate from 0 to 60 mph in seconds (required for predict task)')

parser.add_argument('--model_year', type=int, required=False,
                    help='Model year, e.g., 70 for 1970 (required for predict task)')

parser.add_argument('--origin', type=str, required=False, choices=['USA', 'Europe', 'Japan'],
                    help='Origin of the car: USA, Europe, or Japan (required for predict task)')


args = parser.parse_args()
task = args.task


if task == 'process_data':
    from src.data_preprocessing import DataPreprocessor
    preprocessor = DataPreprocessor()
    preprocessor.preprocess(test_size = args.test_size)

elif task == 'train':
    from src.model.train_model import train
    train(epochs=args.epochs, batch_size=args.batch_size)

elif task == 'evaluate':
    from src.model.evaluate_model import evaluate
    evaluate()

elif task == 'predict':
    required_predict_args = ['cylinders', 'displacement', 'horsepower', 'weight', 
                             'acceleration', 'model_year', 'origin']
    missing_args = [arg for arg in required_predict_args if getattr(args, arg) is None]
    
    if missing_args:
        parser.error(f"The following arguments are required for 'predict' task: {', '.join(['--' + arg for arg in missing_args])}")
    
    from src.model.predict import MPGPredictor
    
    # Construct paths from config
    model_path = str(project_root) + config['saved_weights_path'] + '/best_model.h5'
    scaler_path = str(project_root) + config['saved_weights_path'] + '/x_scaler.pkl'
    
    predictor = MPGPredictor(
        model_path=model_path,
        scaler_path=scaler_path
    )
    
    mpg = predictor.predict(
        cylinders=args.cylinders,
        displacement=args.displacement,
        horsepower=args.horsepower,
        weight=args.weight,
        acceleration=args.acceleration,
        model_year=args.model_year,
        origin=args.origin
    )
    
    print(f"\nPredicted MPG: {mpg:.2f}")
    


