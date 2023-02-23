import numpy as np
import cv2 as cv2
import matplotlib.pyplot as plt
from cv_bridge import CvBridge
cap = cv2.VideoCapture('ball.mov')
if (cap.isOpened()==False):
    print("error on opening ")
trajectory = np.array([[0,0]])
while (cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if(not ret):
        break
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_mask_limit = np.array([0, 100, 100])
    upper_mask_limit = np.array([2, 255, 255])
    mask = cv2.inRange(hsv, lower_mask_limit, upper_mask_limit)
    pixel = np.argwhere(mask == 255)
    if ret == True:
        # Display the resulting frame
        contours, hierarchies = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        blank = np.zeros(mask.shape[:2],dtype='uint8')
        cv2.drawContours(blank, contours, -1, (255, 0, 0), 1)
        for i in contours:
            M = cv2.moments(i)
            if M['m00'] != 0:
                cx = int(M['m10']/M['m00'])
                cy = int(M['m01']/M['m00'])
                point = np.array([[cx, cy]])
                trajectory = np.append(trajectory, point, axis = 0)
                cv2.drawContours(frame, [i], -1, (0, 255, 0), 2)
                cv2.circle(frame, (cx, cy), 7, (0, 0, 255), -1)
                cv2.putText(frame, "center", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
            # if cx<562 and cy<1218:
                # mask[cx, cy] = (255, 0, 0)
        # out = cv2.VideoWriter('ball.mov',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (562,1218))
        if trajectory.size > 6:
            x2_term = np.array([np.multiply(trajectory[:,0], trajectory[:,0])])
            x2_term = x2_term.T
            equation = np.append(x2_term, trajectory, axis=1)
            equation = np.delete(equation, 0, 0)
            equation = np.delete(equation, 0, 0)
            Y = equation[:,2]
            X = np.delete(equation, 2, 1)
            # Create an array of all ones
            vec_of_ones = np.ones((Y.size,1))
            X = np.append(X, vec_of_ones, axis=1)
            B = np.dot(np.linalg.inv(np.dot(X.T,X)), np.dot(X.T,Y))
            for i in range (1, 1200, 10):
                x = int(i)
                y = int(B[0]*x*x + B[1]*x + B[2])
                cv2.circle(frame, (x, y), 3, (255, 0, 0), -1)
                cv2.imshow('Frame',frame)

        cv2.imshow('Frame',frame)
        cv2.imshow("mask", mask)
        # Press Q on keyboard to  exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    
    # Break the loop
    else: 
        break

print("Coefficients of Quadratic equation are")
print(B)
y_init = trajectory[2,1]
y_init = y_init + 300
a = B[0]
b = B[1]
c = B[2]
c = c-y_init
x_final = (-1*b+np.sqrt(b*b-4*a*c))/(2*a)
print("x_final is")
print(x_final)
# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()
if __name__ == '__main__':
    main(sys.argv)