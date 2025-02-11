import bpy
import math

# Access the armature
armature_name = "Armature"
armature = bpy.data.objects[armature_name]

# Set the armature to Pose Mode
bpy.context.view_layer.objects.active = armature 
bpy.ops.object.mode_set(mode='POSE')

# Define the bone names for arms, spine, neck, and legs
left_arm_bone_name = "mixamorig9:LeftArm"
right_arm_bone_name = "mixamorig9:RightArm"
left_forearm_bone_name = "mixamorig9:LeftForeArm"
right_forearm_bone_name = "mixamorig9:RightForeArm"
left_hand_bone_name = "mixamorig9:LeftHand"
right_hand_bone_name = "mixamorig9:RightHand"
neck_bone_name = "mixamorig9:Neck"
spine_bone_name = "mixamorig9:Spine"
left_up_leg_bone_name = "mixamorig9:LeftUpLeg"
left_leg_bone_name = "mixamorig9:LeftLeg"
left_foot_bone_name = "mixamorig9:LeftFoot"
right_up_leg_bone_name = "mixamorig9:RightUpLeg"
right_leg_bone_name = "mixamorig9:RightLeg"
right_foot_bone_name = "mixamorig9:RightFoot"

# Access the bones
left_arm_bone = armature.pose.bones[left_arm_bone_name]
right_arm_bone = armature.pose.bones[right_arm_bone_name]
left_forearm_bone = armature.pose.bones[left_forearm_bone_name]
right_forearm_bone = armature.pose.bones[right_forearm_bone_name]
left_hand_bone = armature.pose.bones[left_hand_bone_name]
right_hand_bone = armature.pose.bones[right_hand_bone_name]
neck_bone = armature.pose.bones[neck_bone_name]
spine_bone = armature.pose.bones[spine_bone_name]
left_up_leg_bone = armature.pose.bones[left_up_leg_bone_name]
left_leg_bone = armature.pose.bones[left_leg_bone_name]
left_foot_bone = armature.pose.bones[left_foot_bone_name]
right_up_leg_bone = armature.pose.bones[right_up_leg_bone_name]
right_leg_bone = armature.pose.bones[right_leg_bone_name]
right_foot_bone = armature.pose.bones[right_foot_bone_name]

# Define the fixed rotations for the leg bones
fixed_leg_rotations = {
    left_up_leg_bone: (math.radians(5.0515), math.radians(-3.056), math.radians(2.9263)),
    left_leg_bone: (math.radians(-7.6541), math.radians(-1.0897), math.radians(-0.2849)),
    left_foot_bone: (math.radians(-1.1828), math.radians(8.0416), math.radians(-4.8417)),
    right_up_leg_bone: (math.radians(5.8384), math.radians(5.8961), math.radians(11.388)),
    right_leg_bone: (math.radians(-9.1384), math.radians(0.19186), math.radians(0.29923)),
    right_foot_bone: (math.radians(1.1469), math.radians(-19.704), math.radians(4.7677))
}

# Function to set fixed rotations for the legs
def set_fixed_leg_rotations(frame):
    bpy.context.scene.frame_set(frame)
    for bone, rotation in fixed_leg_rotations.items():
        bone.rotation_euler = rotation
        bone.keyframe_insert(data_path="rotation_euler", frame=frame)

# Frame 1: Initial Position (Arms Down, Neck Neutral, Spine Neutral, Legs Fixed)
bpy.context.scene.frame_set(1)
left_arm_bone.rotation_euler = (math.radians(74.878), math.radians(-0.34683), math.radians(-0.47143))
right_arm_bone.rotation_euler = (math.radians(65.955), math.radians(-0.36212), math.radians(1.1761))
neck_bone.rotation_euler = (math.radians(-3.6162), math.radians(-0.052238), math.radians(0.24291))
spine_bone.rotation_euler = (math.radians(1.2233), math.radians(0.53879), math.radians(1.5196))
left_arm_bone.keyframe_insert(data_path="rotation_euler", frame=1)
right_arm_bone.keyframe_insert(data_path="rotation_euler", frame=1)
neck_bone.keyframe_insert(data_path="rotation_euler", frame=1)
spine_bone.keyframe_insert(data_path="rotation_euler", frame=1)
set_fixed_leg_rotations(1)

