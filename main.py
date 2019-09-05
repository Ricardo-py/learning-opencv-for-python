import requests
import cv2
import utils
import numpy as np
import filters
import os
from scipy import ndimage

img = np.zeros((200,200),dtype=np.uint8)

img[50:150,50:150] = 255

src = cv2.imread('235157-106.jpg')
ret, thresh = cv2.threshold(img,127,255,0)
ret2,thresh2 = cv2.threshold(src,127,255,cv2.THRESH_BINARY)
cv2.imshow('myWindow',thresh2)
#findContours第一个是输入图像，第二个是轮廓检索模式，第三个是轮廓近似方法
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

color = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
#函数cv2.drawContours()被用来绘制轮廓。第一个参数是一张图片，可以是原图或者其他。第二个参数是轮廓，也可以说是cv2.findContours()找出来的点集，一个列表。第三个参数是对轮廓（第二个参数）的索引，当需要绘制独立轮廓时很有用，若要全部绘制可设为-1。接下来的参数是轮廓的颜色和厚度。
img = cv2.drawContours(color,contours,-1,(0,255,0),2)
cv2.imshow('contours',color)
cv2.waitKey(0)
cv2.destroyAllWindow()
