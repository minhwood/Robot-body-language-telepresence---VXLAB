#!/usr/bin/env python

import rospy
from tf2_msgs.msg import TFMessage

def callback(msg):
    #check each item of msg if it is about body tracker
    for item in msg.transforms:
        if item.child_frame_id.find("cob") != -1:
            #Reference of the joint
            ref = item.child_frame_id
            #Coordinate of the joint
            x = item.transform.translation.x
            y = item.transform.translation.y
            z = item.transform.translation.z
            rospy.loginfo('Reference:{}'.format(ref))
            rospy.loginfo('Coordinate:\nx:{}\ny:{}\nz:{}\n'.format(x,y,z))

def main():
    rospy.init_node('subscriber')
    #Subscribe to tf topic
    rospy.Subscriber("/tf",TFMessage, callback)
    rospy.spin()

if __name__ == '__main__':
    main()
