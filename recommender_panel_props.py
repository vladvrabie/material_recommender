from bpy.props import BoolProperty, EnumProperty, IntProperty
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
                "preferences.",
                1
            ),
            (
                'SEARCH',
                "Search",
                "Search tab offers a grafical view of your " +
                "preferences. Blue dots are materials that are above " +
                "your threshold. New materials are inferred from the " +
                "coordinates given.",
                2
            )
        ],
        default='LEARN',
        name="Tabs",
        description='This addon can quickly generate materials ' +
                    'tailored to your preferences.'
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
