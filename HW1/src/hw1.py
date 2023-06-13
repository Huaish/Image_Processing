import cv2
import numpy as np
import argparse

# parse the command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--image', type=str,
                    default='jpg_image.jpg', help='path to the image')
parser.add_argument('-o', '--output', type=str,
                    default='output', help='name of the output image')
parser.add_argument('-t', '--type', type=str, default='jpg',
                    help='type of the output image')
args = parser.parse_args()


# Read the image
img = cv2.imread(args.image)
cv2.imwrite(args.output + '_color.' + args.type, img)

# Convert the image to grayscale
# Method 1: using numpy
# Convert to grayscale using the formula I = (R+G+B)/3
# gray = np.zeros((img.shape[0], img.shape[1]), dtype=np.uint8)
# for i in range(img.shape[0]):
#     for j in range(img.shape[1]):
#         gray[i,j] = np.sum(img[i,j]) // 3

# Method 2: using cv2.cvtColor
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# show the image
# cv2.imshow('image', gray)
# cv2.waitKey(0)

# Output the image
cv2.imwrite(args.output + '_grayscale.' + args.type, img)
