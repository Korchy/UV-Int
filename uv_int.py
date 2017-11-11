import bpy
import sys


class UV_int_separate(bpy.types.Operator):
    bl_idname = 'uv_int.separate_meshloops'
    bl_label = 'UV-Int: Separate'
    bl_description = 'Separate MeshUVLoops'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if bpy.context.active_object:
            bpy.ops.object.mode_set(mode = 'OBJECT')
            meshdata = bpy.context.active_object.data
            for polygon in meshdata.polygons:
                polygondata = ()
                for i in polygon.loop_indices:
                    polygonvert = meshdata.uv_layers.active.data[i].uv[:]  # Vector -> tuple
                    polygondata += polygonvert,
                polygoncenter = sys.modules[modulesNames['Polygon']].Polygon.centroid(polygondata)
                for i in polygon.loop_indices:
                    if meshdata.uv_layers.active:
                        meshuvloop = meshdata.uv_layers.active.data[i]
                        if meshuvloop.select:
                            moveto = (meshuvloop.uv - polygoncenter) * 0.8 + polygoncenter
                            meshuvloop.uv.x = moveto.x
                            meshuvloop.uv.y = moveto.y
            bpy.ops.object.mode_set(mode = 'EDIT')
        return {'FINISHED'}


class UV_int_weld(bpy.types.Operator):
    bl_idname = 'uv_int.weld_meshloops'
    bl_label = 'UV-Int: Weld'
    bl_description = 'Weld MeshUVLoops'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.uv.weld()
        return {'FINISHED'}


def register():
    bpy.utils.register_class(UV_int_separate)
    bpy.utils.register_class(UV_int_weld)


def unregister():
    bpy.utils.unregister_class(UV_int_weld)
    bpy.utils.unregister_class(UV_int_separate)
