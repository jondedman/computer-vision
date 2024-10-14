import cv2 as cv
import numpy as np

#  blank image

blank = np.zeros((500, 500, 3), dtype='uint8')
# Load an image using 'imread' specifying the path to image
img = cv.imread('./Resources/Photos/cat.jpg')

# Display the image using 'imshow'
# cv.imshow('Cat', img)
# cv.imshow('Blank', blank)

# paint the image a certain color
# blank[200:300, 300:400] = 0, 0, 255

# cv.imshow('Red', blank)

# Draw a rectangle
# cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=2)
# filled rectangle
# cv.rectangle(blank, (0, 0), (250, 500), (0, 255, 0), thickness=cv.FILLED)
# divide proportions using floor division to get the center
# cv.rectangle(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (0, 255, 0), thickness=cv.FILLED)


# cv.imshow('Rectangle', blank)

# Draw a circle

# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0, 0, 255), thickness=-1)

# cv.imshow('Circle', blank)

# Draw a line

# cv.line(blank, (0, 0), (400, 400), (255, 255, 255), thickness=3)

# cv.imshow('Line', blank)

# Write text on an image

cv.putText(blank, 'Hello, my name is Jon', (0, 225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), 2)

cv.imshow('Text', blank)

cv.waitKey(0)
