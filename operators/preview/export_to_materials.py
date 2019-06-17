from bpy.types import Operator


class ExportToMaterialsOperator(Operator):
    bl_idname = 'preview.export_to_materials'
    bl_label = ''
    bl_description = 'This preview will be saved as a material based on '\
                     'a "Uber" material with a specific shader. The Uber '\
                     'material will be generated if it doesn\'t exist'

    def execute(self, context):
        # TODO: implement export to materials
        # remember pattern to find the selected material
        return {'FINISHED'}
