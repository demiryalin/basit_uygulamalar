#!/usr/bin/python3

import rospy
from basit_uygulamalar.srv import circle_move

class MoveCircleReq():
    def __init__(self):
        rospy.wait_for_service("circle_move_srv")
        try:
            radius = float(input("radius: "))
            circle_service = rospy.ServiceProxy("circle_move_srv", circle_move)
            circle_service(radius)
        except rospy.ServiceException:
            rospy.logwarn("service related error has occured ...")

req = MoveCircleReq()

