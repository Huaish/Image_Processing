import cv2
import numpy as np

# Create an image consisting of a white square with a black background
img = np.zeros((800, 800, 3), np.uint8)
cv2.rectangle(img, (200, 200), (600, 600), (255, 255, 255), -1)
img_center_x, img_center_y = img.shape[1]/2, img.shape[0]/2


# create a new image to store the rotated image
rows, cols, _ = img.shape
size = int(np.sqrt(rows**2 + cols**2))
img_rotated = np.zeros((size, size, 3), np.uint8)
img_rotated.fill(100)
rotated_center_x, rotated_center_y = img_rotated.shape[1]/2, img_rotated.shape[0]/2

# Translation matrix1
translation_matrix1 = np.array([
    [1, 0, -img_center_x],
    [0, 1, -img_center_y],
    [0, 0, 1]
])

# Rotation matrix
theta = np.radians(30)
cos_theta, sin_theta = np.cos(theta), np.sin(theta) 
inverse_rotation_matrix = np.array([
    [cos_theta, sin_theta, 0],
    [-sin_theta, cos_theta, 0],
    [0, 0, 1]
])

# Translation matrix2
translation_matrix2 = np.array([
    [1, 0, rotated_center_x],
    [0, 1, rotated_center_y],
    [0, 0, 1]
])

# Matrix multiplication
M = np.dot(translation_matrix2, np.dot(inverse_rotation_matrix, translation_matrix1))


# rotate image by 30 degrees
for y in range(img.shape[0]):
    for x in range(img.shape[1]):
        # transform the pixel coordinates to the original image coordinate system
        x_org = M[0][0]*x + M[0][1]*y + M[0][2]
        y_org = M[1][0]*x + M[1][1]*y + M[1][2]
        
        # round the transformed coordinates to the nearest integer to get the pixel value from the original image
        x_org_rounded, y_org_rounded = int(round(x_org)), int(round(y_org))
        
        # set the pixel value in the rotated image
        if x_org_rounded >= 0 and x_org_rounded < img_rotated.shape[1] and y_org_rounded >= 0 and y_org_rounded < img_rotated.shape[0]:
            img_rotated[y_org_rounded][x_org_rounded] = img[y][x]


# save the rotated image
cv2.imwrite('original.png', img)
cv2.imwrite('rotate.png', img_rotated)
