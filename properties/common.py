from bpy.props import EnumProperty
from bpy.types import PropertyGroup


def tab_changed(self, context):
    context.scene.preferences_properties.dirty_preview = True
    context.scene.recommendations_properties.dirty_preview = True
    context.scene.search_properties.dirty_preview = True


class GlobalProperties(PropertyGroup):

    tabs: EnumProperty(
        items=[
            (
                'PREFERENCES',
                "Preferences",
                "Here you rate materials to be used as basis for " +
                "recomandations.",
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
        default='PREFERENCES',
        name="Tabs",
        description='This addon can quickly generate materials ' +
                    'tailored to your preferences.',
        update=tab_changed
    )
