import os 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from pickle import dump
import sys
from pathlib import Path
import yaml

project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

# Load configuration
config_path = project_root / 'config.yaml'
with open(config_path, 'r') as file:
    config = yaml.safe_load(file)


class DataPreprocessor:
    def __init__(self):
        pass

    def preprocess(self, path: str = None, test_size: float = None, random_state: int = 42):
        """Full pipeline: load, clean, split, preprocess."""
        # Use config values if not provided
        if path is None:
            path = str(project_root) + config['raw_data_path']
        if test_size is None:
            test_size = config['train_test_split']
        
        df = self.load_data(path)
        df = self.clean_data(df)

        x = df.drop(columns=['mpg'])
        y = df['mpg'].values

        # one hot encoding of 'origin' column
        x['is_USA'] = (x['origin'] == '1').astype(int)
        x['is_Europe'] = (x['origin'] == '2').astype(int)
        x = x.drop('origin', axis=1)

        y = y.reshape(-1,1)
        x = x.values

        x_train, x_test, y_train, y_test = train_test_split(
            x, y, test_size=test_size, random_state=random_state
        )

        x_scaler = MinMaxScaler()
        x_train[:] = x_scaler.fit_transform(x_train[:])
        x_test[:] = x_scaler.transform(x_test[:])

        # Create directory if it doesn't exist and save scaler
        scaler_dir = str(project_root) + config['saved_weights_path']
        os.makedirs(scaler_dir, exist_ok=True)

        scaler_path = scaler_dir + '/x_scaler.pkl'
        with open(scaler_path, 'wb') as file:
             dump(x_scaler, file)

        # Use config for processed data path
        processed_path = str(project_root) + config['processed_data_path']
        processed_dir = os.path.dirname(processed_path)
        
        os.makedirs(processed_dir, exist_ok=True)
        with open(processed_path, 'wb') as file:
            dump({
                'x_train': x_train,
                'x_test': x_test,
                'y_train': y_train,
                'y_test': y_test
            }, file) 
        print(f"Data successfully processed and saved to {config['processed_data_path']} \ntest size {test_size} \ntest_samples: {len(x_test)} \ntrain_samples: {len(x_train)}")

    def load_data(self, path: str) -> pd.DataFrame:
        """Load dataset from CSV file."""

        return pd.read_csv(path)

    def clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """Clean dataset (handle missing values, fix dtypes)."""
        df = df.drop('car name', axis=1)
        df.drop(df[df['horsepower'] == '?'].index, inplace=True)
        df.horsepower = df.horsepower.astype('float')
        return df


# if __name__ == "__main__":
#     data_path = "data/raw/auto-mpg.csv"
#     preprocessor = DataPreprocessor()
#     preprocessor.preprocess(data_path)
    
