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

from ..sockets import AddInput, AddOutput
from ..operators import sockets as SocketOperators


PluginParams = (
    {
        'attr' : 'mtlid_gen',
        'desc' : "An integer texture that generates material ids; if not present, neither mtlid_gen_float is present then surface material id will be used",
        'type' : 'INT_TEXTURE',
        'default' : 1,
    },
    {
        'attr' : 'mtlid_gen_float',
        'desc' : "A float texture that generates material ids; if not present, neither mtlid_gen is present then surface material id will be used",
        'type' : 'FLOAT_TEXTURE',
        'default' : 1.0,
    },
    {
        'attr' : 'wrap_id',
        'desc' : "",
        'type' : 'BOOL',
        'default' : False,
    },
)


class VRaySocketMtlMulti(bpy.types.NodeSocket):
    bl_idname = 'VRaySocketMtlMulti'
    bl_label  = 'MtlMulti Socket'

    vray_attr = bpy.props.StringProperty(
        name = "V-Ray Attribute",
        description = "V-Ray plugin attribute name",
        options = {'HIDDEN'},
        default = ""
    )

    value = bpy.props.IntProperty(
        name = "ID",
        description = "ID",
    )

    def draw(self, context, layout, node, text):
        layout.prop(self, 'value', text="")

    def draw_color(self, context, node):
        return (1.000, 0.468, 0.087, 1.000)


class VRayNodeMtlMultiAddSocket(SocketOperators.VRayNodeAddCustomSocket, bpy.types.Operator):
    bl_idname      = 'vray.node_add_mtlmulti_sockets'
    bl_label       = "Add MtlMulti Socket"
    bl_description = "Adds MtlMulti sockets"

    def __init__(self):
        self.vray_socket_type = 'VRaySocketMtlMulti'
        self.vray_socket_name = "Material"

    def set_value(self, nodeSock, value):
        nodeSock.value = value


class VRayNodeTexLayeredDelSocket(SocketOperators.VRayNodeDelCustomSocket, bpy.types.Operator):
    bl_idname      = 'vray.node_del_mtlmulti_sockets'
    bl_label       = "Remove MtlMulti Socket"
    bl_description = "Removes MtlMulti socket (only not linked sockets will be removed)"

    def __init__(self):
        self.vray_socket_type = 'VRaySocketMtlMulti'
        self.vray_socket_name = "Material"



class VRayNodeMtlMulti(bpy.types.Node):
    bl_idname = 'VRayNodeMtlMulti'
    bl_label  = 'Multi ID'
    bl_icon   = 'MATERIAL'

    vray_type   = 'MATERIAL'
    vray_plugin = 'MtlMulti'

    wrap_id = bpy.props.BoolProperty(
        name        = "Wrap ID",
        description = "Wrap the material ID's to the largest specified ID for the material",
        default     =  False
    )

    def init(self, context):
        AddInput(self, 'VRaySocketIntNoValue',   "Int Gen.",   'mtlid_gen',       1)
        AddInput(self, 'VRaySocketFloatNoValue', "Float Gen.", 'mtlid_gen_float', 1.0)

        for i in range(2):
            humanIndex = i
            texSockName = "Material %i" % humanIndex
            AddInput(self, 'VRaySocketMtlMulti', texSockName, default=humanIndex)

        AddOutput(self, 'VRaySocketMtl', "Material")

    def draw_buttons(self, context, layout):
        split = layout.split()
        col = split.column()
        col.prop(self, 'wrap_id')

        split = layout.split()
        row = split.row(align=True)
        row.operator('vray.node_add_mtlmulti_sockets', icon="ZOOMIN", text="Add")
        row.operator('vray.node_del_mtlmulti_sockets', icon="ZOOMOUT", text="")


def GetRegClasses():
    return (
        VRaySocketMtlMulti,
        VRayNodeMtlMultiAddSocket,
        VRayNodeTexLayeredDelSocket,
        VRayNodeMtlMulti,
   )


def register():
    for regClass in GetRegClasses():
        bpy.utils.register_class(regClass)


def unregister():
    for regClass in GetRegClasses():
        bpy.utils.unregister_class(regClass)
