from bpy.types import Operator
import numpy as np

from material_recommender.gms import gpr

class LearnPreferencesOperator(Operator):
    bl_idname = 'scene.learn_preferences'
    bl_label = 'Learn'
    bl_description = 'A model with your preferences will be trained using '\
        'this batch of ratings.'

    @classmethod
    def poll(cls, context):
        materials = context.scene.preferences_properties.materials.collection
        for material in materials:
            if material.rating != 0:
                return True
        return False

    def execute(self, context):
        # TODO: implement learn operator
        preferences_properties = context.scene.preferences_properties

        trained_gpr = gpr.train(
            preferences_properties.materials.collection,
            preferences_properties.is_persistent
        )


        # MOCK for Search tab
        # import bpy
        # var = context.scene.search_properties.latent_space_image_id
        # bpy.data.textures.new(name=var, type='IMAGE')
        # props = context.scene.search_properties
        # props.materials.collection.add()
        # props.materials.index = 0
        # props.materials.collection[-1].frames_ids.add()
        # props.materials.collection[-1].frames_ids.add()
        # props.materials.collection[-1].frames_ids.add()

        # try:
        #     bpy.data.textures[var].image = bpy.data.images['b_frame0000.png']
        #     props.materials.collection[-1].frames_ids[0].id = 'a_a_frame0000.png'
        #     props.materials.collection[-1].frames_ids[1].id = 'a_a_frame0001.png'
        #     props.materials.collection[-1].frames_ids[2].id = 'a_a_frame0002.png'
        # except:
        #     bpy.data.textures[var].image = bpy.data.images['a_a_frame0000.png']
        #     props.materials.collection[-1].frames_ids[0].id = 'b_frame0000.png'
        #     props.materials.collection[-1].frames_ids[1].id = 'b_frame0001.png'
        #     props.materials.collection[-1].frames_ids[2].id = 'b_frame0002.png'
        # END MOCK

        preferences_properties.is_gpr_trained = True
        return {'FINISHED'}
