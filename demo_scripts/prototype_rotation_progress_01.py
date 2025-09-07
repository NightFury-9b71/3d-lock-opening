import bpy
from math import radians

Lock = bpy.data.objects["Body"]
Lock.animation_data_clear()

Key = bpy.data.objects["KeyHolder"]
Key.animation_data_clear()

### Transformation

bpy.context.scene.frame_set(1)
Lock.location = (0, 0, 1)
Lock.keyframe_insert(data_path="location")

bpy.context.scene.frame_set(2)
Key.location = (0.5, 0, 0.973)
Key.keyframe_insert(data_path="location")


bpy.context.scene.frame_set(89)
Key.location = (0.09, 0, 0.973)
Key.keyframe_insert(data_path="location")


## Rotation
KeyHole = bpy.data.objects["KeyHole"]
KeyHole.show_axis = True
KeyHole.animation_data_clear()

#bpy.context.scene.frame_set(101)
#KeyHole.rotation_euler = (radians(90), radians(0), radians(90))
#KeyHole.keyframe_insert(data_path="rotation_euler")
for angle in range(90, 200):
    bpy.context.scene.frame_set(angle)
    Key.show_axis = True
    Key.rotation_euler = (0, radians(angle), radians(90))
    Key.keyframe_insert(data_path="rotation_euler")
    
    KeyHole.rotation_euler = (radians(90), radians(angle), radians(90))
    KeyHole.keyframe_insert(data_path="rotation_euler")

#bpy.context.scene.frame_set(150)
#KeyHole.rotation_euler = (radians(360), radians(90), 0)
#KeyHole.keyframe_insert(data_path="rotation_euler")

#bpy.context.scene.frame_set(150)
#Key.rotation_euler = (radians(360), radians(90), radians(90))
#Key.keyframe_insert(data_path="rotation_euler")


bpy.context.scene.frame_start = 1
bpy.context.scene.frame_end = 200