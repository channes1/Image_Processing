#load/import packages
import cv2 as cv
import numpy as np

#Read image
image = cv.imread("img1.png")

#Detect hsv from the image
hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)

#Detect range of red
lower_red = np.array([0,120,70])
upper_red = np.array([10,255,255])
mask1 = cv.inRange(hsv, lower_red, upper_red)
 
#cont....
lower_red = np.array([170,120,70])
upper_red = np.array([180,255,255])
mask2 = cv.inRange(hsv,lower_red,upper_red)

# Generating the final mask to detect red color
mask_r = mask1 + mask2

#Detect range for blue
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])

mask_b = cv.inRange(hsv, lower_blue, upper_blue)

#Detect range for green
lower_green = np.array([45, 100, 100])
upper_green = np.array([75,255,255])

mask_g = cv.inRange(hsv, lower_green, upper_green)

res1 = cv.bitwise_and(image, image, mask = mask_r)
res2 = cv.bitwise_and(image, image, mask = mask_b)
res3 = cv.bitwise_and(image, image, mask = mask_g)

cv.imshow("Original image", image)
cv.imshow("hsv", hsv)
cv.imshow("Detect Red", res1)
cv.imshow("Detect Blue", res2)
cv.imshow("Detect Green", res3)

cv.waitKey(0)
cv.destroyALLWindows()