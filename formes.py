import cv2
import numpy as np

image = cv2.imread('images/image.jpg', cv2.IMREAD_GRAYSCALE)

blurred = cv2.GaussianBlur(image, (15, 15), 0)

circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, dp=1.2, minDist=30, param1=50, param2=30, minRadius=20, maxRadius=100)

if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    for (x, y, r) in circles:
        cv2.circle(image, (x, y), r, (0, 255, 0), 4)

cv2.imshow("Cercles détectés", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
