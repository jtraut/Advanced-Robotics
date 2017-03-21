#CSCI 4302 Advanced Robotics 
#Homework 3
#Apply kalman filter for state estimate on IMU data 

import math
import numpy as np
from pylab import * 


def euler_angle_update(roll, pitch, yaw, time1, time2, prevAngle):
	phi = prevAngle[0]
	theta = prevAngle[1]
	psi = prevAngle[2]
	
	filterMatrix = np.matrix([(1, math.sin(phi)*math.tan(theta), math.cos(phi)*math.tan(theta)),
					(0, math.cos(phi), -1*math.sin(phi)),
					(0, math.sin(phi)/math.cos(theta), math.cos(phi)/math.cos(theta))])

	dataVec = np.array([[roll], [pitch], [yaw]])
	
	dt = time2 - time1
	
	return prevAngle + filterMatrix * dataVec * dt

def main():
	data = []
	times = []
	phi = []
	theta = []
	psi = []	
	eulerAngle = {}
	#semi-cheating the start time for gladiator 
	dt = 216.155296131 - 216.154285706
	prevTime = 216.154285706 - dt
	prevAngle = np.array([[0], [0], [0]])
	
	with open('lab_run_ninja_imu_data/gyro.txt', 'r') as mag, open('lab_run_ninja_imu_data/timestamp.txt', 'r') as timestamp:
			for state, time in zip(mag, timestamp):
				data.append(state[0:-1] + ',' + time) 
				
	for i in range (0,len(data)):
		line = data[i].split(",")
		roll = float(line[0])
		pitch = float(line[1])
		yaw = float(line[2])
		
		time1 = prevTime
		time2 = float(line[3])
		
		times.append(time2) 
		
		eulerAngle[i] = euler_angle_update(roll, pitch, yaw, time1, time2, prevAngle)
		
		#use these converions for the synthetic data that is in rads
		#phi.append(math.degrees((float(eulerAngle[i][0]))))
		#theta.append(math.degrees(float(eulerAngle[i][1])))
		#psi.append(math.degrees(float(eulerAngle[i][2])))
		
		#gladiator already in degrees
		phi.append(float(eulerAngle[i][0]))
		theta.append(float(eulerAngle[i][1]))
		psi.append(float(eulerAngle[i][2]))		
		
		prevTime = time2
		prevAngle = eulerAngle[i]
		
	fig, ax = subplots()
	ax.set_title('Kalman Filter on Gladiator IMU')
	ax.set_xlabel('Time (s)')
	ax.set_ylabel('Estimated Body Angles (deg)')
	ax.plot(times, phi, label="Roll")
	ax.plot(times, theta, label="Pitch")
	ax.plot(times, psi, label="Yaw")
	ax.legend(loc=3);
	plt.show()


if __name__ == "__main__":
	main()
	
