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

import os
import sys

import bpy

import _vray_for_blender

_has_rt = True
try:
    import _vray_for_blender_rt
except:
    _has_rt = False

from .lib import SysUtils
from .    import export


def Init():
    jsonDirpath = os.path.join(SysUtils.GetExporterPath(), "plugins_desc")
    _vray_for_blender.start(jsonDirpath)
    if _has_rt:
        _vray_for_blender_rt.load(jsonDirpath)


def Shutdown():
    _vray_for_blender.free()
    if _has_rt:
        _vray_for_blender_rt.unload()


class VRayRendererBase(bpy.types.RenderEngine):
    def render(self, scene):
        if self.is_preview:
            if scene.render.resolution_x < 64: # Don't render icons
                return

        err = export.RenderScene(self, scene)
        if err is not None:
            self.report({'ERROR'}, err)


class VRayRenderer(VRayRendererBase):
    bl_idname      = 'VRAY_RENDER'
    bl_label       = "V-Ray"
    bl_use_preview =  False


class VRayRendererPreview(VRayRendererBase):
    bl_idname = 'VRAY_RENDER_PREVIEW'
    bl_label  = "V-Ray (With Material Preview)"

    bl_use_preview      =  True
    bl_preview_filepath = SysUtils.GetPreviewBlend()


class VRayRendererRT(VRayRendererBase):
    bl_idname = 'VRAY_RENDER_RT'
    bl_label  = "V-Ray (With Viewport Rendering)"

    bl_use_preview      = True
    bl_preview_filepath = SysUtils.GetPreviewBlend()

    exporter = None

    def debug(self, msg):
        if False:
            sys.stderr.write(msg)
            sys.stderr.write("\n")
            sys.stderr.flush()

    def __init__(self):
        self.debug("VRayRendererRT::__init__()")
        self.exporter = None

    def __del__(self):
        self.debug("VRayRendererRT::__del__()")
        if self.exporter:
            _vray_for_blender_rt.free(self.exporter)

    def update(self, data, scene):
        self.debug("VRayRendererRT::update()")

    def render(self, scene):
        self.debug("VRayRendererRT::render()")
        super(VRayRendererRT, self).render(scene)

    def view_update(self, context):
        self.debug("VRayRendererRT::view_update()")
        if not self.exporter:
            self.exporter = _vray_for_blender_rt.init(context.as_pointer(),
                self.as_pointer(),
                context.blend_data.as_pointer(),
                context.scene.as_pointer(),
                context.region.as_pointer(),
                context.space_data.as_pointer(),
                context.region_data.as_pointer()
            )
            _vray_for_blender_rt.export(self.exporter)

        if self.exporter:
            _vray_for_blender_rt.update(self.exporter)

    def view_draw(self, context):
        self.debug("VRayRendererRT::view_draw()")
        if self.exporter:
            _vray_for_blender_rt.draw(self.exporter,
                context.space_data.as_pointer(),
                context.region_data.as_pointer()
            )


def GetRegClasses():
    reg_classes = [
        VRayRenderer,
        VRayRendererPreview,
    ]
    if _has_rt:
        reg_classes.append(VRayRendererRT)
    return reg_classes


def register():
    for regClass in GetRegClasses():
        bpy.utils.register_class(regClass)


def unregister():
    for regClass in GetRegClasses():
        bpy.utils.unregister_class(regClass)
