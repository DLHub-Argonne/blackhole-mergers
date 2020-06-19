from tensorflow import keras
import tensorflow as tf
import numpy as np

# Location for the global variables
#  Large objects that I only want to load into memory once!
model = None

def _load_model():
    global model
    if model is None:
        model = keras.models.load_model('model_19-0.00.h5')


def inference(waveforms) -> dict:
    """Perform inference on the model

    Args:
        waveforms (array): Input waveforms
    Returns:
        (dict) Parameter estimated from the waveform
            - q: Mass ratio
            - s1: Spin of primary
            - s2: Spin of secondary
            - S_eff: Effective spin
            - chi: Effective spin parameter 
    """
    _load_model()

    # Convert the inputs into numpy arrays (if they are not already
    inputs = np.array(waveforms)

    # Run through the model
    preds = model.predict(inputs)
    preds = np.hstack(preds)

    # Assign labels before outputing data
    output = dict((k, v.tolist()) for k, v in zip(['q', 's1', 's2', 'chi', 'S_eff'], preds.T))
    return output

if __name__ == "__main__":

    # Make data
    _load_model()
    shape = list(model.input_shape)
    shape[0] = 5
    waveforms = np.zeros(shape)

    # Run
    print(inference(waveforms))
