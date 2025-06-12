import cv2
print(cv2.__version__)
img = cv2.imread("assests/alanpic.jpg",cv2.IMREAD_COLOR)
cv2.imshow("assests/alanpic.jpg",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

