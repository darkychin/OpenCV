"""
Draw a clown on top of doge.jpg with OpenCV
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
img = cv.imread(img_path, cv.IMREAD_COLOR)

# Draw red nose
# Note: when thickness is -1, it will fill up the circle
cv.circle(img, (350,280), 45, (0,0,255), -1)

# Draw goggles
pts = np.array([[330,180],[350,230],[420,200],[500,280],[550,220],[500,100]], np.int32)
cv.polylines(img, [pts], True, (0,255,255), 3)

# Draw a frame on doge
cv.rectangle(img, (250,15),(690,490), (0,255,0),3)

# Put text label
cv.putText(img,'clown',(260,485),cv.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),1)

# Open Image in a window
cv.imshow('doge-clown',img)
# When wait for 0 millisecond, it will exit with any key pressed
cv.waitKey(0)
cv.destroyAllWindows()