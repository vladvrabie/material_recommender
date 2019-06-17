import os

from bpy.types import Operator


class ExportToVSEOperator(Operator):
    bl_idname = 'preview.export_to_vse'
    bl_label = ''
    bl_description = 'These frames can be exported to the Video Editor '\
        'Sequencer to be visualised as an animation.'

    def execute(self, context):
        material = context.scene.preferences_properties.materials.selected
        frames_path, frames_names = material.save_to_disk()

        # context.scene.sequence_editor_create()  # add? remove?
        sequence_name = 'RecommenderStrip'
        sequences = context.scene.sequence_editor.sequences

        if sequence_name in sequences:
            sequences.remove(sequences[sequence_name])

        sequence = sequences.new_image(
            name=sequence_name,
            filepath=os.path.join(frames_path, frames_names[0]),
            channel=1,
            frame_start=1,
        )

        for i in range(1, len(frames_names)):
            sequence.elements.append(frames_names[i])

        return {'FINISHED'}
