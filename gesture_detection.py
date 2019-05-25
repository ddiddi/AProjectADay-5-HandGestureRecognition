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

    frame_ret, frame = cam.read()
    threshold = cv2.getTrackbarPos('tr1','track')

    smooth_frame = cv2.bilateralFilter(frame, 5, 50, 100)  # smoothing filter
    flip_frame = cv2.flip(smooth_frame, 1)  # flip the frame horizontally
    cv2.imshow('Frame', flip_frame)

    if background_flag == True:
        # Create background mask from input
        mask = background.apply(flip_frame,learningRate=0)
        kernel = np.ones((3, 3), np.uint8)
        mask = cv2.erode(mask, kernel, iterations=1)
        mask_image = cv2.bitwise_and(flip_frame, flip_frame, mask=mask)
        cv2.imshow('mask', mask_image)

        # Process image into thresholding for hand detection
        gray_mask = cv2.cvtColor(mask_image, cv2.COLOR_BGR2GRAY)
        blur_mask = cv2.GaussianBlur(gray_mask, (40, 40), 0)
        cv2.imshow('blur', blur_mask)
        ret, thresh = cv2.threshold(blur_mask, threshold, 255, cv2.THRESH_BINARY)
        cv2.imshow('threshold', thresh)

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
