"""
Draw a rectangle on doge's nose with OpenCV
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
img = cv.imread(img_path,cv.IMREAD_COLOR)

# Draw a rectangle on doge's nose with cv
cv.rectangle(img, (300,240),(400,340), (0,255,0),3)

# Put text label
cv.putText(img,'nose',(300,250),cv.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),1)

# Open Image in a window
cv.imshow('image',img)
# When wait for 0 millisecond, it will exit with any key pressed
cv.waitKey(0)
cv.destroyAllWindows()