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

TYPE = 'SETTINGS'
ID   = 'SettingsColorMapping'
NAME = 'Color Mapping'
DESC = ""


def UpdateSystemGamma(self, context):
    if self.sync_with_gamma:
        view_settings = context.scene.view_settings
        view_settings.gamma = 1.0 / self.gamma


PluginParams = (
    {
        'attr' : 'type',
        'desc' : "",
        'type' : 'ENUM',
        'items' : (
            ('0', "Linear", ""),
            ('1', "Exponential", ""),
            ('2', "HSV Exponential", ""),
            ('3', "Intensity Exponential", ""),
            ('4', "Gamma Correction", ""),
            ('5', "Intensity Gamma", ""),
            ('6', "Reinhard", "")
        ),
        'default' : '0',
    },
    {
        'attr' : 'affect_background',
        'desc' : "Affect colors belonging to the background",
        'type' : 'BOOL',
        'default' : True,
    },
    {
        'attr' : 'dark_mult',
        'name' : "Dark multiplier",
        'desc' : "Multiplier for dark colors",
        'type' : 'FLOAT',
        'default' : 1,
    },
    {
        'attr' : 'bright_mult',
        'name' : "Bright multiplier",
        'desc' : "Multiplier for bright colors",
        'type' : 'FLOAT',
        'default' : 1,
    },
    {
        'attr' : 'gamma',
        'desc' : "Gamma correction for the output image regardless of the color mapping mode",
        'type' : 'FLOAT',
        'update' : UpdateSystemGamma,
        'default' : 1,
    },
    {
        'attr' : 'subpixel_mapping',
        'desc' : "This option controls whether color mapping will be applied to the final image pixels, or to the individual sub-pixel samples",
        'type' : 'BOOL',
        'default' : False,
    },
    {
        'attr' : 'clamp_output',
        'desc' : "Clamp colors",
        'type' : 'BOOL',
        'default' : False,
    },
    {
        'attr' : 'clamp_level',
        'desc' : "The level at which colors will be clamped",
        'type' : 'FLOAT',
        'default' : 1,
    },
    {
        'attr' : 'adaptation_only',
        'name' : "Mode",
        'desc' : "Specifies whether color mapping and gamma are applied to the image",
        'type' : 'ENUM',
        'items' : (
            ('0', "Color Mapping & Gamma", "Both \"Color Mapping\" and \"Gamma\" are applied"),
            ('1', "Don't Affect Colors",   "Nothing is applied"),
            ('2', "Color Mapping Only",    "Only color mapping is applied"),
        ),
        'default' : '0',
    },
    {
        'attr' : 'linearWorkflow',
        'desc' : "When this option is checked V-Ray will automatically apply the inverse of the Gamma correction that you have set in the Gamma field to all materials in scene",
        'type' : 'BOOL',
        'default' : False,
    },
    {
        'attr' : 'exposure',
        'desc' : "Additional image exposure",
        'type' : 'COLOR',
        'default' : (1, 1, 1),
    },

    {
        'attr' : 'input_gamma',
        'desc' : "Input gamma for textures",
        'type' : 'FLOAT',
        'skip' : True,
        'default' : 1,
    },
    {
        'attr' : 'use_input_gamma',
        'desc' : "Use global \"Input Gamma\" for textures",
        'type' : 'BOOL',
        'skip' : True,
        'default' : False,
    },
    {
        'attr' : 'sync_with_gamma',
        'desc' : "Set Blender's \"Color Management\" Gamma to (1.0 / ColorMapping.Gamma)",
        'type' : 'BOOL',
        'update' : UpdateSystemGamma,
        'skip' : True,
        'default' : False,
    },
    {
        'attr' : 'preview_use_scene_cm',
        'name' : "Use For Preview",
        'desc' : "Use current scene \"Color Mapping\" settings",
        'type' : 'BOOL',
        'skip' : True,
        'default' : True,
    },
)

PluginWidget = """
{ "widgets": [
]}
"""


def writeDatablock(bus, pluginModule, pluginName, propGroup, overrideParams):
    import bpy
    from vb30.lib import ExportUtils

    current_scene_cm = bpy.context.scene.vray.SettingsColorMapping

    if bus['preview'] and current_scene_cm.preview_use_scene_cm:
        # Use color mapping settings from current scene not from preview scene
        propGroup = current_scene_cm

    return ExportUtils.WritePluginCustom(bus, pluginModule, pluginName, propGroup, overrideParams)
