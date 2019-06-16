from bpy.types import Operator


class ExportToVSEOperator(Operator):
    bl_idname = 'scene.export_to_vse'
    bl_label = ''
    bl_description = 'These frames can be exported to the Video Editor '\
        'Sequencer to be visualised as an animation.'

    def execute(self, context):
        return {'FINISHED'}
