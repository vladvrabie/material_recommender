from bpy.types import Operator
import os


class ExportToVSEOperator(Operator):
    bl_idname = 'scene.export_to_vse'
    bl_label = ''
    bl_description = 'These frames can be exported to the Video Editor '\
        'Sequencer to be visualised as an animation.'

    def execute(self, context):
        gpr_material = context.scene.gpr_materials.selected
        frames_path, frames_names = gpr_material.save_to_disk()

        # context.scene.sequence_editor_create()  # good? bad?
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
