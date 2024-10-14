import cv2 as cv

# Load an image using 'imread' specifying the path to image

img = cv.imread('./Resources/Photos/cat_large.jpg')
# resizing and rescaling

# Rescale the image
def rescale_frame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

capture = cv.VideoCapture('./Resources/Videos/dog.mp4')

resized_img = rescale_frame(img)

cv.imshow('Cat', img)
cv.imshow('Cat Resized', resized_img)

# Loop through the video frame by frame
while True:
    (isTrue, frame) = capture.read()
    # Rescale the frame
    frame_resized = rescale_frame(frame, 0.75)

    cv.imshow('Video', frame)
    cv.imshow('Video', frame_resized)


    # If the 'd' key is pressed, break from the loop
    if cv.waitKey(20) & 0xFF == ord('b'):
        break

# Release the video capture object
capture.release()

# resize the video

def change_res(width, height):
    # live video capture only
    capture.set(3, width)
    capture.set(4, height)

# change_res(400, 300)


cv.destroyAllWindows()
