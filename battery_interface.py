#!/usr/bin/env python
import roslib
import rospy
import geometry_msgs.msg

from std_msgs.msg import String
from std_msgs.msg import Float64


globvar = 13.0 


def talker(bateryAux, cont):
     pub = rospy.Publisher('mybattery', Float64, queue_size=10)
     rospy.init_node('oodometry', anonymous=True) #make node 
     rospy.Subscriber('/RosAria/battery_voltage',Float64,batteryCb)
     rate = rospy.Rate(10)
     while not rospy.is_shutdown():
          bateryAux += globvar;
          cont += 1
          if cont == 10:
               batery = bateryAux/10
               cont = 0
               bateryAux = 0
               if batery < 11.0:
                    pub.publish(Float64(batery))
          rate.sleep()

def batteryCb(msg):
     global globvar
     globvar = msg.data
         #print "position x" + msg.pose.pose.position.x
          #pub.publish(msg)

if __name__ == "__main__":
     bateryAux = 0.0
     cont = 0
     try:
          talker(bateryAux, cont)
     except rospy.ROSInterruptException:
          pass
    
