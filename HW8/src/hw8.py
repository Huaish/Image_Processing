import argparse
import numpy as np
import cv2


def otsu_thresholding(image_file):
    """
    Otsu's thresholding method
    :param image_file: image file
    :return: thresholded image
    """
    # load image and convert to grayscale
    img = cv2.imread(image_file, cv2.IMREAD_GRAYSCALE)

    # get histogram of image
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])

    # get total number of pixels
    total = img.shape[0] * img.shape[1]

    # initialize variables
    varMax = 0  # maximum variance
    threshold = 0

    # loop through all possible thresholds
    for t in range(256):
        # calculate weights
        wB = np.sum(hist[:t]) / total
        wF = np.sum(hist[t:]) / total

        # calculate means
        mB = np.sum([i * hist[i] for i in range(t)]) / np.where(np.sum(hist[:t]) == 0, 1, np.sum(hist[:t]))
        mF = np.sum([i * hist[i] for i in range(t, 256)]) / np.where(np.sum(hist[t:]) == 0, 1, np.sum(hist[t:]))

        # calculate variance
        var = wB * wF * (mB - mF) ** 2

        # update threshold if variance is greater than current maximum
        if var > varMax:
            varMax = var
            threshold = t

    # threshold image
    ret, thresh_img = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)

    return thresh_img


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', type=str, default='apple.jpeg', help='path to the image')
    args = parser.parse_args()
    input_file = args.image
    output_file = input_file.split('.')[0] + '_thresh.' + input_file.split('.')[1]

    thresh_img = otsu_thresholding(args.image)
    cv2.imwrite(output_file, thresh_img)
