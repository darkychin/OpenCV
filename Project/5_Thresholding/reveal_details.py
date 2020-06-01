"""
Reveal man-in-red image details with different thresholding methods
"""

# Import Library
import cv2 as cv
import numpy as np
import os

# Get absolute path
# Reference: https://stackoverflow.com/questions/27844088/python-get-directory-two-levels-up
abs_path = os.path.dirname(os.path.dirname(__file__))
man_path = os.path.join(abs_path, 'input/image/man-in-red.jpeg')

# Read man image
man = cv.imread(man_path, cv.IMREAD_COLOR)

# Resize man image
man_resize = cv.resize(man, (int(man.shape[1]/6),int(man.shape[0]/6)))

# Method 1: Global Threshold
# Use Global Threshold
# Note: normal threshold is between 125-150, 12 is chosen here due to low ilumination on the image
retval, threshold = cv.threshold(man_resize, 12, 255, cv.THRESH_BINARY)

# Use Global Threshold on grayscale man
man_gray = cv.cvtColor(man_resize, cv.COLOR_BGR2GRAY)
retval_gray, threshold_gray = cv.threshold(man_gray, 12, 255, cv.THRESH_BINARY)

# Method 2: Adaptive Threshold 
# Type - Gaussian
# Note: 
# 1. source passed in must be in gray scale 
# 2. the lower the blocksize goes, the the more details is captured, 
# but the boundary between foreground and background is mixed. 
threshold_adapt_gaus = cv.adaptiveThreshold(man_gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 115, 1)
# threshold_adapt_gaus2 = cv.adaptiveThreshold(man_gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 1)

# Type - Mean
# Note: source passed in must be in gray scale
threshold_adapt_mean = cv.adaptiveThreshold(man_gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 115, 1)

# Method 3: Otsu
# Note: this method is not useful if the object area is small compared with the background area
retval,threshold_otsu= cv.threshold(man_gray,12,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

# Show Image
cv.imshow('Original',man_resize)
cv.imshow('Threshold',threshold)
cv.imshow('Threshold Gray',threshold_gray)
cv.imshow('Adaptive Threshold - Gaussian', threshold_adapt_gaus)
# cv.imshow('Adaptive Threshold - Gaussian2', threshold_adapt_gaus2)
cv.imshow('Adaptive Threshold - Mean', threshold_adapt_mean)
cv.imshow('Threshold Otsu', threshold_otsu)
cv.waitKey(0)
cv.destroyAllWindows()