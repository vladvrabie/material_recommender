import os
import pickle
import tempfile

import GPy
import numpy as np


def train(materials, is_persistent):
    # x - (30, 20)
    x = np.array([material.shader_values for material in materials])

    # y - (30, 1)
    y = np.array([material.rating for material in materials])
    y = y[:, np.newaxis]

    path = tempfile.gettempdir()
    path = os.path.join(path, 'material_recommender')
    if not os.path.isdir(path):
        os.mkdir(path)

    gprobj_path = os.path.join(path, 'gpr.obj')

    if is_persistent:
        if os.path.isfile(gprobj_path):
            with open(gprobj_path, 'rb') as gprobj:
                gpr_loaded = pickle.load(gprobj)
                x = np.vstack((x, gpr_loaded.X))
                y = np.vstack((y, gpr_loaded.Y))

    number_of_variables = x.shape[1]
    w_var = np.ones(number_of_variables)
    mlp = GPy.kern.MLP(number_of_variables, ARD=True, weight_variance=w_var)
    gpr_new = GPy.models.GPRegression(x, y, kernel=mlp)
    gpr_new.optimize('rprop')

    with open(gprobj_path, 'wb') as gprobj:
        pickle.dump(gpr_new, gprobj)

    return gpr_new


def predict(materials):
    path = tempfile.gettempdir()
    path = os.path.join(path, 'material_recommender')
    if not os.path.isdir(path):
        os.mkdir(path)

    gprobj_path = os.path.join(path, 'gpr.obj')

    if not os.path.isfile(gprobj_path):
        return

    with open(gprobj_path, 'rb') as gprobj:
        gpr_loaded = pickle.load(gprobj)

    x = np.array([material.shader_values for material in materials])
    return gpr_loaded.predict(x)[0]  # not returning the variance
