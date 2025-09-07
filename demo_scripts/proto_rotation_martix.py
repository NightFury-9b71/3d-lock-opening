import bpy
import math
from mathutils import Matrix

obj = bpy.data.objects["Cylinder"]
obj.animation_data_clear()


for angle in range(1, 180):
    bpy.context.scene.frame_set(angle)
    rotation_matrix = Matrix.Rotation(math.radians(angle), 4, 'Z')
    obj.matrix_world = rotation_matrix
    obj.keyframe_insert(data_path="rotation_euler")

bpy.context.scene.frame_start=1
bpy.context.scene.frame_end=180
