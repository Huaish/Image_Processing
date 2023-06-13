import cv2
import numpy as np

# Read image
img = cv2.imread('input.png', cv2.IMREAD_GRAYSCALE)

# Create structuring element
element = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], dtype=np.uint8)

# Apply Lantuejoul’s  skeletonization
_, img = cv2.threshold(img,127,255,0)
size = np.size(img)
skel = np.zeros(img.shape, np.uint8)

while True:
    eroded = cv2.erode(img, element)
    temp = cv2.dilate(eroded, element)
    temp = cv2.subtract(img, temp)
    skel = cv2.bitwise_or(skel, temp)
    img = eroded.copy()

    zeros = size - cv2.countNonZero(img)
    if zeros == size:
        break

# save image
cv2.imwrite("skel.png", skel)
