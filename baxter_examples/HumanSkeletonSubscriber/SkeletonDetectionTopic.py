#!/usr/bin/env python

import rospy
from tf2_msgs.msg import TFMessage

import SkeletonChildFrameId
import human_skeleton

class HumanDetection:

    def __init__(self):
        self.skeleton = human_skeleton.HumanSkeleton()

    def callback(self,msg):
        for item in msg.transforms:
            if item.child_frame_id.find("/cob_body_tracker") != -1:
                #set user
                self.skeleton.set_name(
                    item.child_frame_id[SkeletonChildFrameId.USER_ID_START_POS:SkeletonChildFrameId.USER_ID_END_POS]
                )
                #update joint
                self.skeleton.update_joint(
                    item.child_frame_id[SkeletonChildFrameId.JOINT_START_POS:len(item.child_frame_id)],
                    item.transform.translation.x,
                    item.transform.translation.y,
                    item.transform.translation.z
                )
                self.skeleton.skeleton_info()
    
    def run_detection(self):
        rospy.init_node('subscriber')
        #Subscribe to tf topic
        rospy.Subscriber("/tf",TFMessage, callback)
        rospy.spin() 



                