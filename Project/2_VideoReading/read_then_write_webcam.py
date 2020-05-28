"""
Reading from webcam then write to output.avi
"""

# Import Library
import cv2 as cv
import numpy as np
import os

# Read from webcam with video capture
# 0 is the first webcam available
video = cv.VideoCapture(0)

# Get resolution (wrong resolution will cause the file to be unplayable)
video_width = int(video.get(cv.CAP_PROP_FRAME_WIDTH))
video_height = int(video.get(cv.CAP_PROP_FRAME_HEIGHT))

# 0 for gray scale, 1 for colour (default)
video_colour = 0

# Absolute path to write
abs_path = os.path.dirname(__file__)
out_path = os.path.join(abs_path, 'output/output.avi')

# Output video format
fourcc = cv.VideoWriter_fourcc(*'XVID')
output = cv.VideoWriter(out_path, fourcc, 20.0, (video_width,video_height), video_colour)

while True:
    check,frame = video.read()

    # Display in gray scale
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('Grey', gray)

    # Output recorded gray scale
    # Note: "frame" passed in must comply with the color mode "output" used
    output.write(gray)

    key = cv.waitKey(1)
    # quit with pressing "q"
    if key==ord('q'):
        break

video.release()
output.release()
cv.destroyAllWindows()