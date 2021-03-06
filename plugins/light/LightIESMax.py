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


TYPE = 'LIGHT'
ID   = 'LightIESMax'
NAME = 'IES (3ds max)'
DESC = ""

PluginParams = (
    {
        'attr' : 'enabled',
        'desc' : "true if the light is casting light (turned on) and false otherwise; it only makes sense to use this parameter if it is animated, or if another object depends on this node but it must not be rendered",
        'type' : 'BOOL',
        'default' : True,
    },
    {
        'attr' : 'transform',
        'desc' : "",
        'type' : 'TRANSFORM',
        'default' : None,
    },
    {
        'attr' : 'color',
        'desc' : "Color of the light",
        'type' : 'COLOR',
        'default' : (1, 1, 1),
    },
    {
        'attr' : 'color_tex',
        'desc' : "A color texture that if present will override the color parameter",
        'type' : 'TEXTURE',
        'default' : (0.0, 0.0, 0.0),
    },
    {
        'attr' : 'shadows',
        'desc' : "true if the light casts shadows and false otherwise",
        'type' : 'BOOL',
        'default' : True,
    },
    {
        'attr' : 'shadowColor',
        'desc' : "The shadow color. Anything but black is not physically accurate",
        'type' : 'COLOR',
        'default' : (0, 0, 0),
    },
    {
        'attr' : 'shadowColor_tex',
        'desc' : "A color texture that if present will override the shadowColor parameter",
        'type' : 'TEXTURE',
        'default' : (0.0, 0.0, 0.0),
    },
    {
        'attr' : 'shadowBias',
        'desc' : "Shadow offset from the surface. Helps to prevent polygonal shadow artifacts on low-poly surfaces",
        'type' : 'FLOAT',
        'default' : 0,
    },
    {
        'attr' : 'photonSubdivs',
        'desc' : "",
        'type' : 'INT',
        'default' : 500,
    },
    {
        'attr' : 'causticSubdivs',
        'desc' : "",
        'type' : 'INT',
        'default' : 1000,
    },
    {
        'attr' : 'diffuseMult',
        'desc' : "Multiplier for the diffuse photons",
        'type' : 'FLOAT',
        'default' : 1,
    },
    {
        'attr' : 'causticMult',
        'desc' : "Multiplier for the caustic photons",
        'type' : 'FLOAT',
        'default' : 1,
    },
    {
        'attr' : 'cutoffThreshold',
        'desc' : "Light cut-off threshold (speed optimization). If the light intensity for a point is below this threshold, the light will not be computed",
        'type' : 'FLOAT',
        'default' : 0.001,
    },
    {
        'attr' : 'affectDiffuse',
        'desc' : "true if the light produces diffuse lighting and false otherwise",
        'type' : 'BOOL',
        'default' : True,
    },
    {
        'attr' : 'affectSpecular',
        'desc' : "true if the light produces specular hilights and false otherwise",
        'type' : 'BOOL',
        'default' : True,
    },
    {
        'attr' : 'bumped_below_surface_check',
        'desc' : "true if the bumped normal should be used to check if the light dir is below the surface",
        'type' : 'BOOL',
        'default' : False,
    },
    {
        'attr' : 'nsamples',
        'desc' : "Number of parameter samples for motion blur",
        'type' : 'INT',
        'default' : 0,
    },
    {
        'attr' : 'diffuse_contribution',
        'desc' : "Diffuse contribution for the light",
        'type' : 'FLOAT',
        'default' : 1,
    },
    {
        'attr' : 'specular_contribution',
        'desc' : "Specular contribution for the light",
        'type' : 'FLOAT',
        'default' : 1,
    },
    {
        'attr' : 'channels',
        'desc' : "Render channels the result of this light will be written to",
        'type' : 'PLUGIN',
        'default' : "",
    },
    {
        'attr' : 'channels_raw',
        'desc' : "Render channels the raw diffuse result of this light will be written to",
        'type' : 'PLUGIN',
        'default' : "",
    },
    {
        'attr' : 'channels_diffuse',
        'desc' : "Render channels the diffuse result of this light will be written to",
        'type' : 'PLUGIN',
        'default' : "",
    },
    {
        'attr' : 'channels_specular',
        'desc' : "Render channels the specular result of this light will be written to",
        'type' : 'PLUGIN',
        'default' : "",
    },
    {
        'attr' : 'use_global_light_level',
        'desc' : "true if the light should use the global light level setting",
        'type' : 'BOOL',
        'default' : True,
    },
    {
        'attr' : 'shadowSubdivs',
        'desc' : "",
        'type' : 'INT',
        'default' : 8,
    },
    {
        'attr' : 'storeWithIrradianceMap',
        'desc' : "",
        'type' : 'BOOL',
        'default' : False,
    },
    {
        'attr' : 'ies_file',
        'desc' : "IES file with luminaire description",
        'type' : 'STRING',
        'subtype' : 'FILE_PATH',        
        'default' : "",
    },
    {
        'attr' : 'filter_color',
        'desc' : "",
        'type' : 'COLOR',
        'default' : (1, 1, 1),
    },
    {
        'attr' : 'soft_shadows',
        'desc' : "true to use the shape of the light as described in the IES profile",
        'type' : 'BOOL',
        'default' : False,
    },
    {
        'attr' : 'area_speculars',
        'desc' : "true to cause specular highlights produced by the light to match the light shape; false to always produce speculars as a point light",
        'type' : 'BOOL',
        'default' : True,
    },
    {
        'attr' : 'power',
        'desc' : "Limuous power (in lm); if zero, the default lumious power from the IES profile is used",
        'type' : 'FLOAT',
        'default' : 0,
    },
    {
        'attr' : 'ies_light_shape',
        'desc' : "IES light shape",
        'type' : 'ENUM',
        'items' : (
            ('-1', "From File", ""),
            ('0',  "Custom", "")
        ),
        'default' : '-1',
    },
    {
        'attr' : 'ies_light_width',
        'desc' : "Light shape width (in metres)",
        'type' : 'FLOAT',
        'default' : 0,
    },
    {
        'attr' : 'ies_light_length',
        'desc' : "Light shape length (in metres)",
        'type' : 'FLOAT',
        'default' : 0,
    },
    {
        'attr' : 'ies_light_height',
        'desc' : "Light shape height (in metres)",
        'type' : 'FLOAT',
        'default' : 0,
    },
    {
        'attr' : 'ies_light_diameter',
        'desc' : "Light shape diameter (in metres)",
        'type' : 'FLOAT',
        'default' : 0,
    },
)

