#!/usr/bin/python3

import rospy
from geometry_msgs.msg import Twist
from basit_uygulamalar.srv import circle_move

class MoveCircle():
    def __init__(self):
        rospy.init_node("circle_move_server_node")
        self.pub = rospy.Publisher("cmd_vel", Twist, queue_size=10)
        rospy.Service("circle_move_srv", circle_move, self.service_func)
        rospy.spin()

    def service_func(self, request):
        vel_msg = Twist()
        vel_msg.linear.x  = 0.5
        vel_msg.angular.z = vel_msg.linear.x / request.radius
        rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            self.pub.publish(vel_msg)
            rate.sleep()

service = MoveCircle()