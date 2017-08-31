import cv2
import numpy as np
import Config
'''Find contours tutorial.
As defined by the OpenCV tutorial, a contour is a set of pixels that continously
enclose an area within the image that has the same color or intensity.
'''


im = cv2.imread('test.jpg')


# It is recommended to add pre-processing before finding contours (Turn into binary image).
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)





# .findContours() receives three inputs:  the image, the way you want the contours to be organized (retrieval mode)
# and its approximation method (after detecting a contour, how much information from it to keep)
# Approximation methods are useful to save memory but might reduce accuracy.

im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


cv2.drawContours(img, contours, -1, (0,255,0), 3)

cnt = contours[4]
cv2.drawContours(img, [cnt], 0, (0,255,0), 3)
