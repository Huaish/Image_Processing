import cv2
import numpy as np

# Lantuejoul’s  skeletonization method using 3x3 structuring element B
def skeletonize(img, element):
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

    return skel


if __name__ == '__main__':
    # Read image
    img = cv2.imread('input.png', cv2.IMREAD_GRAYSCALE)

    # Create structuring element B1, B2
    B1= np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], dtype=np.uint8)
    B2 = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]], dtype=np.uint8)
    
    # Apply Lantuejoul’s  skeletonization
    skel_1 = skeletonize(img,B1)
    skel_2 = skeletonize(img,B2)

    # save image
    cv2.imwrite("skel_1.png", skel_1)
    cv2.imwrite("skel_2.png", skel_2)

