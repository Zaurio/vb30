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
ID   = 'MtlStreakFade'
NAME = 'Streak Fade'
DESC = ""

PluginParams = (
    {
        'attr' : 'base_mtl',
        'desc' : "Base material",
        'type' : 'MATERIAL',
        'default' : "",
    },
    {
        'attr' : 'fade',
        'desc' : "1.0f - no fade, < 1.0f - fade",
        'type' : 'FLOAT',
        'default' : 1,
    },
)
