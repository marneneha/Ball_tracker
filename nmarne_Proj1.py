import numpy as np
import cv2 as cv2
import matplotlib.pyplot as plt
from cv_bridge import CvBridge
#394,450
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

        # print("m here")
        print(mask.shape)
        contours, hierarchies = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        blank = np.zeros(mask.shape[:2],dtype='uint8')
        cv2.drawContours(blank, contours, -1, (255, 0, 0), 1)
        cv2.imwrite("Contours.png", blank)
        for i in contours:
            M = cv2.moments(i)
            if M['m00'] != 0:
                cx = int(M['m10']/M['m00'])
                cy = int(M['m01']/M['m00'])
                cv2.drawContours(frame, [i], -1, (0, 255, 0), 2)
                cv2.circle(frame, (cx, cy), 7, (0, 0, 255), -1)
                cv2.putText(frame, "center", (cx - 20, cy - 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
            print(f"x: {cx} y: {cy}")
            # if cx<562 and cy<1218:
                # mask[cx, cy] = (255, 0, 0)
        # out = cv2.VideoWriter('ball.mov',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (562,1218))
        cv2.imshow('Frame',frame)
        cv2.imshow("mask", mask)
        # print("m here2")
        # print(np.average(np.average(mask, axis=1)))
        # print(np.average(np.average(mask, axis=0)))
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