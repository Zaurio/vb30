#
# V-Ray For Blender
#
# http://chaosgroup.com
#
# Author: Andrei Izrantcev
# E-Mail: andrei.izrantcev@chaosgroup.com
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# All Rights Reserved. V-Ray(R) is a registered trademark of Chaos Software.
#

import bpy

import TexCommonParams


TYPE = 'TEXTURE'
ID   = 'TexRock'
NAME = 'Rock'
DESC = ""

PluginParams = list(TexCommonParams.PluginParams)

PluginParams.extend([
    {
        'attr' : 'use_3d_mapping',
        'desc' : "",
        'type' : 'BOOL',
        'default' : False,
    },
    {
        'attr' : 'color1_tex',
        'desc' : "",
        'type' : 'TEXTURE',
        'default' : (0.0, 0.0, 0.0),
    },
    {
        'attr' : 'color2_tex',
        'desc' : "",
        'type' : 'TEXTURE',
        'default' : (0.0, 0.0, 0.0),
    },
    {
        'attr' : 'grain_size',
        'desc' : "",
        'type' : 'FLOAT',
        'default' : 0.01,
    },
    {
        'attr' : 'diffusion',
        'desc' : "",
        'type' : 'FLOAT',
        'default' : 1,
    },
    {
        'attr' : 'mix_ratio',
        'desc' : "",
        'type' : 'FLOAT',
        'default' : 0.5,
    },
])


PluginWidget = """
{ "widgets": [
    {   "layout" : "ROW",
        "align" : true,
        "attrs" : [
            { "name" : "grain_size", "label" : "Grain" },
            { "name" : "diffusion" },
            { "name" : "mix_ratio" }
        ]
    },
    
    {   "layout" : "ROW",
        "align" : false,
        "attrs" : [
            { "name" : "use_3d_mapping" }
        ]
    },

    {TEX_COMMON}
]}
"""
PluginWidget = PluginWidget.replace('{TEX_COMMON}', TexCommonParams.PluginWidget)
