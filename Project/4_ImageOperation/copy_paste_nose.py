"""
Copy doge's nose and paste it on top left with OpenCV
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

# Pickup the last pixel of nose
before_px = img[330,395]

# Pickup nose by reference (because nose is not a list)
nose = img[240:340,300:400]

# Draw some white
# Note: this white proved that nose is pick up by reference , not by value
img[320:360,360:400] = [255,255,255]

# Print nose's Region of Image (ROI)
print(nose)

# Pick up the last pixel of nose after whiten
after_px = img[330,395]

# Put nose at the top left corner
img[0:100,0:100] = nose

# Draw a rectangle on doge's nose with cv
cv.rectangle(img, (300,240),(400,340), (0,255,0),3)

# Put text label
cv.putText(img,'nose',(300,250),cv.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),1)

# Open Image in a window
cv.imshow('image',img)
# When wait for 0 millisecond, it will exit with any key pressed
cv.waitKey(0)
cv.destroyAllWindows()

# Print pixel to compare (still by reference)
# print(before_px)
# print(after_px)