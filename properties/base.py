from bpy.props import BoolProperty, PointerProperty

from . data.material_list import MaterialList


class BaseTabProperties:

    materials: PointerProperty(
        type=MaterialList,
        name='Tab Materials',
        description='The list of materials generated in the tab'
    )

    dirty_preview: BoolProperty(
        name='Is Preview Dirty',
        description='This toggles when user selects a new material ' +
                    'to preview, which will force a redraw.',
        default=False
    )
