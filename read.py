import cv2 as cv

# Load an image using 'imread' specifying the path to image

img = cv.imread('./Resources/Photos/cat_large.jpg')

# Display the image using 'imshow'
cv.imshow('Cat', img)

# reading videos






# Capture a video using 'VideoCapture' specifying the path to video
capture = cv.VideoCapture('./Resources/Videos/dog.mp4')

# Loop through the video frame by frame
while True:
    (isTrue, frame) = capture.read()
    cv.imshow('Video', frame)

    # If the 'b' key is pressed, break from the loop
    if cv.waitKey(20) & 0xFF == ord('b'):
        break

# Release the video capture object
capture.release()

# Wait for a key event and close the window
cv.waitKey(0)
