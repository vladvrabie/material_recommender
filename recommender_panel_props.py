import bpy
from bpy.props import EnumProperty
from bpy.types import PropertyGroup


class RecommenderPanelProps(PropertyGroup):

    tabs: EnumProperty(
        items = [
            ('LEARN', "Learn", "", 0),
            ('RECOMMANDATIONS', "Recommandations", "", 1),
        ],
        default = 'LEARN',
        name = "Tabs",
        description = '''Learn tab is for learning your material preferences 
            while the recommendations tab offers sugestions based on your preferences.'''
    )
