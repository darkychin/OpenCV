"""
Add masked python logo at bottom right of doge with OpenCV
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
logo_resize = cv.resize(logo, (int(logo.shape[1]/2),int(logo.shape[0]/2)))

# Create ROI for the logo in doge
d_rows,d_cols,d_channels = doge.shape
l_rows,l_cols,l_channels = logo_resize.shape
roi = doge[(d_rows-l_rows):d_rows, (d_cols-l_cols):d_cols]

# Create mask
gray_logo = cv.cvtColor(logo_resize, cv.COLOR_BGR2GRAY)
# Note: 220 will be the threshold to convert the higher value to white,
# then in the end, inverse them altogether.
ret,mask = cv.threshold(gray_logo, 220, 255, cv.THRESH_BINARY_INV)

# Create inverse mask
mask_inverse = cv.bitwise_not(mask)

# Add the mask_inverse on top to create dst background
# Note: bitwise_and will work because black is 0,  >0 AND 0  => 0 ; >0 AND >0 => >0 (substitute by source)
dst_bg = cv.bitwise_and(roi, roi, mask=mask_inverse)

# Add the mask on top of logo to create dst foreground
dst_fg = cv.bitwise_and(logo_resize, logo_resize, mask=mask)

# Combine into one dst
dst = cv.add(dst_bg, dst_fg)

# Add the dst back to doge at the same roi
doge[(d_rows-l_rows):d_rows, (d_cols-l_cols):d_cols] = dst

# Open each processed images
cv.imshow('Logo', logo_resize)
cv.imshow('Gray Logo', gray_logo)
cv.imshow('Mask', mask)
cv.imshow('Mask Inverse', mask_inverse)
cv.imshow('Destination Background', dst_bg)
cv.imshow('Destination Foreground', dst_fg)
cv.imshow('Final Destination', dst)

# Open combined image
cv.imshow('Final Image', doge)
# When wait for 0 millisecond, it will exit with any key pressed
cv.waitKey(0)
cv.destroyAllWindows()
