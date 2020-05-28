"""
Add both weighted python-logo and doge together with OpenCV
"""

# Import Library
import cv2 as cv
import numpy as np
import os

# Get absolute path
# Reference: https://stackoverflow.com/questions/27844088/python-get-directory-two-levels-up
abs_path = os.path.dirname(os.path.dirname(__file__))
doge_path = os.path.join(abs_path, 'input/image/doge.jpg')
logo_path = os.path.join(abs_path, 'input/image/python-logo.png')

# Read image
doge = cv.imread(doge_path, cv.IMREAD_COLOR)
logo = cv.imread(logo_path, cv.IMREAD_COLOR)

# Resize logo
logo_resize = cv.resize(logo, (doge.shape[1],doge.shape[0]))

# Final image
# Note: the weight somehow works like opacity
final = cv.addWeighted(doge, 0.7, logo_resize, 0.3, 0)

# Open combined image
cv.imshow('Final Image', final)
# When wait for 0 millisecond, it will exit with any key pressed
cv.waitKey(0)
cv.destroyAllWindows()
