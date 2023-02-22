import numpy as np
import cv2 as cv2
import matplotlib.pyplot as plt
from cv_bridge import CvBridge

# print("inside project 1 file")
cap = cv2.VideoCapture('ball.mov')
if (cap.isOpened()==False):
    print("error on opening ")

while (cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_mask_limit = np.array([0, 100, 100])
    upper_mask_limit = np.array([2, 255, 255])
    mask = cv2.inRange(hsv, lower_mask_limit, upper_mask_limit)

    if ret == True:
    
        # Display the resulting frame
        cv2.imshow('Frame',frame)
        cv2.imshow("mask", mask)
        # Press Q on keyboard to  exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    
    # Break the loop
    else: 
        break

# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()
if __name__ == '__main__':
    main(sys.argv)