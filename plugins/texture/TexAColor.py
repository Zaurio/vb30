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

from vb30.lib import ExportUtils, AttributeUtils


TYPE = 'TEXTURE'
ID   = 'TexAColor'
NAME = 'Color'
DESC = "Just a color"

PluginParams = (
    {
        'attr'    : 'texture',
        'name'    : "Color",
        'desc'    : "Color",
        'type'    : 'TEXTURE',
        'default' :  (1,1,1,1),
    },
    {
        'attr' : 'uvwgen',
        'name' : "Mapping",
        'desc' : "Mapping generator",
        'type' : 'UVWGEN',
        'options' : 'HIDDEN',
        'default' : "",
    },
)
