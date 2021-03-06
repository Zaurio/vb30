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


TYPE = 'MATERIAL'
ID   = 'MtlRenderStats'
NAME = 'Render Stats'
DESC = ""

PluginParams = (
    {
        'attr' : 'base_mtl',
        'desc' : "Base material",
        'type' : 'MATERIAL',
        'default' : "",
    },
    {
        'attr' : 'camera_visibility',
        'desc' : "",
        'type' : 'BOOL',
        'default' : True,
    },
    {
        'attr' : 'reflections_visibility',
        'desc' : "",
        'type' : 'BOOL',
        'default' : True,
    },
    {
        'attr' : 'refractions_visibility',
        'desc' : "",
        'type' : 'BOOL',
        'default' : True,
    },
    {
        'attr' : 'gi_visibility',
        'desc' : "",
        'type' : 'BOOL',
        'default' : True,
    },
    {
        'attr' : 'shadows_visibility',
        'desc' : "",
        'type' : 'BOOL',
        'default' : True,
    },
    {
        'attr' : 'visibility',
        'desc' : "Overall visibility",
        'type' : 'BOOL',
        'default' : True,
    },

    {
        'attr' : 'use',
        'name' : "Use",
        'desc' : "Use Render Stats material",
        'type' : 'BOOL',
        'skip' : True,
        'default' : False,
    },
)


def nodeDraw(context, layout, MtlRenderStats):
    layout.prop(MtlRenderStats, 'visibility', text="Primary Visibility")
    layout.label(text="Visible to:")
    layout.prop(MtlRenderStats, 'camera_visibility', text="Camera")
    layout.prop(MtlRenderStats, 'gi_visibility', text="GI")
    layout.prop(MtlRenderStats, 'shadows_visibility', text="Shadows")
    layout.prop(MtlRenderStats, 'reflections_visibility', text="Reflections")
    layout.prop(MtlRenderStats, 'refractions_visibility', text="Refractions")
