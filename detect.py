import cv2
import numpy as np

# Define the dimensions of the white image
width = 1000
height = 500

# Create a white image
img = np.ones((height, width, 3), dtype=np.uint8) * 255

# Define the four points
area1_pointA = (210, 350)
area1_pointB = (433, 350)
area1_pointC = (165, 400)
area1_pointD = (460, 400)

# Define the color and radius for the plotted points
color1 = (0, 0, 0)  # Black color
color2 = (0, 0, 255)  # Black color
color3 = (0, 255, 0)  # Black color
color4 = (255, 0, 0)  # Black color
radius = 5

# Plot the four points on the white image
cv2.circle(img, area1_pointA, radius, color1, -1)
cv2.circle(img, area1_pointB, radius, color2, -1)
cv2.circle(img, area1_pointC, radius, color3, -1)
cv2.circle(img, area1_pointD, radius, color4, -1)

# Display the image
cv2.imshow('White Image with Plotted Points', img)
cv2.waitKey(0)