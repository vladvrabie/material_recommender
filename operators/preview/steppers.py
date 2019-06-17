from bpy.types import Operator


class FrameStepper(Operator):
    bl_idname = 'preview.base_stepper'
    bl_label = 'Base Frame Stepper'
    bl_description = 'This operator will step through '\
        'the frames of the render.'

    def execute(self, context):
        properties = context.scene.global_properties

        if properties.tabs == 'PREFERENCES':
            properties = context.scene.preferences_properties
        elif properties.tabs == 'RECOMMENDATIONS':
            properties = context.scene.recommendations_properties
        elif properties.tabs == 'SEARCH':
            properties = context.scene.search_properties

        material = properties.materials.selected
        material.preview_frame_index += self.step
        material.preview_frame_index %= len(material.frames_ids)
        properties.dirty_preview = True
        return {'FINISHED'}


class NextFrameStepper(FrameStepper):
    bl_idname = 'preview.next_stepper'
    bl_label = ''
    bl_description = 'This operator will move to the next '\
        'frame of the render.'

    step: int = 1


class PreviousFrameStepper(FrameStepper):
    bl_idname = 'preview.previous_stepper'
    bl_label = ''
    bl_description = 'This operator will move to the previous '\
        'frame of the render.'

    step: int = -1
