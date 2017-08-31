import cv2 as cv

cap =  cv.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    if cap.isOpened():
        print ("Video Opened correctly.")
    else:
        print ("Video did not Open. Opening with cap.open()")
        cap.open()

    # Our operations on the frame come here
    #gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv.rectangle(frame,(384,100),(510,128),(0,255,0),8)
    #cv.imshow("grayscale", gray)
    cv.imshow("normal", frame)

    if cv.waitKey(1) & 0xFF == ord("q"):
        break

# When everything's done, release the Capture
cap.release()
cv.destroyAllWindows()
