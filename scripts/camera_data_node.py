#!/usr/bin/python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class RobotCamera():
    def __init__(self):
        rospy.init_node("camera_node")
        rospy.Subscriber("camera/rgb/image_raw", Image, self.__ImageCallback)
        self.__bridge = CvBridge()
        rospy.spin()

    def __ImageCallback(self, image_data):
        foto = self.__bridge.imgmsg_to_cv2(image_data, "bgr8")
        cv2.imshow("Robot Image", foto)
        cv2.waitKey(1)

obj = RobotCamera()