# Frame 60: Arms Raised, Neck and Spine Neutral, Legs Fixed
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
set_fixed_leg_rotations(60)

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

# Hold the position of the 180th frame for 20 more frames
bpy.context.scene.frame_set(200)

# Copy the pose from frame 180
left_arm_bone.rotation_euler = (math.radians(-0.81583), math.radians(-0.17929), math.radians(83.767))
right_arm_bone.rotation_euler = (math.radians(0.22223), math.radians(-0.00122), math.radians(-89.647))
left_forearm_bone.rotation_euler = (math.radians(4.8302), math.radians(-0.63979), math.radians(-0.57466))
right_forearm_bone.rotation_euler = (math.radians(3.4149), math.radians(0.44517), math.radians(-0.40367))
left_hand_bone.rotation_euler = (math.radians(-19.682), math.radians(-23.005), math.radians(0.91373))
right_hand_bone.rotation_euler = (math.radians(-16.771), math.radians(2.8743), math.radians(-4.3653))
neck_bone.rotation_euler = (math.radians(-3.6162), math.radians(-0.052238), math.radians(0.24291))
spine_bone.rotation_euler = (math.radians(1.2233), math.radians(0.53879), math.radians(1.5196))

# Insert keyframes for frame 200
left_arm_bone.keyframe_insert(data_path="rotation_euler", frame=200)
right_arm_bone.keyframe_insert(data_path="rotation_euler", frame=200)
left_forearm_bone.keyframe_insert(data_path="rotation_euler", frame=200)
right_forearm_bone.keyframe_insert(data_path="rotation_euler", frame=200)
left_hand_bone.keyframe_insert(data_path="rotation_euler", frame=200)
right_hand_bone.keyframe_insert(data_path="rotation_euler", frame=200)
neck_bone.keyframe_insert(data_path="rotation_euler", frame=200)
spine_bone.keyframe_insert(data_path="rotation_euler", frame=200)

# Frame 240: Arms Fully Lowered
bpy.context.scene.frame_set(240)

# Update arm, forearm, and hand angles for arms lowered position
left_arm_bone.rotation_euler = (math.radians(84.444), math.radians(17.647), math.radians(75.632))
right_arm_bone.rotation_euler = (math.radians(80.706), math.radians(-21.199), math.radians(-73.2199))
left_forearm_bone.rotation_euler = (math.radians(4.8646), math.radians(-0.65938), math.radians(-0.38431))
right_forearm_bone.rotation_euler = (math.radians(4.1132), math.radians(0.89965), math.radians(-4.0124))
left_hand_bone.rotation_euler = (math.radians(-174), math.radians(-80.779), math.radians(161.11))
right_hand_bone.rotation_euler = (math.radians(-53.732), math.radians(81.064), math.radians(-39.356))

# Insert keyframes for frame 240
left_arm_bone.keyframe_insert(data_path="rotation_euler", frame=240)
right_arm_bone.keyframe_insert(data_path="rotation_euler", frame=240)
left_forearm_bone.keyframe_insert(data_path="rotation_euler", frame=240)
right_forearm_bone.keyframe_insert(data_path="rotation_euler", frame=240)
left_hand_bone.keyframe_insert(data_path="rotation_euler", frame=240)
right_hand_bone.keyframe_insert(data_path="rotation_euler", frame=240)

# Adjust the timeline to end at frame 240
bpy.context.scene.frame_end = 240

print("Animation updated: Arms smoothly lowered over 40 frames (200 to 240).")

# Exit Pose Mode
bpy.ops.object.mode_set(mode='OBJECT')

print("Final animation sequence created: Raise arms, hold, bend forward, return, and lower arms.")
