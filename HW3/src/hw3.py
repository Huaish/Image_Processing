import numpy as np
import cv2
import argparse

# parse the command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--image', type=str,
                    default='img/art4.jpeg', help='path to the image')
parser.add_argument('-o', '--output', type=str,
                    default='output', help='name of the output image')
parser.add_argument('-t', '--type', type=str, default='',
                    help='type of the output image')
args = parser.parse_args()

if(args.output == ''): args.output = args.image.split('/')[-1].split('.')[0]
if(args.type == ''): args.type = args.image.split('.')[-1]


#Load color image and save original
img = cv2.imread(args.image, cv2.IMREAD_COLOR)
cv2.imwrite(args.output + '_original.' + args.type, img)

#Convert to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply HE to Grayscale image
img_gray_he = cv2.equalizeHist(img_gray)


# apply HE to color image for each channel
img_he = img.copy()
for i in range(3):
    img_he[:, :, i] = np.clip(img_he[:, :, i] * (img_gray_he / img_gray), 0, 255)

img_he = np.clip(img_he, 0, 255)


# save images
cv2.imwrite(args.output + '_grayscale.' + args.type, img_gray)
cv2.imwrite(args.output + '_grayscale_he.' + args.type, img_gray_he)
cv2.imwrite(args.output + '_color_he.' + args.type, img_he)


# Show images
# cv2.imshow('Original', img)
# cv2.imshow('Grayscale', img_gray)
# cv2.imshow('Grayscale HE', img_gray_he)
# cv2.imshow('Color HE', img_he)

# cv2.waitKey(0)
# cv2.destroyAllWindows()