import numpy as np
import cv2 as cv2
import matplotlib.pyplot as plt
from cv_bridge import CvBridge

def nothing(x):
    pass
# print("inside project 1 file")
cap = cv2.VideoCapture('ball.mov')
cv2.namedWindow("Trackbars")
cv2.createTrackbar("L-H", "Trackbars", 0, 179, nothing)
cv2.createTrackbar("L-S", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("L-V", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("U-H", "Trackbars", 0, 179, nothing)
cv2.createTrackbar("U-S", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("U-V", "Trackbars", 0, 255, nothing)
# if (cap.isOpened()==False):
#     print("error on opening ")

cap.set(cv2.CAP_PROP_POS_FRAMES, 100)
res, frame = cap.read()
# cv2.waitKey(0)
while True:
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    l_h = cv2.getTrackbarPos("L-H", "Trackbars")
    l_s = cv2.getTrackbarPos("L-S", "Trackbars")
    l_v = cv2.getTrackbarPos("L-V", "Trackbars")
    u_h = cv2.getTrackbarPos("U-H", "Trackbars")
    u_s = cv2.getTrackbarPos("U-S", "Trackbars")
    u_v = cv2.getTrackbarPos("U-V", "Trackbars")
    lower_mask_limit = np.array([0, 100, 100])
    upper_mask_limit = np.array([2, 255, 255])
    mask = cv2.inRange(hsv, lower_mask_limit, upper_mask_limit)
    cv2.imshow('Frame',frame)
    cv2.imshow('mask',mask)
    key = cv2.waitKey(1)
    if key == 'k':
        break

while False:
    # Capture frame-by-frame
    # ret, frame = cap.read()
    cap.set(cv2.CAP_PROP_POS_FRAMES, 100)
    res, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    l_h = cv2.getTrackbarPos("L-H", "Trackbars")
    l_s = cv2.getTrackbarPos("L-S", "Trackbars")
    l_v = cv2.getTrackbarPos("L-V", "Trackbars")
    u_h = cv2.getTrackbarPos("U-H", "Trackbars")
    u_s = cv2.getTrackbarPos("U-S", "Trackbars")
    u_v = cv2.getTrackbarPos("U-V", "Trackbars")
    lower_mask_limit = np.array([l_h, l_s, l_v])
    upper_mask_limit = np.array([u_h, u_s, u_v])
    mask = cv2.inRange(hsv, lower_mask_limit, upper_mask_limit)

    cv2.imshow('Frame',frame)

    # if ret == True:
    
    #     # Display the resulting frame
    #     cv2.imshow('Frame',frame)
    #     cv2.imshow("mask", mask)
    #     # Press Q on keyboard to  exit
    #     if cv2.waitKey(25) & 0xFF == ord('q'):
    #         break
    
    # # Break the loop
    # else: 
    #     break

# When everything done, release the video capture object
# cap.release()

# Closes all the frames
cv2.destroyAllWindows()
if __name__ == '__main__':
    main(sys.argv)