# model_builder.py

from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import ModelCheckpoint
from keras.utils import plot_model


def build_model(input_dim: int = 8) -> Sequential:
    """
    Build and compile a Sequential Keras model for regression.
    
    Parameters
    ----------
    input_dim : int
        Number of input features.
    
    Returns
    -------
    model : keras.models.Sequential
        Compiled Keras model.
    """
    model = Sequential([
        Dense(64, input_dim=input_dim, activation='linear'),
        Dense(64, activation='linear'),
        Dense(1)  # regression output
    ])

    model.compile(
        loss='mse',
        optimizer='adam',
        metrics=['mae']
    )

    # plot_model(
    #     model,
    #     to_file="model.jpg",
    #     show_shapes=True,
    #     show_dtype=False,
    #     show_layer_names=False,
    #     rankdir="TB",
    #     expand_nested=False,
    #     dpi=500
    # )
    return model


def get_checkpoint(filepath: str = None) -> ModelCheckpoint:
    """
    Create a ModelCheckpoint callback to save the best model.
    
    Parameters
    ----------
    filepath : str
        Path where the best model will be saved.
    
    Returns
    -------
    checkpoint : keras.callbacks.ModelCheckpoint
        Configured checkpoint callback.
    """
    checkpoint = ModelCheckpoint(
        filepath=filepath,
        save_weights_only=False,
        monitor='val_loss',
        mode='min',
        save_best_only=True,
        verbose=1
    )
    return checkpoint


# if __name__ == "__main__":
#     # Example usage
#     model = build_model(input_dim=8)
#     checkpoint = get_checkpoint("src/saved_models/best_model.h5")
#     model.summary()
