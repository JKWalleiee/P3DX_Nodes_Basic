#!/usr/bin/env python
import roslib
import rospy
import geometry_msgs.msg

from sensor_msgs.msg import LaserScan

def pointcloudCb(msg):
     rospy.loginfo("Range minime of Laser is %s", msg.range_min)
     rospy.loginfo("Range max of Laser is %s", msg.range_max)
     
    

if __name__ == "__main__":
    rospy.init_node('LaseScan', anonymous=True) #make node 
    rospy.Subscriber('scan',LaserScan,pointcloudCb)
    rospy.spin()

