import cv2
import numpy
import utils

def strokeEdges(src,dst,blurKsize = 7, edgeKsize = 5):
    if blurKsize >= 3:
        blurredSrc = cv2.medianBlur(src,blurKsize)
        graySrc = cv2.cvtColor(blurredSrc,cv2.COLOR_BGR2GRAY)
    else:
        graySrc = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)

    cv2.Laplacian(graySrc,cv2.CV_8U,graySrc,ksize=edgeKsize)
    normalizedInverseAlpha = (1.0 / 255) * (255 - graySrc)
    channels = cv2.split(src)
    for channel in channels:
        channel[:] = channel * normalizedInverseAlpha
    cv2.merge(channels,dst)

if __name__ == '__main__':
    src = cv2.imread('235157-106.jpg')
    dst = src
    strokeEdges(src,dst)
    cv2.namedWindow('myWindow',cv2.WINDOW_NORMAL)
    cv2.imshow('myWindow',dst)
    cv2.waitKey(0)