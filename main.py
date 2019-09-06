import requests
import cv2
import utils
import numpy as np
import filters
import os
from scipy import ndimage

img = cv2.imread('235157-106.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray,50,120)

minLineLength = 20
maxLineGap = 5

#opencv的HoughLinesP函数是统计概率霍夫线变换函数，该函数能输出检测到的直线的端点 (x_{0}, y_{0}, x_{1}, y_{1}),
#其函数原型为：HoughLinesP(image, rho, theta, threshold, lines, minLineLength, maxLineGap) -> lines
lines = cv2.HoughLinesP(edges,1,np.pi / 180, 100, minLineLength, maxLineGap)



for x1, y1, x2, y2 in lines[0]:
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)


cv2.imshow('edges',edges)

cv2.imshow('lines',img)

cv2.waitKey(0)

cv2.destroyAllWindows()
