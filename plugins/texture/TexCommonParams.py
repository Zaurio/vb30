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

PluginParams = (
    # Outputs
    {
        'attr' : 'color',
        'desc' : "The resulting color",
        'type' : 'OUTPUT_TEXTURE',
        'default' : (0, 0, 0),
    },
    {
        'attr' : 'out_transparency',
        'desc' : "The resulting transparency",
        'type' : 'OUTPUT_TEXTURE',
        'default' : (0, 0, 0),
    },
    {
        'attr' : 'out_alpha',
        'desc' : "The resulting alpha",
        'type' : 'OUTPUT_FLOAT_TEXTURE',
        'default' : 1.0,
    },
    {
        'attr' : 'out_intensity',
        'desc' : "The resulting intensity",
        'type' : 'OUTPUT_FLOAT_TEXTURE',
        'default' : 1.0,
    },

    # Mappable params
    {
        'attr' : 'color_mult',
        'desc' : "A multiplier for the texture color",
        'type' : 'TEXTURE',
        'default' : (1, 1, 1),
    },
    {
        'attr' : 'color_offset',
        'desc' : "An additional offset for the texture color",
        'type' : 'TEXTURE',
        'default' : (0, 0, 0),
    },
    {
        'attr' : 'alpha_mult',
        'desc' : "A multiplier for the texture alpha",
        'type' : 'FLOAT_TEXTURE',
        'default' : 1,
    },
    {
        'attr' : 'alpha_offset',
        'desc' : "An additional offset for the texture alpha",
        'type' : 'FLOAT_TEXTURE',
        'default' : 0,
    },
    {
        'attr' : 'nouvw_color',
        'name' : 'No UV Color',
        'desc' : "The color when there are no valid uvw coordinates",
        'type' : 'TEXTURE',
        'default' : (0.5, 0.5, 0.5),
    },

    # UV generator
    {
        'attr' : 'uvwgen',
        'name' : "Mapping",
        'desc' : "The uvw generator for the texture",
        'type' : 'UVWGEN',
        'default' : "",
    },

    # Non mappable params
    {
        'attr' : 'compatibility_with',
        'desc' : "This is used to differentiate between textures exported from different applications",
        'type' : 'ENUM',
        'items' : (
            ('0', "3ds Max", ""),
            ('1', "Maya",    ""),
        ),
        'default' : '0',
    },
    {
        'attr' : 'alpha_from_intensity',
        'desc' : "",
        'type' : 'ENUM',
        'items' : (
            ('0', "Self",          "The alpha is taken from the alpha"),
            ('1', "Сompatibility", "The resulting alpha is the color intensity (if \"Compatibility\" is \"3ds max\") or the color luminance (if \"Compatibility\" is \"Maya\")"),
            ('2', "Force 1.0",     "The alpha is forced to 1.0f"),
        ),
        'default' : '0',
    },
    {
        'attr' : 'invert',
        'desc' : "If true, the resulting texture color will be inverted",
        'type' : 'BOOL',
        'default' : False,
    },
    {
        'attr' : 'invert_alpha',
        'desc' : "If true and invert is on, the resulting texture alpha will be inverted too. If false, just the color will be inverted",
        'type' : 'BOOL',
        'default' : True,
    },
    {
        'attr' : 'placement_type',
        'desc' : "The way the valid portion of the texture is applied",
        'type' : 'ENUM',
        'items' : (
            ('0', "Full",  "The whole texture is valid."),
            ('1', "Crop",  "Crop texture."),
            ('2', "Place", "Place texture."),
        ),
        'default' : '0',
    },
    {
        'attr' : 'u',
        'desc' : "U coordinate of the valid texture sector",
        'type' : 'FLOAT',
        'default' : 0,
    },
    {
        'attr' : 'v',
        'desc' : "V coordinate of the valid texture sector",
        'type' : 'FLOAT',
        'default' : 0,
    },
    {
        'attr' : 'w',
        'desc' : "Width of the valid texture sector",
        'type' : 'FLOAT',
        'default' : 1,
    },
    {
        'attr' : 'h',
        'desc' : "Height of the valid texture sector",
        'type' : 'FLOAT',
        'default' : 1,
    },
    {
        'attr' : 'jitter',
        'desc' : "Amount of random placement variation",
        'type' : 'FLOAT',
        'default' : 0,
    },
    {
        'attr' : 'tile_u',
        'desc' : "If true there is horizontal tiling",
        'type' : 'BOOL',
        'default' : True,
    },
    {
        'attr' : 'tile_v',
        'desc' : "If true there is vertical tiling",
        'type' : 'BOOL',
        'default' : True,
    },
    {
        'attr' : 'uv_noise_on',
        'desc' : "If true the noise is enabled",
        'type' : 'BOOL',
        'default' : False,
    },
    {
        'attr' : 'uv_noise_animate',
        'desc' : "If true the noise is animated",
        'type' : 'BOOL',
        'default' : True,
    },
    {
        'attr' : 'uv_noise_amount',
        'desc' : "UV noise amount",
        'type' : 'FLOAT',
        'default' : 1,
    },
    {
        'attr' : 'uv_noise_levels',
        'desc' : "UV noise iterations",
        'type' : 'FLOAT',
        'default' : 1,
    },
    {
        'attr' : 'uv_noise_size',
        'desc' : "UV noise size",
        'type' : 'FLOAT',
        'default' : 1,
    },
    {
        'attr' : 'un_noise_phase',
        'name' : "UV Noise Phase",
        'desc' : "UV noise phase",
        'type' : 'FLOAT',
        'default' : 0,
    },
)

PluginWidget = """
    {   "layout" : "SEPARATOR",
        "label" : "Common Properties" },

    {   "layout" : "ROW",
        "attrs" : [
            { "name" : "compatibility_with", "label" : "Compatibility" }
        ]
    },

    {   "layout" : "SEPARATOR",
        "label" : "Color" },

    {   "layout" : "COLUMN",
        "attrs" : [
            { "name" : "invert" }
        ]
    },

    {   "layout" : "SEPARATOR",
        "label" : "Alpha" },

    {   "layout" : "COLUMN",
        "align" : true,
        "attrs" : [
            { "name" : "alpha_from_intensity", "label" : "Alpha From" },
            { "name" : "invert_alpha" }
        ]
    },

    {   "layout" : "SEPARATOR",
        "label" : "UV" },
    
    {   "layout" : "COLUMN",
        "attrs" : [
            { "name" : "placement_type", "label" : "Placement" }
        ]
    },
    
    {   "layout" : "SPLIT",
        "splits" : [
            {   "layout" : "COLUMN",
                "align" : true,
                "attrs" : [
                    { "name" : "u" },
                    { "name" : "v" },
                    { "name" : "w" },
                    { "name" : "h" },
                    { "name" : "tile_u" },
                    { "name" : "tile_v" }
                ]
            },
            {   "layout" : "COLUMN",
                "align" : true,
                "attrs" : [
                    { "name" : "uv_noise_on" },
                    { "name" : "uv_noise_amount" },
                    { "name" : "uv_noise_levels" },
                    { "name" : "uv_noise_size" },
                    { "name" : "un_noise_phase" },
                    { "name" : "uv_noise_animate" }
                ]
            }
        ]
    }
"""
