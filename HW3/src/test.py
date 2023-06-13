import numpy as np
import cv2

#Load color image
img = cv2.imread('img/jpg_image.jpeg', cv2.IMREAD_COLOR)

# Convert color image to YUV color space
img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

# Apply HE to Y channel
img_yuv[:, :, 0] = cv2.equalizeHist(img_yuv[:, :, 0])

# Convert back to RGB color space
img_he = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)



# Show images
cv2.imshow('Original', img)
cv2.imshow('Color HE', img_he)

cv2.waitKey(0)
cv2.destroyAllWindows()