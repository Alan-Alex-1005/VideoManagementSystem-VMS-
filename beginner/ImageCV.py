import cv2 as cv
import sys
img = cv.imread(cv.samples.findFile("assests/alanpic.jpg",cv.IMREAD_UNCHANGED))
if img is None:
    sys.exit("could not read the image")
cv.imshow("Display window",img)
k = cv.waitKey(0)
if k == ord("q"):
    cv.imwrite("assests/alanpic.jpg",img)    