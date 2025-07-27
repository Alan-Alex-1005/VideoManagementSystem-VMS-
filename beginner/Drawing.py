import numpy as np
import cv2 as cv

# Create black image and draw on it
img = np.zeros((512,512,3), np.uint8)
cv.line(img,(0,0),(511,511),(255,0,0),5)
cv.rectangle(img,(384,0),(510,128),(0,255,0),3)

while(1):    
    cv.imshow('Drawing image',img)
    if cv.waitKey(20) & 0xFF == 27:
        break
cv.destroyAllWindows()