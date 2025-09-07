import bpy
import math
from mathutils import Matrix

obj = bpy.data.objects["KeyHole"]
obj.animation_data_clear()

bpy.context.scene.frame_set(1)
rotation_matrix = Matrix.Rotation(math.radians(90), 4, 'Y')
obj.matrix_world = rotation_matrix
obj.keyframe_insert(data_path="rotation_euler")

for angle in range(2, 180):
    bpy.context.scene.frame_set(angle)
    rotation_matrix = Matrix.Rotation(math.radians(angle), 4, 'X')
    obj.matrix_world = rotation_matrix
    obj.keyframe_insert(data_path="rotation_euler")

bpy.context.scene.frame_start=1
bpy.context.scene.frame_end=180
