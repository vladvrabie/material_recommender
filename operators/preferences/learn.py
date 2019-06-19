from bpy.types import Operator


class LearnPreferencesOperator(Operator):
    bl_idname = 'scene.learn_preferences'
    bl_label = 'Learn'
    bl_description = 'A model with your preferences will be trained using '\
        'this batch of ratings.'

    @classmethod
    def poll(cls, context):
        # TODO: if at least one is different than 0
        return True

    def execute(self, context):
        # TODO: implement learn operator

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

        context.scene.preferences_properties.is_gpr_trained = True
        return {'FINISHED'}
