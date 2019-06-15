from bpy.types import Operator


class FrameStepper(Operator):
    bl_idname = 'preview.basestepper'
    bl_label = 'Base Frame Stepper'
    bl_description = 'This operator will step through '\
        'the frames of the render.'

    # step is not defined here; derived classes don't override it
    def execute(self, context):
        gpr_material = context.scene.gpr_materials.selected
        gpr_material.preview_frame_index += self.step
        gpr_material.preview_frame_index %= len(gpr_material.frames_ids)
        properties = context.scene.recommender_props
        properties.dirty_preview = True
        return {'FINISHED'}


class NextFrameStepper(FrameStepper):
    bl_idname = 'preview.nextstepper'
    bl_label = ''
    bl_description = 'This operator will move to the next '\
        'frame of the render.'

    step: int = 1


class PreviousFrameStepper(FrameStepper):
    bl_idname = 'preview.previousstepper'
    bl_label = ''
    bl_description = 'This operator will move to the previous '\
        'frame of the render.'

    step: int = -1
