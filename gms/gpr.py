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

    if is_persistent:
        gpr_loaded = load_from_disk()
        if gpr_loaded is not None:
            x = np.vstack((x, gpr_loaded.X))
            y = np.vstack((y, gpr_loaded.Y))

    number_of_variables = x.shape[1]
    w_var = np.ones(number_of_variables)
    mlp = GPy.kern.MLP(number_of_variables, ARD=True, weight_variance=w_var)
    gpr_new = GPy.models.GPRegression(x, y, kernel=mlp)
    gpr_new.optimize('rprop')

    save_to_disk(gpr_new)

    return gpr_new


def predict(x, gpr_model=None):
    if gpr_model is None:
        gpr_model = load_from_disk()

    return gpr_model.predict(x)[0]  # not returning the variance


def load_from_disk():
    path = tempfile.gettempdir()
    path = os.path.join(path, 'material_recommender')
    if not os.path.isdir(path):
        os.mkdir(path)

    gprobj_path = os.path.join(path, 'gpr.obj')

    if not os.path.isfile(gprobj_path):
        return

    with open(gprobj_path, 'rb') as gprobj:
        gpr_loaded = pickle.load(gprobj)

    return gpr_loaded


def save_to_disk(model):
    if model is not None:
        path = tempfile.gettempdir()
        path = os.path.join(path, 'material_recommender')
        if not os.path.isdir(path):
            os.mkdir(path)

        gprobj_path = os.path.join(path, 'gpr.obj')

        with open(gprobj_path, 'wb') as gprobj:
            pickle.dump(model, gprobj)


def generate_random_shader(count=1):
    number_of_variables = 20
    shader = np.random.rand(count, number_of_variables)
    # Roughness of Glossy 1 is always 1
    shader[:, 3] = np.full((count,), 1.0)
    # Volume absorbtion density in (0, 2)
    shader[:, 11] *= 2
    # Glass roughness
    shader[:, 15] = np.random.uniform(0.0, 0.04, (count,))
    # Glass IOR
    shader[:, 16] = np.random.uniform(1.1, 2.0, (count,))
    return shader


def recommend(at_least=1, min_threshold=0, gpr_model=None):
    if gpr_model is None:
        gpr_model = load_from_disk()

    shaders, ratings = None, None
    while shaders is None:
        shaders, ratings = _recommend_from_batch(
            min_threshold=min_threshold,
            gpr_model=gpr_model
        )

    all_shaders = shaders
    all_ratings = ratings

    while all_shaders.shape[0] < at_least:
        shaders, ratings = _recommend_from_batch(
            min_threshold=min_threshold,
            gpr_model=gpr_model
        )

        if shaders is not None:
            all_shaders = np.vstack((all_shaders, shaders))
            all_ratings = np.vstack((all_ratings, ratings))

    return all_shaders, all_ratings


def _recommend_from_batch(batch_size=20, min_threshold=0, delta=2, gpr_model=None):
    shaders = generate_random_shader(batch_size)
    ratings = predict(shaders, gpr_model)
    ratings = np.clip(ratings, 0, 10)

    # Throw away the shaders that are too far away from threshold
    shaders = shaders[ratings.flatten() > min_threshold - delta]
    ratings = ratings[ratings.flatten() > min_threshold - delta]

    if shaders.shape[0] == 0:
        return None, None

    shaders_to_improve = ratings.flatten() < min_threshold
    count = np.count_nonzero(shaders_to_improve)

    minima = np.array([[0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,    0, 1.1, 0, 0, 0]])
    maxima = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 0.04,   2, 1, 1, 1]])

    number_of_steps = 20
    if count > 0:
        for _ in range(number_of_steps):
            corrections = 0.1 * generate_random_shader(count)
            if np.random.uniform(0, 1) < 0.5:
                shaders[shaders_to_improve] += corrections
            else:
                shaders[shaders_to_improve] -= corrections

            shaders[shaders_to_improve] = np.clip(
                shaders[shaders_to_improve],
                minima,
                maxima
            )

            ratings[shaders_to_improve] = predict(shaders[shaders_to_improve], gpr_model)
            shaders_to_improve = ratings.flatten() < min_threshold
            count = np.count_nonzero(shaders_to_improve)
            if count == 0:
                break

    # Throw away the shaders that below threshold
    shaders = shaders[ratings.flatten() > min_threshold]
    ratings = ratings[ratings.flatten() > min_threshold]

    return shaders, ratings
