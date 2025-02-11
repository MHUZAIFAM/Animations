#Raise arms, bend forward, and come back, arms have not yet been put down, leg position is out of place
import bpy
import math

# Access the armature
armature_name = "Armature"
armature = bpy.data.objects[armature_name]

# Set the armature to Pose Mode
bpy.context.view_layer.objects.active = armature
bpy.ops.object.mode_set(mode='POSE')

# Define the bone names
left_arm_bone_name = "mixamorig9:LeftArm"
right_arm_bone_name = "mixamorig9:RightArm"
left_forearm_bone_name = "mixamorig9:LeftForeArm"
right_forearm_bone_name = "mixamorig9:RightForeArm"
left_hand_bone_name = "mixamorig9:LeftHand"
right_hand_bone_name = "mixamorig9:RightHand"
neck_bone_name = "mixamorig9:Neck"
spine_bone_name = "mixamorig9:Spine"

# Access the bones
left_arm_bone = armature.pose.bones[left_arm_bone_name]
right_arm_bone = armature.pose.bones[right_arm_bone_name]
left_forearm_bone = armature.pose.bones[left_forearm_bone_name]
right_forearm_bone = armature.pose.bones[right_forearm_bone_name]
left_hand_bone = armature.pose.bones[left_hand_bone_name]
right_hand_bone = armature.pose.bones[right_hand_bone_name]
neck_bone = armature.pose.bones[neck_bone_name]
spine_bone = armature.pose.bones[spine_bone_name]

# Frame 1: Initial Position (Arms Down, Neck Neutral, Spine Neutral)
bpy.context.scene.frame_set(1)
left_arm_bone.rotation_euler = (math.radians(74.878), math.radians(-0.34683), math.radians(-0.47143))
right_arm_bone.rotation_euler = (math.radians(65.955), math.radians(-0.36212), math.radians(1.1761))
neck_bone.rotation_euler = (math.radians(-3.6162), math.radians(-0.052238), math.radians(0.24291))
spine_bone.rotation_euler = (math.radians(1.2233), math.radians(0.53879), math.radians(1.5196))
left_arm_bone.keyframe_insert(data_path="rotation_euler", frame=1)
right_arm_bone.keyframe_insert(data_path="rotation_euler", frame=1)
neck_bone.keyframe_insert(data_path="rotation_euler", frame=1)
spine_bone.keyframe_insert(data_path="rotation_euler", frame=1)

# Frame 60: Arms Raised, Neck and Spine Neutral
bpy.context.scene.frame_set(60)
left_arm_bone.rotation_euler = (math.radians(-0.81583), math.radians(-0.17929), math.radians(83.767))
right_arm_bone.rotation_euler = (math.radians(0.22223), math.radians(-0.00122), math.radians(-89.647))
left_forearm_bone.rotation_euler = (math.radians(4.8302), math.radians(-0.63979), math.radians(-0.57466))
right_forearm_bone.rotation_euler = (math.radians(3.4149), math.radians(0.44517), math.radians(-0.40367))
left_hand_bone.rotation_euler = (math.radians(-19.682), math.radians(-23.005), math.radians(0.91373))
right_hand_bone.rotation_euler = (math.radians(-16.771), math.radians(2.8743), math.radians(-4.3653))
neck_bone.rotation_euler = (math.radians(-3.6162), math.radians(-0.052238), math.radians(0.24291))
spine_bone.rotation_euler = (math.radians(1.2233), math.radians(0.53879), math.radians(1.5196))
left_arm_bone.keyframe_insert(data_path="rotation_euler", frame=60)
right_arm_bone.keyframe_insert(data_path="rotation_euler", frame=60)
left_forearm_bone.keyframe_insert(data_path="rotation_euler", frame=60)
right_forearm_bone.keyframe_insert(data_path="rotation_euler", frame=60)
left_hand_bone.keyframe_insert(data_path="rotation_euler", frame=60)
right_hand_bone.keyframe_insert(data_path="rotation_euler", frame=60)
neck_bone.keyframe_insert(data_path="rotation_euler", frame=60)
spine_bone.keyframe_insert(data_path="rotation_euler", frame=60)

