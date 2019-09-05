import requests
import cv2
import utils
import numpy
import filters
import os
from scipy import ndimage

src = cv2.imread('235157-106.jpg')
cv2.namedWindow('myWindow1',cv2.WINDOW_NORMAL)
cv2.namedWindow('myWindow2',cv2.WINDOW_NORMAL)
cv2.namedWindow('myWindow3',cv2.WINDOW_NORMAL)
cv2.imshow('myWindow1',src)
#b,g,r = cv2.split(src)
#
#dtype = numpy.uint8
#length = numpy.iinfo(dtype).max + 1
#bFunc = None
#vFunc = None
#gFunc = None
#rFunc = None
#bLookupArray = utils.createLookupArray(utils.createCompositeFunc(bFunc, vFunc), length)
#gLookupArray = utils.createLookupArray(utils.createCompositeFunc(gFunc, vFunc), length)
#rLookupArray = utils.createLookupArray(utils.createCompositeFunc(rFunc, vFunc), length)

#utils.applyLookupArray(bLookupArray, b, b)
#utils.applyLookupArray(gLookupArray, g, g)
#utils.applyLookupArray(rLookupArray, r, r)

#cv2.merge([b,g,r],src)
#cv2.imshow('myWindow2',src)
#cv2.waitKey(0)

filters.strokeEdges(src,src)
cv2.imshow('myWindow2',src)
curveFilter = filters.BGRPortraCurveFilter()
curveFilter.apply(src,src)
cv2.imshow('myWindow3',src)
cv2.waitKey(0)
