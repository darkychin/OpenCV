"""
Read Image - image/doge.jpg
"""

# Import Library
import cv2 as cv
import numpy as np
import os

# Get absolute path
# Reference: https://stackoverflow.com/questions/27844088/python-get-directory-two-levels-up
abs_path = os.path.dirname(os.path.dirname(__file__))
img_path = os.path.join(abs_path, 'input/image/doge.jpg')

# Read an image
# This position is absolute path, so please move to proper project directory before running the script
img = cv.imread(img_path,cv.IMREAD_COLOR)
"""
flags/Enum:
IMREAD_UNCHANGED = -1
IMREAD_GRAYSCALE = 0
IMREAD_COLOR = 1
"""

# Resize image 
# 1. this will compressed the image
#   resize_img = cv.resize(img, (600,600))
# 2. this will scale properly
resize_img = cv.resize(img, (int(img.shape[1]/2),int(img.shape[0]/2)))

# Open Image in a window
cv.imshow('image',resize_img)
# When wait for 0 second till exit it will exit with any key press
cv.waitKey(0)
cv.destroyAllWindows()