#import numpy as np
import cv2 as cv

#img = np.zeros((512,512,3), np.uint8)
#cv.line(img,(0,0),(511,511),(255,0,0),5)
cap = cv.VideoCapture(0)
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_models/haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_models/haarcascade_eye.xml')
if not cap.isOpened():
    print("cannot open camera alan")
    exit()
while True:
    # Read frame-by-frame
    ret, frame = cap.read()
    if not ret:
       # print("Can't receive frame (stream end?). Exiting...")
        break
    
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    cv.imshow('Alan',gray)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    for (x, y, w, h) in faces:
     cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)   
     
     roi_gray =gray [y:y+h, x:x+w]
     roi_color= frame[y:y+h,x:x+w]
     eyes = eye_cascade.detectMultiScale(roi_gray)

    for(ex,ey,ew,eh) in eyes:
     cv.rectangle(frame, (xx, ey), (ex + ew, ey + eh), (0, 255, 0), 2)   


    cv.imshow("rect on face",frame)

    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()  

