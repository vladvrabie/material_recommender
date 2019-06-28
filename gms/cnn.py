import os

from keras import backend as K
from keras.models import model_from_json
import numpy as np


def hardcoded_predict(material_data):
    folder1 = r'C:\Users\tbd7bm\Desktop\licenta\h200'
    # folder2 = ('C:\\Users\\vladv\\Desktop\\test\\0_14_12__0\\', 'a_a_')
    # # folder3 = ('C:\\Users\\vladv\\Desktop\\test\\18_6_40__0\\', 'b_')
    # sel = random.sample((folder1, folder2), 1)[0]
    material_data.id = 'mat'
    material_data.load_from_folder(
        folder1,
        frames_count=25,
        # prefix=sel[1],
        extension='.png'
    )


def predict(shader_values):
    # TODO: implement cnn predict
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
