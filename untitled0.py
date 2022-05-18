import cv2
import numpy as np


im = cv2.imread('img1-bw.png')

#im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

#Feature enhancement

erode_kernel_size = (3,3)
erode_iterations = 1
threshold_thresh = 81

kernel = np.ones(erode_kernel_size, np.uint8)
im = cv2.erode(im, kernel, iterations = erode_iterations)

#imagee thresholding 
th, im_bw = cv2.threshold(im, 50, 240, cv2.THRESH_BINARY)

cv2.imshow("A", im_bw)
   
cv2.waitKey(1)
cv2.destroyAllWindows()