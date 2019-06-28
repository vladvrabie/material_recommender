from bpy.types import PropertyGroup

from . base import BaseTabProperties


class RecommendationsProperties(BaseTabProperties, PropertyGroup):

    @property
    def next_id(self):
        current_id = 'Recomm{}'.format(self.unique_index)
        self.unique_index += 1
        return current_id
