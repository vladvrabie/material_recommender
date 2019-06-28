# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import os
import sys
sys.path.append(os.path.abspath('.'))

import bpy
from bpy.props import PointerProperty
from bpy.types import Scene
from bpy.utils import register_class

from . operators.preferences.generator import PreferencesListGenerator
from . operators.preferences.learn import LearnPreferencesOperator
from . operators.preview.export_to_materials import ExportToMaterialsOperator
from . operators.preview.export_to_vse import ExportToVSEOperator
from . operators.preview.steppers import FrameStepper
from . operators.preview.steppers import NextFrameStepper
from . operators.preview.steppers import PreviousFrameStepper
from . operators.recommendations.clear import ClearRecommendationsOperator
from . operators.recommendations.recommend import RecommendOperator
from . operators.search.add import AddFromLatentSpaceOperator
from . panels.recommender_panel import RecommenderPanel
from . properties.data.frame_id import FrameIdGroup
from . properties.data.material_data import MaterialData
from . properties.data.material_list import MaterialList
from . properties.common import GlobalProperties
from . properties.preferences import PreferencesProperties
from . properties.recommendations import RecommendationsProperties
from . properties.search import SearchProperties
from . ui.base_list import BASE_UL_List
from . ui.preferences import PREFERENCES_UL_List
from . ui.recommendations import RECOMMENDATIONS_UL_List
from . ui.search import SEARCH_UL_List


bl_info = {
    "name": "Material Recommender",
    "author": "Vlad Vrabie",
    "description": "Quickly generate materials based on your preferences",
    "blender": (2, 80, 0),
    "version": (0, 0, 1),
    "location": "Properties",
    "warning": "",
    "category": "Material"
}

classes = (
    PreferencesListGenerator,
    LearnPreferencesOperator,
    ExportToMaterialsOperator,
    ExportToVSEOperator,
    FrameStepper,
    NextFrameStepper,
    PreviousFrameStepper,
    ClearRecommendationsOperator,
    RecommendOperator,
    AddFromLatentSpaceOperator,
    RecommenderPanel,
    FrameIdGroup,
    MaterialData,
    MaterialList,
    GlobalProperties,
    PreferencesProperties,
    RecommendationsProperties,
    SearchProperties,
    BASE_UL_List,
    PREFERENCES_UL_List,
    RECOMMENDATIONS_UL_List,
    SEARCH_UL_List
)


def register():
    for aclass in classes:
        register_class(aclass)
    Scene.global_properties = PointerProperty(type=GlobalProperties)
    Scene.preferences_properties = PointerProperty(type=PreferencesProperties)
    Scene.recommendations_properties = PointerProperty(type=RecommendationsProperties)
    Scene.search_properties = PointerProperty(type=SearchProperties)


def unregister():
    for aclass in classes:
        bpy.utils.unregister_class(aclass)
    del Scene.global_properties
    del Scene.preferences_properties
    del Scene.recommendations_properties
    del Scene.search_properties


if __name__ == '__main__':
    register()
