import cv2
import numpy as np
import copy
import math

threshold = 20
def print_threshold(threshold):
    print("Binary threshold: "+str(threshold))

# Setup video camera OpenCV object to get input stream from webcam
cam = cv2.VideoCapture(0)
# Set some size
cam.set(100,250)
cv2.namedWindow('track')
cv2.createTrackbar('tr1','track',threshold,100,print_threshold)

while cam.isOpened():
    key_press = cv2.waitKey(10)
    # Check if 'escape' key is pressed
    if key_press == 27:
        cam.release()
        cv2.destroyAllWindows()
        break
    # Check if 'b' key is pressed to capture background
    elif key_press == ord('b'):
        background = cv2.createBackgroundSubtractorMOG2(0, background_threshold)
        background_flag = True
        print( 'Background Set \n')
    # Check if 'r' key is pressed to refresh background
    elif key_press == ord('r'):
        background = None
        background_flag = False
        print ('Background Reset \n')
