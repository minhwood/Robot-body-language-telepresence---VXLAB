#!/usr/bin/env python

import SkeletonChildFrameId

class Joint:
    def __init__(self,id):
        self.id = id
        self.x = None
        self.y = None
        self.z = None
    
    def update_joint(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    
    def joint_info(self):
        print('{} Joint:\n x: {}\n y: {}\n z: {}\n'.format(self.id, self.x, self.y, self.z))

class HumanSkeleton:

    def __init__(self):
        self.name  = None

        self.head = Joint(SkeletonChildFrameId.HEAD)

        self.right_shoulder = Joint(SkeletonChildFrameId.RIGHT_SHOULDER)
        self.left_shoulder = Joint(SkeletonChildFrameId.LEFT_SHOULDER)

        self.right_elbow = Joint(SkeletonChildFrameId.RIGHT_ELBOW)
        self.left_elbow = Joint(SkeletonChildFrameId.LEFT_ELBOW)

        self.right_hand = Joint(SkeletonChildFrameId.RIGHT_HAND)
        self.left_hand = Joint(SkeletonChildFrameId.LEFT_HAND)

        self.joints = (self.head, 
                        self.right_elbow,self.right_hand,self.right_shoulder,
                        self.left_elbow,self.left_hand,self.left_shoulder)

    def set_name(self,name):
        self.name = name

    def update_joint(self,id,x,y,z):
        for joint in self.joints:
            if joint.id == id:
                joint.update_joint(x,y,z)

    def skeleton_info(self):
        print('{} Skeleton Info:'.format(self.name))
        for joint in self.joints:
            joint.joint_info()
