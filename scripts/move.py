#!/usr/bin/python3
import rospy
from geometry_msgs.msg import Twist
import numpy as np

def move():
    rospy.init_node("move_forward")
    pub = rospy.Publisher("cmd_vel", Twist, queue_size=10)
    velo_msg = Twist()
    velo_msg.linear.x = 0.5
    velo_msg.linear.y = 0.5
    velo_msg.linear.z = 0.0

    delta_d = 5.0
    d = 0.0
    t0 = rospy.Time.now().to_sec()
    while(d < delta_d):
        pub.publish(velo_msg)
        t1 = rospy.Time.now().to_sec()
        d = np.sqrt(velo_msg.linear.x**2 +velo_msg.linear.y **2)*(t1-t0)

    velo_msg.linear.x = 0.0
    velo_msg.linear.y = 0.0
    pub.publish(velo_msg)
    rospy.loginfo("Target reached")
    d = 0.0

move()