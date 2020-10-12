# PR2 joint states difference detection between giskard and robot actual joint values

- Run the PR2 normally to publish both (/body/joint_states) and (/giskard/joint_states) topics and then run this python code.

- The output of the code should be similar to:

  The Joints that have difference between body and giskard joint_states are:
  
     ('l_upper_arm_roll_joint', '   has difference =', 1.308927187451011)
     
     ('l_shoulder_lift_joint', '   has difference =', -1.0947722246832159)



