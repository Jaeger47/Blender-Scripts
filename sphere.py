
import bpy

# for demo it creates a sphere if it doesn't exist,
# but this can be any existing named object.
if not 'Sphere' in bpy.data.objects:
	bpy.ops.mesh.primitive_uv_sphere_add()

# positions to be keyed
new_pos = (0,3,1), (4,1,6), (1,8,1)

mesh_obj = bpy.data.objects["Sphere"]

frame_num = 0

#looping through the positions
for position in new_pos:
    bpy.context.scene.frame_set(frame_num)
    mesh_obj.location = position
    mesh_obj.keyframe_insert(data_path="location", index = -1)
    frame_num +=20
