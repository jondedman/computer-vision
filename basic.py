import cv2 as cv

# img = cv.imread('./Resources/Photos/cat.jpg')

# cv.imshow('Cat', img)

# convert to grayscale

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('img', img) # displays the image in color
# cv.imshow('Gray', gray) # displays the image in grayscale

# park in color
park = cv.imread('./Resources/Photos/park.jpg')
cv.imshow('Park', park)

# convert to grayscale
gray_park = cv.cvtColor(park, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Park', gray_park)

# Blur an image
# Gaussian blur
# blur = cv.GaussianBlur(park, (7, 7), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

# Edge Cascade
# canny = cv.Canny(park, 125, 175)
# blur_canny = cv.Canny(blur, 125, 175)
# cv.imshow('Canny Edges', canny)
# cv.imshow('Blur Canny Edges', blur_canny)

# Dilating the image
# dilated = cv.dilate(blur_canny, (7, 7), iterations=3)
# cv.imshow('Dilated', dilated)

# eroding
# eroded = cv.erode(dilated, (7, 7), iterations=3)
# cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(park, (500, 500), interpolation=cv.INTER_AREA)
cv.imshow('Resized', resized)

# Cropping
cropped = park[50:200, 200:400]
cv.imshow('Cropped', cropped)



cv.waitKey(0) # waits for a key to be pressed before closing the window
