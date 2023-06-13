import numpy as np
import cv2

img = cv2.imread('input.png', cv2.IMREAD_COLOR)
rows, cols, _ = img.shape

# rotation matrix
M = cv2.getRotationMatrix2D((cols/2, rows/2), -30, 1)

# nearest neighbor interpolation
rotated_NN = cv2.warpAffine(img, M, (cols, rows), flags=cv2.INTER_NEAREST, borderValue=(100, 100, 100))

# bilinear interpolation
rotated_bilinear = cv2.warpAffine(img, M, (cols, rows), flags=cv2.INTER_LINEAR, borderValue=(100, 100, 100))

# save image
cv2.imwrite('cv2_rotated_NN.png', rotated_NN)
cv2.imwrite('cv2_rotates_bilinear.png', rotated_bilinear)