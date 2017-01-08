import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)

cv2.circle(img, (477,63), 63, (0,0,255), -1)

cv2.imshow('image', img)
while(1):
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cv2.destroyAllWindows()
