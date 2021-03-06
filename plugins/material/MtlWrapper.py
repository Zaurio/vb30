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

from vb30.lib.DrawUtils import GetContextType, GetRegionWidthFromContext
from vb30.ui.classes    import narrowui


TYPE = 'MATERIAL'
ID   = 'MtlWrapper'
NAME = 'Wrapper'
DESC = ""

PluginParams = (
    {
        'attr' : 'base_material',
        'desc' : "The base material",
        'type' : 'MATERIAL',
        'default' : "",
    },
    {
        'attr' : 'generate_gi',
        'desc' : "Controls the GI generated by the material",
        'type' : 'FLOAT',
        'default' : 1,
    },
    {
        'attr' : 'receive_gi',
        'desc' : "Controls the GI received by the material",
        'type' : 'FLOAT',
        'default' : 1,
    },
    {
        'attr' : 'generate_caustics',
        'desc' : "Controls the caustics generated by the material",
        'type' : 'FLOAT',
        'default' : 1,
    },
    {
        'attr' : 'receive_caustics',
        'desc' : "Controls the caustics received by the material",
        'type' : 'FLOAT',
        'default' : 1,
    },
    {
        'attr' : 'alpha_contribution',
        'desc' : "The contribution of the resulting color to the alpha channel",
        'type' : 'FLOAT',
        'default' : 1,
    },
    {
        'attr' : 'matte_surface',
        'desc' : "Makes the material appear as a matte material, which shows the background, instead of the base material, when viewed directly",
        'type' : 'BOOL',
        'default' : False,
    },
    {
        'attr' : 'shadows',
        'desc' : "Turn this on to make shadow visible on the matter surface",
        'type' : 'BOOL',
        'default' : False,
    },
    {
        'attr' : 'affect_alpha',
        'desc' : "Turn this on to make shadows affect the alpha contribution of the matte surface",
        'type' : 'BOOL',
        'default' : False,
    },
    {
        'attr' : 'shadow_tint_color',
        'desc' : "Tint for the shadows on the matte surface",
        'type' : 'COLOR',
        'default' : (0, 0, 0),
    },
    {
        'attr' : 'shadow_brightness',
        'desc' : "An optional brightness parameter for the shadows on the matte surface.A value of 0.0 will make the shadows completely invisible, while a value of 1.0 will show the full shadows",
        'type' : 'FLOAT',
        'default' : 1,
    },
    {
        'attr' : 'reflection_amount',
        'desc' : "Shows the reflections of the base material",
        'type' : 'FLOAT',
        'default' : 1,
    },
    {
        'attr' : 'refraction_amount',
        'desc' : "Shows the refractions of the base material",
        'type' : 'FLOAT',
        'default' : 1,
    },
    {
        'attr' : 'gi_amount',
        'desc' : "Determines the amount of gi shadows",
        'type' : 'FLOAT',
        'default' : 1,
    },
    {
        'attr' : 'no_gi_on_other_mattes',
        'desc' : "This will cause the material to appear as a matte object in reflections, refractions, GI etc for other matte objects",
        'type' : 'BOOL',
        'default' : True,
    },
    {
        'attr' : 'matte_for_secondary_rays',
        'desc' : "Set this to 1 to make the material act as matte for all secondary rays (reflections and refractions); if set to 2, the material will perform automatic projection mapping of theenvironment map on the matte geometry",
        'type' : 'INT',
        'default' : 0,
    },
    {
        'attr' : 'gi_surface_id',
        'desc' : "If two objects have different GI surface ids, the light cache samples of the two objects will not be blended",
        'type' : 'INT',
        'default' : 0,
    },
    {
        'attr' : 'gi_quality_multiplier',
        'desc' : "A multiplier for GI quality",
        'type' : 'FLOAT',
        'default' : 1,
    },
    {
        'attr' : 'maya_background_shader_compatibility',
        'desc' : "Setting this to true will make the matte alpha opaque so that the alpha of objects behind the matte won't be seen",
        'type' : 'BOOL',
        'default' : False,
    },
    {
        'attr' : 'alpha_contribution_tex',
        'desc' : "Same as alpha_contribution but used for the Maya's useBackground shader which supports textures as alpha contribution",
        'type' : 'FLOAT_TEXTURE',
        'default' : 1,
    },
    {
        'attr' : 'shadow_brightness_tex',
        'desc' : "Same as shadow_brightness but used for the Maya's useBackground shader which supports textures as shadow brightness",
        'type' : 'FLOAT_TEXTURE',
        'default' : 1,
    },
    {
        'attr' : 'reflection_filter_tex',
        'desc' : "",
        'type' : 'TEXTURE',
        'default' : (1, 1, 1),
    },
    {
        'attr' : 'trace_depth',
        'desc' : "The maximum reflection depth (-1 is controlled by the global options)",
        'type' : 'INT',
        'default' : -1,
    },
    {
        'attr' : 'channels',
        'desc' : "Render channels the result of this BRDF will be written to",
        'type' : 'PLUGIN',
        'default' : "",
    },
    {
        'attr' : 'generate_render_elements',
        'desc' : "Setting this to false makes objects to not affect the render elements",
        'type' : 'BOOL',
        'default' : True,
    },
    {
        'attr' : 'reflection_exclude',
        'desc' : "A list of plugins that will be excluded from reflections",
        'type' : 'LIST',
        'default' : "",
    },
    {
        'attr' : 'refraction_exclude',
        'desc' : "A list of plugins that will be excluded from refractions",
        'type' : 'LIST',
        'default' : "",
    },

    {
        'attr' : 'use',
        'name' : "Use",
        'desc' : "Use Wrapper material",
        'type' : 'BOOL',
        'skip' : True,
        'default' : False,
    },
)


def gui(context, layout, MtlWrapper, node):
    contextType = GetContextType(context)
    regionWidth = GetRegionWidthFromContext(context)

    wide_ui = regionWidth > narrowui

    split= layout.split()
    col= split.column()
    col.prop(MtlWrapper, 'generate_gi')
    col.prop(MtlWrapper, 'receive_gi')
    if wide_ui:
        col= split.column()
    col.prop(MtlWrapper, 'generate_caustics')
    col.prop(MtlWrapper, 'receive_caustics')

    split= layout.split()
    col= split.column()
    col.prop(MtlWrapper, 'gi_quality_multiplier')

    split= layout.split()
    col= split.column()
    col.label(text="Matte properties")

    split= layout.split()
    colL= split.column()
    colL.prop(MtlWrapper, 'matte_surface')
    if wide_ui:
        colR= split.column()
    else:
        colR= colL
    colR.prop(MtlWrapper, 'alpha_contribution')
    if MtlWrapper.matte_surface:
        colR.prop(MtlWrapper, 'reflection_amount')
        colR.prop(MtlWrapper, 'refraction_amount')
        colR.prop(MtlWrapper, 'gi_amount')
        colR.prop(MtlWrapper, 'no_gi_on_other_mattes')

        colL.prop(MtlWrapper, 'affect_alpha')
        colL.prop(MtlWrapper, 'shadows')
        if MtlWrapper.shadows:
            colL.prop(MtlWrapper, 'shadow_tint_color')
            colL.prop(MtlWrapper, 'shadow_brightness')

    split= layout.split()
    col= split.column()
    col.label(text="Miscellaneous")

    split= layout.split()
    col= split.column()
    col.prop(MtlWrapper, 'gi_surface_id')
    col.prop(MtlWrapper, 'trace_depth')
    if wide_ui:
        col= split.column()
    col.prop(MtlWrapper, 'matte_for_secondary_rays')
