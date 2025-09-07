import bpy
from math import radians

Lock = bpy.data.objects["Body"]
Lock.animation_data_clear()

Key = bpy.data.objects["KeyHolder"]
Key.animation_data_clear()

## Transformation

bpy.context.scene.frame_set(1)
Lock.location = (0, 0, 1)
Lock.keyframe_insert(data_path="location")

bpy.context.scene.frame_set(2)
Key.location = (0.5, 0, 0.973)
Key.keyframe_insert(data_path="location")


bpy.context.scene.frame_set(100)
Key.location = (0.09, 0, 0.973)
Key.keyframe_insert(data_path="location")


## Rotation
KeyHole = bpy.data.objects["KeyHole"]
KeyHole.animation_data_clear()

bpy.context.scene.frame_set(101)
KeyHole.rotation_euler = (0, radians(90), 0)
KeyHole.keyframe_insert(data_path="rotation_euler")

bpy.context.scene.frame_set(101)
Key.rotation_euler = (0, radians(90), radians(90))
Key.keyframe_insert(data_path="rotation_euler")

bpy.context.scene.frame_set(150)
KeyHole.rotation_euler = (radians(300), radians(90), 0)
KeyHole.keyframe_insert(data_path="rotation_euler")

#bpy.context.scene.frame_set(150)
#Key.rotation_euler = (radians(360), radians(90), radians(90))
#Key.keyframe_insert(data_path="rotation_euler")


bpy.context.scene.frame_start = 1
bpy.context.scene.frame_end = 150