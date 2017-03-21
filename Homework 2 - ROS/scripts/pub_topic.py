#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def pub_topic():
	pub = rospy.Publisher('topic', String, queue_size=1)
	rospy.init_node('publisher')
	rate = rospy.Rate(10) # 10hz
	i = 0
	while not rospy.is_shutdown() and i < 400:
		topic_time = "%s" % rospy.Time.now()
		rospy.loginfo(rospy.get_caller_id() + " sent at: %s", topic_time)
		pub.publish(topic_time)
		i += 1
		rate.sleep()

if __name__ == '__main__':
    try:
        pub_topic()
    except rospy.ROSInterruptException:
        pass
