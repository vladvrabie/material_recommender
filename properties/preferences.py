from bpy.props import BoolProperty, IntProperty, PointerProperty
from bpy.types import PropertyGroup
from . data.material_list import MaterialList


class PreferenceProperties(PropertyGroup):

    materials: PointerProperty(
        type=MaterialList,
        name='Preference Tab Materials',
        description='The list of materials generated in the preference tab'
    )

    dirty_preview: BoolProperty(
        name='Is Preview Dirty',
        description='This toggles when user selects a new material ' +
                    'to preview, which will force a redraw.',
        default=False
    )

    persistent_gpr: BoolProperty(
        name='Persistent preferences',
        description='With persistent preferences, you can do multiple ' +
                    'rounds of rating materials. The recommender will get ' +
                    'better at recommending materials after each round.',
        default=False
    )

    gpr_threshold: IntProperty(
        name='Threshold',
        description='Minimum rating for a material to be recommended. ' +
                    'Search tab will use the materials rated above ' +
                    'this threshold.',
        default=7,
        min=0,
        max=10
    )
