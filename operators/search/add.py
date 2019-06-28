from bpy.types import Operator
import numpy as np

from material_recommender.gms import cnn
from material_recommender.gms import gplvm
from material_recommender.gms import gpr


class AddFromLatentSpaceOperator(Operator):
    bl_idname = 'scene.add_from_latent_space'
    bl_label = 'Add'
    bl_description = 'Press this button to add the material at the '\
        'given coordinates to the list for previewing'

    @classmethod
    def poll(cls, context):
        return context.scene.preferences_properties.is_gpr_trained

    def execute(self, context):
        properties = context.scene.search_properties
        materials = properties.materials.collection

        coordinates = np.array([[properties.x_coordinate, properties.y_coordinate]])
        shader_values = gplvm.predict(coordinates)  # (1, 20)
        rating = gpr.predict(shader_values)  # (1, 1)

        materials.add()
        current_material = materials[-1]
        # TODO: generate unique id
        # TODO: call neural net for frames
        cnn.hardcoded_predict(current_material)

        current_material.rating = int(np.clip(rating, 0, 10))
        current_material.shader_values = shader_values[0]

        # TODO: generate new render of latent space

        return {'FINISHED'}
