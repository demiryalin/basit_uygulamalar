#!/usr/bin/python3

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class LaserData():
    def __init__(self):
        rospy.init_node("laser_node")
        rospy.Subscriber("scan", LaserScan, self.__laserCallback)
        self.__pub = rospy.Publisher("cmd_vel", Twist, queue_size=10)
        self.__vel_msg = Twist()
        rospy.spin()

    def __laserCallback(self, scan_data):
        sol_on = list(scan_data.ranges[0:9])
        sag_on = list(scan_data.ranges[350:359])
        on   = sol_on + sag_on
        sol  = list(scan_data.ranges[80:100])
        sag  = list(scan_data.ranges[260:280])
        arka = list(scan_data.ranges [170:190])

        min_on   = min(on)
        min_sol  = min(sol)
        min_sag  = min(sag)
        min_arka = min(arka)

        if min_on < 1.0:
            self.__vel_msg.linear.x = 0.0
        else:
            self.__vel_msg.linear.x = 0.25
        self.__pub.publish(self.__vel_msg)


obj = LaserData()