# open CV python tutorial 1.  CV-TeamLeo Clemente
import cv2 as cv
#import pandas as pd
#import time



# Displaying images with openCV is really easy.
img = cv.imread('/Users/leonardo/Desktop/Vantec-CV/Dataset/Boat/2017-06-22-11_45_58.png', 0)  # Or IMREAD(file,0)

cv.namedWindow('image', cv.WINDOW_NORMAL) # This function opens a window prior to loading an image (Just like figures in matplotlib or matlab)
cv.imshow('image', img) # imshow shows the image (Duh!). The window name should be specified first, then the image object
cv.waitKey(0)
cv.destroyAllWindows()


img = cv.imread('/Users/leonardo/Desktop/Vantec-CV/Dataset/Boat/2017-06-22-11_45_58.png', 1)

cv.namedWindow('image', cv.WINDOW_NORMAL)
cv.imshow('image', img) #
cv.waitKey(0)
cv.destroyAllWindows()

cap = cv.VideoCapture(0)
cap2 =  cv.VideoCapture('10.23.37.63:4747')


while(True):
    # Capture frame-by-fram
    ret, frame = cap.read()
    ret2, frame2 = cap2.read()

    if cap.isOpened():
        print 'Video Opened correctly.'
    else:
        print 'Video did not Open. Opening with cap.open()'
        cap.open()

    # cap object has fields containing information about the video being captured.
    # They can be accessed by the function .get(propId) where propId is a number from 0 through 18.
    # E.G.

    videoWidth= cap.get(3) #Getting width
    videoHeight = cap.get(4) #Getting height

    print 'Accessed video Width = {0} and Height = {1} using .get()'.format(videoWidth, videoHeight)

    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv.imshow('frame', frame)
    cv.imshow('frame2', frame2)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# When everything's done, release the Capture
cap.release()
cv.destroyAllWindows()
