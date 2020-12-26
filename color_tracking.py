import cv2
import numpy as np

def nothing(x):
    pass


# define a video capture object
video = cv2.VideoCapture(0)
cv2.namedWindow("Trackbars")

cv2.createTrackbar("L-H", "Trackbars", 0, 179, nothing)
cv2.createTrackbar("L-S", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("L-V", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("U-H", "Trackbars", 0, 179, nothing)
cv2.createTrackbar("U-S", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("U-V", "Trackbars", 0, 255, nothing)


while True:
    
    #Capture the video frame by frame
    ret, frame = video.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    l_h = cv2.getTrackbarPos("L-H", "Trackbars")
    l_s = cv2.getTrackbarPos("L-S", "Trackbars")
    l_v = cv2.getTrackbarPos("L-V", "Trackbars")
    u_h = cv2.getTrackbarPos("U-H", "Trackbars")
    u_s = cv2.getTrackbarPos("U-S", "Trackbars")
    u_v = cv2.getTrackbarPos("U-V", "Trackbars")
    
    #create the range for the blue
    lower_blue = np.array([l_h, l_s, l_v])
    upper_blue = np.array([u_h, u_s, u_v])
    #default
#     lower_blue = np.array([37, 62, 0])
#     upper_blue = np.array([109, 255, 255])
    #create the mask
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    cv2.imshow("mask", mask)
    
    output = cv2.bitwise_and(frame, frame, mask = mask)
    
    
    #Display the resulting frame
    cv2.imshow('webcam', frame)
#    cv2.imshow('gray webcam', gray)
    cv2.imshow("output", output)

    # the 'q' button is set as the 
    # quitting button 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
    
# When everything done, release the capture
video.release()
cv2.destroyAllWindows()