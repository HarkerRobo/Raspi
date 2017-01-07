import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

	# Take each frame
	re, frame = cap.read()

	# Convert BGR to HSV
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	center = 180
	error = 30

	# define range of blue color in HSV
	color = 75
	err = 5
	lower_blue = (color - error, 150,150)
	upper_blue = (color + error, 255,255)
	#print lower_blue, upper_blue

	# Threshold the HSV image to get only blue colors
	mask = cv2.inRange(hsv, lower_blue, upper_blue)
	mask = cv2.erode(mask, None, iterations=2)
	mask = cv2.dilate(mask, None, iterations=2)

	# Bitwise-AND mask and original image
	res = cv2.bitwise_and(frame,frame, mask= mask)

	cv2.imshow('frame',frame)
	cv2.imshow('mask',mask)
	cv2.imshow('res',res)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cv2.destroyAllWindows()
