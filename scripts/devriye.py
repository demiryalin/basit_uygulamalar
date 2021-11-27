#!/usr/bin/python3
import rospy
from geometry_msgs.msg import Twist
def volta():
    rospy.init_node("devriye_node")
    pub = rospy.Publisher("cmd_vel", Twist, queue_size=10)
    velo_msg = Twist()
    robot_velo = 0.25
    volta_uzunluk = rospy.get_param("/VoltaUzunluk")
    volta_sayisi = rospy.get_param("/VoltaSayisi")
    volta_counter = 0

    rospy.loginfo("decriye basladi")
    while volta_counter < volta_sayisi:
        t0 = rospy.Time.now().to_sec()
        yer_degistirme = 0.0
        if volta_counter %2 == 0:
            velo_msg.linear.x = robot_velo
        else:
            velo_msg.linear.x = -robot_velo

        while yer_degistirme < volta_uzunluk:
            pub.publish(velo_msg)
            t1 = rospy.Time.now().to_sec()
            yer_degistirme = robot_velo * (t1-t0)
        velo_msg.linear.x = 0.0
        pub.publish(velo_msg)
        volta_counter +=1
    rospy.loginfo("decriye tamamlandi")
    rospy.is_shutdown()

volta()
