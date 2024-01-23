import os
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cv2.inRange(hsvImage)

    cv2.imshow("frame", frame)

    if cv2.waitKey(0) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

