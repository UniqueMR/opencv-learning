import numpy as np
import cv2

img = cv2.imread('E:\lamborghini.jpg')
print(img.shape)

#kernel = np.ones((2,2),dtype=np.uint8)

#imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#imgBlur = cv2.GaussianBlur(imgGray, ksize=(7,7),sigmaX=0)
#imgCanny = cv2.Canny(img,threshold1=100,threshold2=100)
#imgDialation = cv2.dilate(imgCanny, kernel, iterations=2)
#imgErrosion = cv2.erode(imgDialation, kernel, iterations=2)

cv2.imshow('image', img)
#cv2.imshow('canny image',imgCanny)
#cv2.imshow('dialation image',imgDialation)
#cv2.imshow('erossion image',imgErrosion)

#imResize = cv2.resize(img,(1920,1080))

#cv2.imshow('resized image',imResize)
imgCropped = img[100:200,200:500]

cv2.imshow('cropped image',imgCropped)

cv2.waitKey(0)