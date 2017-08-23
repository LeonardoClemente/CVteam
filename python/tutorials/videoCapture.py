import cv2 as cv

cap =  cv.VideoCapture("http://10.23.14.237:4747/mjpegfeed")

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    if cap.isOpened():
        print ("Video Opened correctly.")
    else:
        print ("Video did not Open. Opening with cap.open()")
        cap.open()

    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv.imshow("grayscale", gray)
    cv.imshow("normal", frame)

    if cv.waitKey(1) & 0xFF == ord("q"):
        break

# When everything's done, release the Capture
cap.release()
cv.destroyAllWindows()