# Frame 80: Hold Raised Position, Neck and Spine Neutral
bpy.context.scene.frame_set(80)
left_arm_bone.keyframe_insert(data_path="rotation_euler", frame=80)
right_arm_bone.keyframe_insert(data_path="rotation_euler", frame=80)
left_forearm_bone.keyframe_insert(data_path="rotation_euler", frame=80)
right_forearm_bone.keyframe_insert(data_path="rotation_euler", frame=80)
left_hand_bone.keyframe_insert(data_path="rotation_euler", frame=80)
right_hand_bone.keyframe_insert(data_path="rotation_euler", frame=80)
neck_bone.rotation_euler = (math.radians(-3.6162), math.radians(-0.052238), math.radians(0.24291))
spine_bone.rotation_euler = (math.radians(1.2233), math.radians(0.53879), math.radians(1.5196))
neck_bone.keyframe_insert(data_path="rotation_euler", frame=80)
spine_bone.keyframe_insert(data_path="rotation_euler", frame=80)

# Frame 120: Bend Forward, Adjust Neck, Spine, and Arms
bpy.context.scene.frame_set(120)
left_arm_bone.rotation_euler = (math.radians(-56.527), math.radians(4.7927), math.radians(92.276))
right_arm_bone.rotation_euler = (math.radians(-53.728), math.radians(1.6757), math.radians(-111.1))
neck_bone.rotation_euler = (math.radians(-35.52), math.radians(7.2719), math.radians(8.1611))
spine_bone.rotation_euler = (math.radians(60.539), math.radians(3.9663), math.radians(-1.0038))
left_arm_bone.keyframe_insert(data_path="rotation_euler", frame=120)
right_arm_bone.keyframe_insert(data_path="rotation_euler", frame=120)
neck_bone.keyframe_insert(data_path="rotation_euler", frame=120)
spine_bone.keyframe_insert(data_path="rotation_euler", frame=120)

# Frame 140: Hold Bent Position
bpy.context.scene.frame_set(140)
left_arm_bone.rotation_euler = (math.radians(-56.527), math.radians(4.7927), math.radians(92.276))
right_arm_bone.rotation_euler = (math.radians(-53.728), math.radians(1.6757), math.radians(-111.1))
neck_bone.rotation_euler = (math.radians(-35.52), math.radians(7.2719), math.radians(8.1611))
spine_bone.rotation_euler = (math.radians(60.539), math.radians(3.9663), math.radians(-1.0038))
left_arm_bone.keyframe_insert(data_path="rotation_euler", frame=140)
right_arm_bone.keyframe_insert(data_path="rotation_euler", frame=140)
neck_bone.keyframe_insert(data_path="rotation_euler", frame=140)
spine_bone.keyframe_insert(data_path="rotation_euler", frame=140)

# Frame 180: Return to Raised Position, Neck and Spine Neutral
bpy.context.scene.frame_set(180)
left_arm_bone.rotation_euler = (math.radians(-0.81583), math.radians(-0.17929), math.radians(83.767))
right_arm_bone.rotation_euler = (math.radians(0.22223), math.radians(-0.00122), math.radians(-89.647))
left_forearm_bone.rotation_euler = (math.radians(4.8302), math.radians(-0.63979), math.radians(-0.57466))
right_forearm_bone.rotation_euler = (math.radians(3.4149), math.radians(0.44517), math.radians(-0.40367))
left_hand_bone.rotation_euler = (math.radians(-19.682), math.radians(-23.005), math.radians(0.91373))
right_hand_bone.rotation_euler = (math.radians(-16.771), math.radians(2.8743), math.radians(-4.3653))
neck_bone.rotation_euler = (math.radians(-3.6162), math.radians(-0.052238), math.radians(0.24291))
spine_bone.rotation_euler = (math.radians(1.2233), math.radians(0.53879), math.radians(1.5196))
left_arm_bone.keyframe_insert(data_path="rotation_euler", frame=180)
right_arm_bone.keyframe_insert(data_path="rotation_euler", frame=180)
left_forearm_bone.keyframe_insert(data_path="rotation_euler", frame=180)
right_forearm_bone.keyframe_insert(data_path="rotation_euler", frame=180)
left_hand_bone.keyframe_insert(data_path="rotation_euler", frame=180)
right_hand_bone.keyframe_insert(data_path="rotation_euler", frame=180)
neck_bone.keyframe_insert(data_path="rotation_euler", frame=180)
spine_bone.keyframe_insert(data_path="rotation_euler", frame=180)

# Adjust Timeline
bpy.context.scene.frame_end = 180

print("Animation updated: Transition back to raised position at frame 180.")


# Exit Pose Mode
bpy.ops.object.mode_set(mode='OBJECT')

print("Animation created: Arms raised, hold position, bend forward with spine and neck animation.")
