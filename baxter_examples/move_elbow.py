import rospy
from tf2_msgs.msg import TFMessage
import baxter_interface
#Only apply for right Elbow

# Save the old coordinator of the elbow
class OldCoor:
    y = 0

def callback(msg):
    for item in msg.transforms:
        #find the elbow coodinators
        if item.child_frame_id.find("right_elbow") != -1:
            #Coordinator
            x = round(item.transform.translation.x,4)
            y = round(item.transform.translation.y,4)
            z = round(item.transform.translation.z,4)

            right_limb = baxter_interface.Limb('right')
            right_angles = right_limb.joint_angles()

            #check if the user elbow have been raise up
            if y > OldCoor.y:
                right_angles['right_s1'] += 0.1
            elif y < OldCoor.y:
                right_angles['right_s1'] -= 0.1
            right_limb.move_to_joint_positions(right_angles)
            rospy.loginfo('oldy:{} vs y:{}\n'.format(OldCoor.y,y))
            OldCoor.y = y

def main():
    rospy.init_node('subscriber')
    #Subscribe to tf topic
    rospy.Subscriber("/tf",TFMessage, callback)
    rospy.spin()

if __name__ == '__main__':
    main()
