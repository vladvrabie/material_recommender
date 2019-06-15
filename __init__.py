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

import bpy
from bpy.props import PointerProperty
from bpy.types import Scene
from bpy.utils import register_class

from . frame_id_property import FrameIdProperty
from . gpr_material_data import GPRMaterialData
from . gpr_materials_list import GPRMaterialsList
from . gpr_list_generator import GRPListGenerator
from . gpr_ui_list import GPRUIList
from . recommender_panel import RecommenderPanel
from . recommender_panel_props import RecommenderPanelProps

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
    FrameIdProperty,
    GPRMaterialData,
    GPRMaterialsList,
    GRPListGenerator,
    GPRUIList,
    RecommenderPanelProps,
    RecommenderPanel
)


def register():
    for aclass in classes:
        register_class(aclass)
    Scene.recommender_props = PointerProperty(type=RecommenderPanelProps)
    Scene.gpr_materials = PointerProperty(type=GPRMaterialsList)


def unregister():
    for aclass in classes:
        bpy.utils.unregister_class(aclass)
    del bpy.types.Scene.recommender_props
    del bpy.types.Scene.gpr_materials


if __name__ == '__main__':
    register()
