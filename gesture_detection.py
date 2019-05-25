import cv2
import numpy as np
import copy
import math


# Setup video camera OpenCV object to get input stream from webcam
cam = cv2.VideoCapture(0)
# Set some size
cam.set(10,100)
cv2.namedWindow('track')
cv2.createTrackbar('tr1','track',threshold,100)
