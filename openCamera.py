# Import necessary libraries
import torch
import torchvision
import cv2

# Open the video capture
vid = cv2.VideoCapture(0)

# Set the width and height of the video capture
vid.set(3, 200)
vid.set(4, 200)

# Start an infinite loop to continuously read frames from the video capture
while True:
    # Read a frame from the video capture
    ret, frame = vid.read()

    # Flip the frame horizontally
    frame = cv2.flip(frame, 1)

    # Display the frame in a window named 'frame'
    cv2.imshow('frame', frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture
vid.release()

# Destroy all the windows
cv2.destroyAllWindows()
