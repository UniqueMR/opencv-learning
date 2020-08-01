import cv2
import numpy as np

path = 'E:/shapes.jpg'

def getContours(img,imgContour):
    contours, hieracy = cv2.findContours(img, mode=cv2.RETR_EXTERNAL,method=cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area > 500:
            cv2.drawContours(imgContour,cnt,-1,(0,255,0),thickness=2)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            print(len(approx))
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(imgContour, (x,y), (x+w,y+h), (0,255,0), 1)

            if objCor == 3:
                objectType ="Tri"

            elif objCor == 4:
                judge = w/float(h)
                if judge > 0.95 and judge < 1.05:
                    objectType = "Square"
                else:
                    objectType = "Rectangle"

            else:
                objectType = "Circle"


            cv2.putText(imgContour, objectType, (x+(w//2)-10,y+(h//2)-10), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,0,0), 1)

path = "E:\shapes.jpg"
img = cv2.imread(path)
imgContour = img.copy()
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 1)
imgCanny = cv2.Canny(imgBlur,50,50)

getContours(imgCanny,imgContour)

cv2.imshow("Result",imgContour)

cv2.waitKey(0)
