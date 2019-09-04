import requests
import cv2
import numpy as np
import os
from scipy import ndimage

#高通滤波器是根据像素与邻近像素的亮度差值来提升该像素的亮度
kernel_3x3 = np.array([
    [-1,-1,-1],
    [-1,0,-1],
    [-1,-1,-1]])

kernel_5x5 = np.array([
    [-1,-1,-1,-1,-1],
    [-1,1,2,1,-1],
    [-1,2,4,2,-1],
    [-1,1,2,1,-1],
    [-1,-1,-1,-1,-1]])

img = cv2.imread('235157-106.jpg',0)
k3 = ndimage.convolve(img,kernel_3x3)
k5 = ndimage.convolve(img,kernel_5x5)

blurred = cv2.GaussianBlur(img,(11,11),0)
g_hpf = img - blurred
cv2.namedWindow('3x3',cv2.WINDOW_NORMAL)
cv2.namedWindow('5x5',cv2.WINDOW_NORMAL)
cv2.namedWindow('g_hpf',cv2.WINDOW_NORMAL)

cv2.imshow('3x3',k3)
cv2.imshow('5x5',k5)
cv2.imshow('g_hpf',g_hpf)
cv2.waitKey()
cv2.destroyAllWindows()
