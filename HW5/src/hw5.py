import cv2
import numpy as np

# Create an image consisting of a white square with a black background
src_img = np.zeros((800, 800, 3), np.uint8)
cv2.rectangle(src_img, (200, 200), (600, 600), (255, 255, 255), -1)
src_centerX, src_centerY = src_img.shape[1]/2, src_img.shape[0]/2

# create a new image to store the rotated image
src_rows, src_cols, _ = src_img.shape
rotated_size = int(np.sqrt(src_rows**2 + src_cols**2))
img_rotated_NN = np.zeros((rotated_size, rotated_size, 3), np.uint8)
img_rotated_NN.fill(100)
img_rotated_bilinear = img_rotated_NN.copy()
rotated_centerX, rotated_centerY = img_rotated_NN.shape[1]/2, img_rotated_NN.shape[0]/2

# 將旋轉中心移至新圖片的中心
translation_matrix1 = np.array([
    [1, 0, -rotated_centerX],
    [0, 1, -rotated_centerY],
    [0, 0, 1]
])

# Inverse rotation matrix
theta = np.radians(30)
cos_theta, sin_theta = np.cos(theta), np.sin(theta) 
inverse_rotation_matrix = np.array([
    [cos_theta, -sin_theta, 0],
    [sin_theta, cos_theta, 0],
    [0, 0, 1]
])

# 將旋轉中心移回原圖片的中心
translation_matrix2 = np.array([
    [1, 0, src_centerX],
    [0, 1, src_centerY],
    [0, 0, 1]
])

# Matrix multiplication
M = np.dot(translation_matrix2, np.dot(inverse_rotation_matrix, translation_matrix1))

# Rotate image by 30 degrees with nearest neighbor interpolation
for y in range(rotated_size):
    for x in range(rotated_size):
        # transform the pixel coordinates to the original image coordinate system
        x_org = M[0][0]*x + M[0][1]*y + M[0][2]
        y_org = M[1][0]*x + M[1][1]*y + M[1][2]
        
        # round the transformed coordinates to the nearest integer to get the pixel value from the original image
        x_org_rounded, y_org_rounded = int(round(x_org)), int(round(y_org))
        
        # set the pixel value in the rotated image
        if x_org_rounded >= 0 and x_org_rounded < src_cols and y_org_rounded >= 0 and y_org_rounded < src_rows:
            img_rotated_NN[y][x] = src_img[y_org_rounded][x_org_rounded]
            

# Rotate image by 30 degrees with bilinear interpolation
for y in range(rotated_size):
    for x in range(rotated_size):
        
        # transform the pixel coordinates to the original image coordinate system
        x_org = M[0][0]*x + M[0][1]*y + M[0][2]
        y_org = M[1][0]*x + M[1][1]*y + M[1][2]
        
        # get the pixel value from the original image
        x_org_floor, y_org_floor = int(np.floor(x_org)), int(np.floor(y_org))
        x_org_ceil, y_org_ceil = int(np.ceil(x_org)), int(np.ceil(y_org))
        
        # set the pixel value in the rotated image
        if x_org_floor >= 0 and x_org_ceil < src_img.shape[1] and y_org_floor >= 0 and y_org_ceil < src_img.shape[0]:
            img_rotated_bilinear[y][x] = (x_org_ceil-x_org)*(y_org_ceil-y_org)*src_img[y_org_floor][x_org_floor] + \
                                (x_org_ceil-x_org)*(y_org-y_org_floor)*src_img[y_org_ceil][x_org_floor] + \
                                (x_org-x_org_floor)*(y_org_ceil-y_org)*src_img[y_org_floor][x_org_ceil] + \
                                (x_org-x_org_floor)*(y_org-y_org_floor)*src_img[y_org_ceil][x_org_ceil]

# save the rotated images
cv2.imwrite('original.png', src_img)
cv2.imwrite('rotated_NN.png', img_rotated_NN)
cv2.imwrite('rotated_bilinear.png', img_rotated_bilinear)
