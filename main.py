import requests
import cv2
import utils
import numpy as np
import filters
import os
from scipy import ndimage

planets = cv2.imread('screenshot.png')
gray_img = cv2.cvtColor(planets,cv2.COLOR_BGR2GRAY)

img = cv2.medianBlur(gray_img, 5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,120,param1=100,param2=30,minRadius=0,maxRadius=0)

circles = np.uint16(np.around(circles))

print(circles[0,:])
for i in circles[0,:]:
    #draw the outer circle
    cv2.circle(planets,(i[0],i[1]),i[2],(0,255,0),2)
    #draw the center of the circle
    cv2.circle(planets,(i[0],i[1]),2,(0,0,255),3)

cv2.imwrite('planets_circles.jpg',planets)
cv2.imshow('HoughCircles',planets)
cv2.waitKey(0)
cv2.destroyAllWindows()