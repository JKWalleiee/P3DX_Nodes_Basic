#!/usr/bin/env python
import roslib
import rospy
import geometry_msgs.msg

from nav_msgs.msg import Odometry

def odometryCb(msg):
     rospy.loginfo("X is %s", msg.pose.pose.position.x)
     rospy.loginfo("Y is %s", msg.pose.pose.position.y)
    #print "position x" + msg.pose.pose.position.x

if __name__ == "__main__":
    rospy.init_node('oodometry', anonymous=True) #make node 
    rospy.Subscriber('RosAria/pose',Odometry,odometryCb)
    rospy.spin()
