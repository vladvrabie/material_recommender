from bpy.types import Operator


class ViewFromLatentSpaceOperator(Operator):
    bl_idname = 'scene.view_from_latent_space'
    bl_label = 'View'
    bl_description = 'Press this button to preview the material at the '\
        'given coordinates'

    def execute(self, context):
        properties = context.scene.search_properties
        properties.materials.collection.clear()

        # TODO: implement view from latent space
        # get material float values from latent space
        # generate frames
        # load frames into blender and create material property group
        # MAYBE: generate new render of latent space

        # properties.materials.index = 0  # TODO: uncomment on finishing implementation
        # # always 1 material and will refresh the view
        return {'FINISHED'}
