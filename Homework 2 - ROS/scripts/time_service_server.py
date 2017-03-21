#!/usr/bin/env python

import rospy
import time
from beginner_tutorials.srv import *

def handle_time_service(req):
	time2 = int(round(time.time() * 1000))
	print "Returning [%s - %s = %sms]"%(time2, req.time1, (time2 - req.time1))
	return TimeServiceResponse(time2 - req.time1)

def time_service_server():
	rospy.init_node('time_service_server')
	s = rospy.Service('time_service', TimeService, handle_time_service)
	print "Ready to compute time difference in server requests."
	rospy.spin()

if __name__ == "__main__":
	time_service_server()
