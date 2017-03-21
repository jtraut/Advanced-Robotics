#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import matplotlib.pyplot as plot 

pub_time = "0"
sub_time = "0"

def callback(data):
	globals().update(pub_time = "%s" % data.data, sub_time = "%s" % rospy.Time.now())
	rospy.loginfo(rospy.get_caller_id() + ' topic published at %s recieved at %s', data.data, sub_time)


def sub_topic():
	histogram = []
	rospy.init_node('subscriber')

	rospy.Subscriber('topic', String, callback)
	rate = rospy.Rate(10)
	
	while len(histogram) < 350 and not rospy.is_shutdown():
		ptime = float(pub_time)
		stime = float(sub_time)
		histogram.append((stime - ptime) / 1000000)
		rate.sleep()
	
	if len(histogram) >= 350:
		return histogram
			
	rospy.spin()


def make_histogram(histogramData):
	plot.hist(histogramData, bins=[0,1,2,3,4,5,6,7,8,9,10])
	plot.title("Publisher-Subscriber Histogram")
	plot.xlabel("Time Difference (Milliseconds)")
	plot.ylabel("Frequency (out of 350)")
	plot.show()
	

def main():
	
	dataSet = sub_topic() 
	make_histogram(dataSet)
	
if __name__ == '__main__':
    main()
