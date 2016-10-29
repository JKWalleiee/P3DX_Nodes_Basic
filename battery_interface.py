#!/usr/bin/env python
import roslib
import rospy
import geometry_msgs.msg

from std_msgs.msg import String
from std_msgs.msg import Float64


globvar = Float64()

def talker():
     pub = rospy.Publisher('mybattery', Float64, queue_size=10)
     rospy.init_node('oodometry', anonymous=True) #make node 
     rospy.Subscriber('/RosAria/battery_voltage',Float64,batteryCb)
     rate = rospy.Rate(10)
     while not rospy.is_shutdown():
          if globvar < 11.0:
               hello = "La cosa va bien"
               pub.publish(globvar)
               rate.sleep()

def batteryCb(msg):
     #rospy.loginfo("X is %s", msg)
     if msg.data < 11.0:
          global globvar
          globvar = msg.data
         #print "position x" + msg.pose.pose.position.x
          #pub.publish(msg)

if __name__ == "__main__":
     try:
          talker()
     except rospy.ROSInterruptException:
          pass
    
