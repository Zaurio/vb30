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

from vb30.lib import ExportUtils

import TexCommonParams


TYPE = 'TEXTURE'
ID   = 'TexGradRamp'
NAME = 'Gradient Ramp'
DESC = "Gradient Ramp texture"

PluginParams = list(TexCommonParams.PluginParams)

PluginParams.extend([
    {
        'attr' : 'positions',
        'desc' : "positions of the given colors",
        'type' : 'FLOAT_LIST',
        'default' : 0.0,
    },
    {
        'attr' : 'colors',
        'desc' : "the given colors",
        'type' : 'LIST',
        'default' : (0.0, 0.0, 0.0),
    },
    {
        'attr' : 'gradient_position',
        'desc' : "",
        'type' : 'FLOAT_TEXTURE',
        'default' : 0,
    },
    {
        'attr' : 'texture_map',
        'desc' : "The texture used for mapped gradient ramp",
        'type' : 'TEXTURE',
        'default' : (0.0, 0.0, 0.0),
    },
    {
        'attr' : 'gradient_type',
        'desc' : "Gradient type",
        'type' : 'ENUM',
        'items' : (
            ('0',  "Four corner", "Four corner"),
            ('1',  "Box",         "Box"),
            ('2',  "Diagonal",    "Diagonal"),
            ('3',  "Lighting",    "Lighting"),
            ('4',  "Linear",      "Linear"),
            ('5',  "Mapped",      "Mapped"),
            ('6',  "Normal",      "normal"),
            ('7',  "Pong",        "Pong"),
            ('8',  "Radial",      "Radial"),
            ('9',  "Spiral",      "Spiral"),
            ('10', "Sweep",       "Sweep"),
            ('11', "Tartan",      "Tartan"),
            ('12', "Position",    "Return value in position"),
        ),
        'default' : '0',
    },
    {
        'attr' : 'interpolation',
        'desc' : "Interpolation",
        'type' : 'ENUM',
        'items' : (
            ('0', "None",          "None"),
            ('1', "Linear",        "Linear"),
            ('2', "Exponent Up",   "Exponent Up"),
            ('3', "Exponent Down", "Exponent Down"),
            ('4', "Smooth",        "Smooth"),
            ('5', "Bump",          "Bump"),
            ('6', "Spike",         "Spike"),
        ),
        'default' : '1',
    },
    {
        'attr' : 'noise_type',
        'desc' : "0:regular, 1:fractal, 2:turbulence",
        'type' : 'ENUM',
        'items' : (
            ('0', "Regular",    ""),
            ('1', "Fractal",    ""),
            ('2', "Turbulence", ""),
        ),
        'default' : '0',
    },
    {
        'attr' : 'noise_amount',
        'desc' : "Distortion noise amount",
        'type' : 'FLOAT',
        'default' : 0,
    },
    {
        'attr' : 'noise_size',
        'desc' : "",
        'type' : 'FLOAT',
        'default' : 1,
    },
    {
        'attr' : 'noise_phase',
        'desc' : "",
        'type' : 'FLOAT',
        'default' : 0,
    },
    {
        'attr' : 'noise_levels',
        'desc' : "",
        'type' : 'FLOAT',
        'default' : 4,
    },
    {
        'attr' : 'noise_treshold_low',
        'desc' : "",
        'type' : 'FLOAT',
        'default' : 0,
    },
    {
        'attr' : 'noise_treshold_high',
        'desc' : "",
        'type' : 'FLOAT',
        'default' : 0,
    },
    {
        'attr' : 'noise_smooth',
        'desc' : "",
        'type' : 'FLOAT',
        'default' : 0,
    },
])

PluginWidget = """
{ "widgets": [
    {   "layout" : "COLUMN",
        "attrs" : [
            { "name" : "gradient_type" },
            { "name" : "interpolation" }
        ]
    },

    {   "layout" : "SEPARATOR" },

    {   "layout" : "SPLIT",
        "splits" : [
            {   "layout" : "COLUMN",
                "align" : true,
                "attrs" : [
                    { "name" : "noise_type", "label" : "" },
                    { "name" : "noise_amount" },
                    { "name" : "noise_size" },
                    { "name" : "noise_levels" }
                ]
            },
            {   "layout" : "COLUMN",
                "align" : true,
                "attrs" : [
                    { "name" : "noise_phase" },
                    { "name" : "noise_treshold_low" },
                    { "name" : "noise_treshold_high" },
                    { "name" : "noise_smooth" }
                ]
            }
        ]
    },

    {TEX_COMMON}
]}
"""
PluginWidget = PluginWidget.replace('{TEX_COMMON}', TexCommonParams.PluginWidget)


def nodeDraw(context, layout, node):
    if not node.texture:
        layout.label("Missing texture!")
        return

    layout.template_color_ramp(node.texture, 'color_ramp', expand=True)
