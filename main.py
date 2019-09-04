import cv2
import requests
import numpy as np
import os

videoCapture = cv2.VideoCapture('0.mp4')
fps = videoCapture.get(cv2.CAP_PROP_FPS)
print(fps,'帧')
size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
videoWrite = cv2.VideoWriter('MyOutputVid.avi',cv2.VideoWriter_fourcc('I','4','2','0'),fps,size)
success, frame = videoCapture.read()

while success:
    videoWrite.write(frame)
    success, frame = videoCapture.read()
