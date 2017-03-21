#!/usr/bin/env python

import sys
import rospy
import time 
import matplotlib.pyplot as plot 
from beginner_tutorials.srv import *

def time_service_client(time1):
	rospy.wait_for_service('time_service')
	try:
		time_service = rospy.ServiceProxy('time_service', TimeService)
		resp1 = time_service(time1)
		return resp1.difference 
	except rospy.ServiceException, e:
		print "Service call failed: %s"%e

def usage():
	return "%s auto generate time1 (no args)"%sys.argv[0]
	
def make_histogram(histogramData):
	plot.hist(histogramData, bins=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25])
	plot.title("Client-Server Histogram")
	plot.xlabel("Time Difference (Milliseconds)")
	plot.ylabel("Frequency (out of 350)")
	plot.show()	
	
def main():
	if len(sys.argv) == 1:
		time1 = int(round(time.time() * 1000))
	else:
		print usage()
		sys.exit(1)
		
	print "Requested at time %s"%(time1)
	time_diff = time_service_client(time1)
	print "Service completed in %s ms "%(time_diff)		
	
	histogram = []
	histogram.append(time_diff)
	
	for i in range(1, 350):
		time1 = int(round(time.time() * 1000))		
		time_diff = time_service_client(time1)
		histogram.append(time_diff)
		#print "Service completed in %s ms "%(time_diff)		
	
	make_histogram(histogram)

if __name__ == "__main__":
	main()
	
