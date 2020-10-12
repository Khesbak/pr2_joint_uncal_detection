#!/usr/bin/env python
import rospy
from time import sleep
from sensor_msgs.msg import JointState
from std_msgs.msg import Float64
import numpy as np
import multiprocessing
import sys
import objectpath
import features

import pandas as pd



a=[]
b=[]
c=[]
joint_names=[]
cnt=0

while(cnt<45):
    a.append(cnt)
    c.append(cnt)
    cnt=cnt+1
    joint_names.append("")
cnt=0
while(cnt<48):
    b.append(cnt)
    cnt=cnt+1
joint_names=['fl_caster_rotation_joint', 'fl_caster_l_wheel_joint', 'fl_caster_r_wheel_joint', 'fr_caster_rotation_joint', 'fr_caster_l_wheel_joint', 'fr_caster_r_wheel_joint', 'bl_caster_rotation_joint', 'bl_caster_l_wheel_joint', 'bl_caster_r_wheel_joint', 'br_caster_rotation_joint', 'br_caster_l_wheel_joint', 'br_caster_r_wheel_joint', 'torso_lift_joint', 'torso_lift_motor_screw_joint', 'head_pan_joint', 'head_tilt_joint', 'laser_tilt_mount_joint', 'r_upper_arm_roll_joint', 'r_shoulder_pan_joint', 'r_shoulder_lift_joint', 'r_forearm_roll_joint', 'r_elbow_flex_joint', 'r_wrist_flex_joint', 'r_wrist_roll_joint',  'r_gripper_joint', 'r_gripper_l_finger_joint', 'r_gripper_r_finger_joint', 'r_gripper_r_finger_tip_joint', 'r_gripper_l_finger_tip_joint', 'r_gripper_motor_screw_joint', 'r_gripper_motor_slider_joint',  'l_upper_arm_roll_joint', 'l_shoulder_pan_joint', 'l_shoulder_lift_joint', 'l_forearm_roll_joint',  'l_elbow_flex_joint', 'l_wrist_flex_joint',' l_wrist_roll_joint', 'l_gripper_joint','l_gripper_l_finger_joint',  'l_gripper_r_finger_joint', 'l_gripper_r_finger_tip_joint', 'l_gripper_l_finger_tip_joint',  'l_gripper_motor_screw_joint', 'l_gripper_motor_slider_joint']
#print((joint_names[3]))


class Nodo(object):
    def __init__(self):
        # Params
        self.body_pos = None
        self.giskard_pos = None

        # Node cycle rate (in Hz).
        self.loop_rate = rospy.Rate(10)

        # Publishers
        self.sub=rospy.Subscriber("body/joint_states", JointState, self.body_joint, queue_size=10)
        self.sub=rospy.Subscriber("giskard/joint_states", JointState, self.giskard_joint, queue_size=10)
        

    def body_joint(self, msg):
        self.body_pos=msg.position
    
    def giskard_joint(self, msg1):
        self.giskard_pos=msg1.position


    def start(self):
        rospy.loginfo("In attesa")

        while not rospy.is_shutdown():
            #for ii in xrange(1, 51):
            
            #print(self.body_pos)
            #a=np.array(self.body_pos)
            a1=self.body_pos
            a2= pd.DataFrame(a1)
            a3=(a2.values)
            
            cnt=0
            for i in a3:
                a[cnt]=float(i)
                cnt=cnt+1
            #print("/body/joint_states:")
            #print(a)
            # print("")
            # print("")
            # print("")

            b1=self.giskard_pos
            b2= pd.DataFrame(b1)
            b3=(b2.values)
            cnt=0
            for i in b3:
                b[cnt]=float(i)
                #c[cnt]=a[cnt]-b[cnt]
                cnt=cnt+1
            #print("/giskard/joint_states:")
            #print(b)
            # print("")
            # print("")
            # print("")
            
            cnt=0
            print("The Joints that have difference between body and giskard joint_states are:")
            while(cnt<45):
                c[cnt]=a[cnt]-b[cnt]
                if abs(c[cnt])>1:
                    print(joint_names[cnt],str("   has difference ="),c[cnt])
                    e=3
                    
                cnt=cnt+1
            #print(c)
            print("")
            print("")
            print("")

            self.loop_rate.sleep()
                


if __name__ == '__main__':
    rospy.init_node("nodo1", anonymous=True)
    my_node = Nodo()
    my_node.start()