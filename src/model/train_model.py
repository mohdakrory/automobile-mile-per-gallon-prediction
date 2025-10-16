# train_model.py
import sys
from pathlib import Path
import matplotlib as plt
from contextlib import redirect_stdout
import yaml

# Add project root to sys.path
project_root = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(project_root))

# Load configuration
config_path = project_root / 'config.yaml'
with open(config_path, 'r') as file:
    config = yaml.safe_load(file)

from src.model.build_model import build_model, get_checkpoint
from src.data_preprocessing import DataPreprocessor

def plot_training_curves(history):

    import matplotlib.pyplot as plt

    # Create a figure with 1 row and 2 columns
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))

    # Plot loss
    axes[0].plot(history.history['loss'], label='Training Loss')
    axes[0].plot(history.history['val_loss'], label='Validation Loss')
    axes[0].set_xlabel('Epoch')
    axes[0].set_ylabel('Loss (MSE)')
    axes[0].set_title('Model Loss')
    axes[0].legend()
    axes[0].grid(True)

    # Plot MAE
    axes[1].plot(history.history['mae'], label='Training MAE')
    axes[1].plot(history.history['val_mae'], label='Validation MAE')
    axes[1].set_xlabel('Epoch')
    axes[1].set_ylabel('MAE')
    axes[1].set_title('Model MAE')
    axes[1].legend()
    axes[1].grid(True)

    # Adjust layout to prevent overlap
    plt.tight_layout()

    # Save the figure without displaying it
    plot_path = str(project_root) + config['training_artifacts_path'] + '/training_metrics_plot.png'
    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
    plt.close()


def train(data_path: str = None,
          model_path: str = None,
          epochs: int = None,
          batch_size: int = None):
    """
    Full training pipeline:
    - Preprocess data
    - Build model
    - Train and save best model

    Parameters
    ----------
    data_path : str
        Path to dataset CSV.
    model_path : str
        Path to save the best trained model.
    epochs : int
        Number of training epochs.
    batch_size : int
        Batch size for training.

    Returns
    -------
    history : keras.callbacks.History
        Training history object.
    """
    
    # Use config values if not provided
    if data_path is None:
        data_path = str(project_root) + config['processed_data_path']
    if model_path is None:
        model_path = str(project_root) + config['saved_weights_path'] + '/best_model.h5'
    if epochs is None:
        epochs = config['epochs']
    if batch_size is None:
        batch_size = config['batch_size']

    # 1. Preprocess data
    from pickle import load

    # Load the train/test data
    with open(data_path, 'rb') as file:
        data = load(file)
        x_train = data['x_train']
        x_test = data['x_test']
        y_train = data['y_train']
        y_test = data['y_test']

    # 2. Build model
    model = build_model(input_dim=x_train.shape[1])
    checkpoint = get_checkpoint(model_path)

    log_path = str(project_root) + config['training_artifacts_path'] + '/training_log.txt'
    with open(log_path, 'w') as log_file:
        with redirect_stdout(log_file):
            # 3. Train model
            history = model.fit(
                x_train,
                y_train,
                epochs=epochs,
                batch_size=batch_size,
                validation_data=(x_test, y_test),
                callbacks=[checkpoint],
                verbose=1
            )
    
    plot_training_curves(history)
    print(f'Training artifacts saved to {config["training_artifacts_path"]}')
    return history


# if __name__ == "__main__":
#     # Example usage
#     data_path = "data/raw/auto-mpg.csv"
#     train(data_path)
