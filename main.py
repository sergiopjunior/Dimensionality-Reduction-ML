import cv2 as cv
import numpy as np

thresh = 127
img = cv.imread(r"cat.jpg")
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

img_bin = cv.threshold(img_gray, thresh, 255, cv.THRESH_BINARY)[1]

img_bin_filter = cv.GaussianBlur(img_gray, (7, 7), 0)
img_bin_filter = cv.threshold(img_bin_filter, thresh, 255, cv.THRESH_BINARY)[1]

cv.imshow('Normal Image', img)
cv.imshow("Gray Scale Image", img_gray)
cv.imshow("Binary Image", img_bin)
cv.imshow("Binary Gaussian Image", img_bin_filter)
cv.waitKey()
cv.destroyAllWindows()
