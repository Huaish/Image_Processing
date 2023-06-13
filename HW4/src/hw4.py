import numpy as np
import cv2
import argparse


# argument parser
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', type=str,
                        default='img/apple.jpeg', help='path to the image')
    parser.add_argument('-o', '--output', type=str,
                        default='output', help='name of the output image')
    parser.add_argument('-t', '--type', type=str, default='',
                        help='type of the output image')
    parser.add_argument('-n', '--n', type=int, default=35,
                        help='size of the mask')
    parser.add_argument('-k', '--scale', type=int, default=0.7,
                        help='scale of the image')
    args = parser.parse_args()
    if(args.output == ''): args.output = args.image.split('/')[-1].split('.')[0]
    if(args.type == ''): args.type = args.image.split('.')[-1]
    return args

def average_blur(img, n):
    mask = np.ones((n, n))
    mask = mask / (n*n)
    img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    img_yuv[:, :, 0] = cv2.filter2D(img_yuv[:, :, 0], -1, mask)
    blurred = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

    return blurred

def median_blur(img, n):
    # padding img
    img_pad = np.pad(img, ((n//2, n//2), (n//2, n//2), (0, 0)), 'edge')
    img_yuv = cv2.cvtColor(img_pad, cv2.COLOR_BGR2YUV)

    height, width = img.shape[:2]
    blurred_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

    for i in range(height):
        for j in range(width):
            blurred_yuv[i, j, 0] = np.median(img_yuv[i:i+n, j:j+n, 0])

    blurred = cv2.cvtColor(blurred_yuv.astype(np.uint8), cv2.COLOR_YUV2BGR)

    return blurred



args = parse_args()

img = cv2.imread(args.image, cv2.IMREAD_COLOR)
# img = cv2.imread(args.image, cv2.IMREAD_GRAYSCALE)
n = args.n
k = args.scale

# unsharp masking using average filter
average_burred = cv2.blur(img, (n, n))
# average_burred = average_blur(img, n)
# high_pass = (img/255 - average_burred/255) * 255
high_pass = cv2.subtract(img, average_burred)
average_sharp = img + k * high_pass

# unsharp masking using median filter
# median_burred = cv2.medianBlur(img, n)
median_burred = median_blur(img, n)
high_pass = (img/255 - median_burred/255) * 255
median_sharp = img + k * high_pass


# save the images
cv2.imwrite(args.output + '_original.' + args.type, img)
cv2.imwrite(args.output + '_average_burred.' + args.type, average_burred)
cv2.imwrite(args.output + '_median_burred.' + args.type, median_burred)
cv2.imwrite(args.output + '_average_sharp.' + args.type, average_sharp)
cv2.imwrite(args.output + '_median_sharp.' + args.type, median_sharp)