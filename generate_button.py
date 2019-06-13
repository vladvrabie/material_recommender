import bpy


class GenerateButton(bpy.types.Operator):
    bl_idname = "material.generate_button"
    bl_label = "Generate materials"
    bl_description = "Materials will be generated based on your preferences."

    def execute(self, context):
        #TODO: open window
        return {"FINISHED"}  # sau RUNNING_MODAL