PluginWidget = """
{ "widgets": [
    {   "layout" : "ROW",
        "attrs" : [
            { "name" : "enabled" }
        ]
    },

    {   "layout" : "ROW",
        "attrs" : [
            { "name" : "ies_file" }
        ]
    },

    {   "layout" : "SPLIT",
        "splits" : [
            {   "layout" : "COLUMN",
                "attrs" : [
                    { "name" : "color", "label" : "" }                   
                ]
            },
            {   "layout" : "COLUMN",
                "attrs" : [
                    { "name" : "power" },
                    { "name" : "shadowSubdivs" }
                ]
            }
        ]
    },

    {   "layout" : "SPLIT",
        "splits" : [
            {   "layout" : "COLUMN",
                "align" : false,
                "attrs" : [
                    { "name" : "shadows" },
                    { "name" : "shadowBias" },
                    { "name" : "shadowColor", "label" : "" }
                ]
            },
            {   "layout" : "COLUMN",
                "align" : true,
                "attrs" : [
                    { "name" : "soft_shadows" }
                ]
            }
        ]
    },

    {   "layout" : "SPLIT",
        "splits" : [
            {   "layout" : "COLUMN",
                "align" : true,
                "attrs" : [
                    { "name" : "ies_light_shape", "label" : "Shape" }
                ]
            },
            {   "layout" : "COLUMN",
                "align" : true,
                "attrs" : [
                    { "name" : "ies_light_width" },
                    { "name" : "ies_light_length" },
                    { "name" : "ies_light_height"  },
                    { "name" : "ies_light_diameter" }
                ]
            }
        ]
    },

    {   "layout" : "SPLIT",
        "splits" : [
            {   "layout" : "COLUMN",
                "align" : true,
                "attrs" : [
                    { "name" : "photonSubdivs" },
                    { "name" : "diffuseMult" }
                ]
            },
            {   "layout" : "COLUMN",
                "align" : true,
                "attrs" : [
                    { "name" : "causticSubdivs" },
                    { "name" : "causticMult" }
                ]
            }
        ]
    },

    {   "layout" : "SPLIT",
        "splits" : [
            {   "layout" : "COLUMN",
                "align" : true,
                "attrs" : [
                    { "name" : "storeWithIrradianceMap" },
                    { "name" : "bumped_below_surface_check" }
                ]
            },
            {   "layout" : "COLUMN",
                "align" : true,
                "attrs" : [
                    { "name" : "cutoffThreshold" },
                    { "name" : "nsamples" },
                    { "name" : "use_global_light_level" }
                ]
            }
        ]
    },

    {   "layout" : "SPLIT",
        "splits" : [
            {   "layout" : "COLUMN",
                "align" : true,
                "attrs" : [
                { "name" : "diffuse_contribution" },
                { "name" : "specular_contribution" }
                ]
            },
            {   "layout" : "COLUMN",
                "align" : true,
                "attrs" : [
                    { "name" : "area_speculars" },
                    { "name" : "affectSpecular" },
                    { "name" : "affectDiffuse" }
                ]
            }
        ]
    }
]}
"""
