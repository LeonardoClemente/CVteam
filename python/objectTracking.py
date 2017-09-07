import cv2
import argparse
import sys
import time

# Set up tracker.
# Instead of MIL, you can also use
# BOOSTING, KCF, TLD, MEDIANFLOW or GOTURN


# Variables for ROI detection
roi_coordinates = [(0,0), (0,0)]
checking_ROI = True
bbox = None
firstCoord = False
# Read video : (Put either a device or a camera)
dev = 0 #'../testImages/roboboatCam.mp4' #
video = cv2.VideoCapture(dev) #


# Callback Functions

def myROI(event, x, y, flags, param):
    # grab references to the global variables
    global roi_coordinates, clone, firstCoord
    print('EnteringEvent')

    # if the left mouse button was clicked, record the starting
    # (x, y) coordinates
    if event == cv2.EVENT_LBUTTONDOWN and firstCoord == False:
        print('Selected initial coordinates as ({0}, {1})'.format(x, y))
        roi_coordinates[0] = (x, y)
        firstCoord = True
    # Record second set of coordinates to give an idea of shape
    elif event == cv2.EVENT_MOUSEMOVE and firstCoord == True:
        roi_coordinates[1] = (x, y)
        # Save last set of cooridnates
        # draw a rectangle around the region of interest
        img2 = cv2.rectangle(clone.copy(), roi_coordinates[0], roi_coordinates[1], (0, 255, 0), 2)
        cv2.imshow("image", img2)

    elif event == cv2.EVENT_LBUTTONUP and firstCoord == True:
    # record the ending (x, y) coordinates and indicate that
        print('Selected final coordinates as {0}'.format((x,y)))
        roi_coordinates[1] = (x, y)
        # draw a rectangle around the region of interest
        img2 = cv2.rectangle(clone.copy(), roi_coordinates[0], roi_coordinates[1], (0, 255, 0), 2)
        cv2.imshow("image", img2)
        firstCoord = False







tracker =cv2.TrackerKCF_create()  # Starts KCF tracker device, KCF explanation: https://arxiv.org/pdf/1404.7584.pdf

# Read first frame.
ok, frame = video.read()

clone = frame.copy()


# Exit if video not opened.
if not video.isOpened():
    print("Could not open video")
    sys.exit()

if not ok:
    print('Cannot read video file')
    sys.exit()

# Define an initial bounding box



'''
# Find region of interest
cv2.namedWindow("Select region of interest")
cv2.setMouseCallback("Select region of interest", myROI)

# bbox = cv2.selectROI(frame, False) # BUILT in ROI

while checking_ROI:
    cv2.imshow("Select region of interest", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("k"):
        bbox = roi_coordinates
        checking_ROI = False
    elif key == ord("c"):
        sys.exit()
        roi_coordinates = [(0,0), (0,0)]
'''



while True:
    # Read a new frame
    ok, frame = video.read()
    if not ok:
        break

    # Update tracker
    if bbox is None:
        time.sleep(1)
        ok, frame = video.read()
        bbox = cv2.selectROI(frame, False)
        ok = tracker.init(frame, bbox) # Initialize tracker with first frame and bounding box

    ok, bbox = tracker.update(frame)


    # Draw bounding box
    if ok:
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        cv2.rectangle(frame, p1, p2, (0,0,255))

    # Display result
    cv2.imshow("Tracking", frame)

    # Exit if ESC pressed
    k = cv2.waitKey(1) & 0xff
    if k == 27 : break
