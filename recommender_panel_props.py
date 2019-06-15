from bpy.props import BoolProperty, EnumProperty
from bpy.types import PropertyGroup


class RecommenderPanelProps(PropertyGroup):

    tabs: EnumProperty(
        items=[
            (
                'LEARN',
                "Learn",
                "Learn tab is for learning your material preferences.",
                0
            ),
            (
                'RECOMMENDATIONS',
                "Recommendations",
                "Recommendations tab offers sugestions based on your " +
                "preferences. You can fine tune and save materials.",
                1
            )
        ],
        default='LEARN',
        name="Tabs",
        description='This addon can quickly generate materials ' +
                    'tailored to your preferences.'
    )

    dirty_preview: BoolProperty(
        name='Is Preview Dirty',
        description='This toggles when user selects a new material' +
                    'to preview, which will force a redraw.',
        default=False
    )
