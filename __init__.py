# ##### BEGIN GPL LICENSE BLOCK #####
#
#  <Blender Project Starter is an addon for automatic Project Folder Structure Generation.>
#    Copyright (C) <2021>  <Steven Scott>
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 3
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

bl_info = {
    "name": "Blender Project Starter",
    "description": "",
    "author": "Steven Scott, Blender Defender",
    "version": (1, 0, 0),
    "blender": (2, 83, 0),
    "location": "Properties >> Scene Properties",
    "warning": "",
    "wiki_url": "https://www.youtube.com/channel/UCiy-QcXrvu9hhe4arymNcfw",
    "tracker_url": "https://github.com/BlenderDefender/blender_project_starter/issues",
    "category": "System"
}


from .functions.main_functions import (
    sn_print,
    sn_handle_script_line_exception,
    sn_register_icons,
    sn_register_properties,
    sn_unregister_icons,
    sn_unregister_properties,
)

from . import (
    operators,
    prefs,
    panels
)


def register():
    operators.register()
    prefs.register(bl_info)
    panels.register()

    sn_register_icons()
    sn_register_properties()


def unregister():
    operators.unregister()
    prefs.unregister()
    panels.unregister()

    sn_unregister_icons()
    sn_unregister_properties()
