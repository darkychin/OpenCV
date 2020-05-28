"""
Draw a line on top of doge.jpg with matplotlib
"""

# Import Library
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import os

# Get absolute path
# Reference: https://stackoverflow.com/questions/27844088/python-get-directory-two-levels-up
abs_path = os.path.dirname(os.path.dirname(__file__))
img_path = os.path.join(abs_path, 'input/image/doge.jpg')

# Read an image
img = cv.imread(img_path,cv.IMREAD_COLOR)

# Open image in a window with pixel rulers
plt.imshow(img, cmap='gray', interpolation='bicubic')

# Draw a white line on top of the image
plt.plot([300,250], [400,250], 'white', linewidth=3)
plt.show()
# Press key 'q' to exit window