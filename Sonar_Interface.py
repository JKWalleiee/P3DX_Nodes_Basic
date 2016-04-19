#!/usr/bin/env python
import roslib
import rospy
import geometry_msgs.msg

from sensor_msgs.msg import PointCloud

def pointcloudCb(msg):
     rospy.loginfo("Sonar 1 is %s", msg.points[1])
     rospy.loginfo("Sonar 2 is %s", msg.points[2])
    

if __name__ == "__main__":
    rospy.init_node('pointcloud', anonymous=True) #make node 
    rospy.Subscriber('RosAria/sonar',PointCloud,pointcloudCb)
    rospy.spin()
