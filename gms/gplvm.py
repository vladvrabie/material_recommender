import os
import pickle
import tempfile

import GPy
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from . import gpr


def train(x, dimensions=2):
    gplvm_model = GPy.models.GPLVM(x, dimensions)
    gplvm_model.optimize('rprop')

    save_to_disk(gplvm_model)

    return gplvm_model


def predict(coords, gplvm_model=None):
    if gplvm_model is None:
        gplvm_model = load_from_disk()

    return gplvm_model.predict(coords)[0]  # not returning the variance


def generate_preference_map(y, highlight_coords=None,
                            gplvm_model=None, gpr_model=None):
    if gplvm_model is None:
        gplvm_model = load_from_disk()

    xmin, xmax = -2.5, 2.5
    ymin, ymax = -2.5, 2.5
    plot_resolution = 20
    dimensions = 2

    plot_x = np.linspace(xmin, xmax, plot_resolution)
    plot_y = np.linspace(ymax, ymin, plot_resolution)

    mesh_x, mesh_y = np.meshgrid(plot_x, plot_y)

    xy_coordinates = np.stack((mesh_x, mesh_y), axis=-1)
    xy_coordinates = xy_coordinates.reshape(-1, dimensions)

    latent_space_materials = gplvm_model.predict(xy_coordinates)[0]  # (400, 20)

    if gpr_model is None:
        gpr_model = gpr.load_from_disk()

    latent_space_ratings = gpr.predict(latent_space_materials, gpr_model)  # (400, 1)
    latent_space_ratings = latent_space_ratings.reshape(plot_resolution, plot_resolution)

    preferences_coordinates = gplvm_model.infer_newX(y, optimize=True)[0]

    matplotlib.use('Agg')
    fig, ax = plt.subplots()
    plt.imshow(
        latent_space_ratings,
        interpolation='lanczos',
        extent=[xmin, xmax, ymin, ymax],
        cmap=plt.get_cmap('autumn')
    )
    plt.colorbar()
    for pref_coord in preferences_coordinates:
        circle = plt.Circle(pref_coord, 0.08, color='g')
        ax.add_artist(circle)
    if highlight_coords is not None:
        circle = plt.Circle(highlight_coords, 0.08, color='b')
        ax.add_artist(circle)

    fig.tight_layout(pad=0.8)
    fig.set_size_inches(4, 3)
    fig.canvas.draw()
    # plt.savefig(path, format='png', dpi=100)

    data = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8, sep='')
    width, height = fig.canvas.get_width_height()
    data = data.reshape(height, width, 3)

    plt.clf()
    plt.close()

    return data


def load_from_disk():
    path = tempfile.gettempdir()
    path = os.path.join(path, 'material_recommender')
    if not os.path.isdir(path):
        os.mkdir(path)

    gplvmobj_path = os.path.join(path, 'gplvm.obj')

    if not os.path.isfile(gplvmobj_path):
        return

    with open(gplvmobj_path, 'rb') as gplvmobj:
        gplvm_loaded = pickle.load(gplvmobj)

    return gplvm_loaded


def save_to_disk(model):
    if model is not None:
        path = tempfile.gettempdir()
        path = os.path.join(path, 'material_recommender')
        if not os.path.isdir(path):
            os.mkdir(path)

        gplvmobj_path = os.path.join(path, 'gplvm.obj')

        with open(gplvmobj_path, 'wb') as gplvmobj:
            pickle.dump(model, gplvmobj)
