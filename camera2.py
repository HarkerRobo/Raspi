import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)

last_time = time.clock()
count = 0

while(1):
        loop_time = time.clock() - last_time
        last_time = time.clock()
        fps = int(1/loop_time)
        count += 1
        if count > fps:
                print "fps: " + str(fps)
                count = 0
        
	# Take each frame
	re, frame = cap.read()

	# Convert BGR to HSV
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        
        center = tuple([x/2 for x in hsv.shape[:2]][::-1])
        #print "center" + str(center)
                
        col = hsv[240,320]

	# define range of blue color in HSV
	color = 0
	err = 0
	lower = (color-err,0,150)
	upper = (color+err, 255,255)
	#print lower_blue, upper_blue

        #hsv = cv2.GaussianBlur(hsv, (15,15),0)

	# Threshold the HSV image to get only blue colors
	mask = cv2.inRange(hsv, lower, upper)
	mask = cv2.erode(mask, None, iterations=2)
	mask = cv2.dilate(mask, None, iterations=2)


        # Draw circle
        cv2.circle(frame,center,10,(255,255,255), 1)
        cv2.putText(frame,str(col),center,cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0))

	# Bitwise-AND mask and original image
	res = cv2.bitwise_and(frame,frame, mask= mask)

	cv2.imshow('frame',frame)
	cv2.imshow('mask',mask)
	cv2.imshow('res',res)
	#cv2.imshow('hsv',hsv)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cv2.destroyAllWindows()
