import os

from keras import backend as K
from keras.models import model_from_json
import numpy as np


def predict(shader_values):
    K.clear_session()

    json_path = os.path.join(os.path.dirname(__file__), 'cnn_architecture.json')
    with open(json_path, 'r') as json_file:
        json_model = json_file.read()

    model = model_from_json(json_model)
    weights_path = os.path.join(os.path.dirname(__file__), 'cnn_weights.h5')
    model.load_weights(weights_path)
    model.compile(loss='mse', optimizer='adam', metrics=['mse'])

    x = _process_shader_values(shader_values)
    predicted = model.predict(x)
    return predicted


def _process_shader_values(shader_values):
    number_of_frames = 25

    frames = np.linspace(0, 1, number_of_frames)
    frames = np.tile(frames, shader_values.shape[0])  # repeat it how many shaders there are
    frames = frames.reshape(-1, 1)

    x = np.repeat(shader_values, number_of_frames, axis=0)
    x = np.hstack((frames, x))
    x = x[:, :, np.newaxis]
    return x
