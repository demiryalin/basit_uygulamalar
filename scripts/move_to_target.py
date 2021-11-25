#!/usr/bin/python3
import rospy
from geometry_msgs.msg import Twist
from basit_uygulamalar.msg import distance
from nav_msgs.msg import Odometry

i = 0
class move_to_target():
    def __init__(self):

        rospy.init_node("move_forward")
        rospy.Subscriber("odom", Odometry, self.__odomCallback)
        rospy.Subscriber("distance_to_go", distance, self.__distanceCallback)

        self.__target = 0.0
        self.__actual_position = 0.0
        self.__control = True
        pub = rospy.Publisher("cmd_vel", Twist, queue_size=10)
        velo_msg = Twist()
        rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            if self.__control:
                velo_msg.linear.x = 1.5
                velo_msg.linear.y = 1.5
                pub.publish(velo_msg)
            else:
                velo_msg.linear.x = 0.0
                velo_msg.linear.y = 0.0
                pub.publish(velo_msg)
                rospy.loginfo("Reached the target %f", self.__target)
            rate.sleep()

    def __odomCallback(self, data):
        global i
        i+=1
        rospy.loginfo("%f", data.pose.pose.position.x)
        inital_pose = 0.0
        if(i == 1):
            inital_pose = data.pose.pose.position.x

        self.__actual_position = data.pose.pose.position.x - inital_pose
        self.__control = True if (self.__actual_position <= self.__target) is True else False

    def __distanceCallback(self, data):
        self.__target = data.distance

try:
    move = move_to_target()
except rospy.ROSInterruptException:
    rospy.loginfo("rosnode is imterrupted")
