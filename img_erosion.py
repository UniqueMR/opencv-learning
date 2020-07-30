import cv2
import numpy

kernel = numpy.ones((2,2),dtype=numpy.uint8)

img = cv2.imread('E:/racingcar.jpg')

img_erosion = cv2.erode(img, kernel, iterations=1)

cv2.imshow('imgErosion',img_erosion)
cv2.imshow('img',img)

cv2.waitKey(0)