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

bl_info = {
    "name" : "Material Recommender",
    "author" : "Vlad Vrabie",
    "description" : "Quickly generate materials based on your preferences",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "Properties",
    "warning" : "",
    "category" : "Material"
}

import bpy

from . recommender_panel import RecommenderPanel
from . recommender_panel_props import RecommenderPanelProps

classes = (RecommenderPanelProps, RecommenderPanel)

def register():
    for aclass in classes:
        bpy.utils.register_class(aclass)
    bpy.types.Scene.recommender_props = bpy.props.PointerProperty(type=RecommenderPanelProps)

def unregister():
    for aclass in classes:
        bpy.utils.unregister_class(aclass)
    del bpy.types.Scene.recommender_props

if __name__ == '__main__':
    register()
