import cv2
import numpy as np

img = np.zeros((480,640,3),dtype=np.uint8)

#img[100:400,200:500] = 0,255,0
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),2)
cv2.rectangle(img,(100,100),(300,300),(255,255,0),2)
cv2.circle(img,(250,250),50,(255,255,0),2)
cv2.putText(img,'Fuck you!',(200,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)

cv2.imshow('Image',img)

cv2.waitKey(0)
