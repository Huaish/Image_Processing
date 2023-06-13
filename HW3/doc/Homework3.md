# Homework No.3

Student ID: 41047902S Name: 鄭淮薰

## Problem Statement

1. Develop a histogram equalization (HE) program

2. Apply the HE to (i) gray, (ii) color images

3. For each input image, print out the input/output images and their histograms

4. Discuss your experiments.

    For a color image C,

    (i)       Convert it into a gray image G

    (ii)      Apply HE to G to get G’

    (iii)     For each pixel of C, modify its color $(r,g,b)$ by $ (r’,g’,b’) = (r,g,b) \times G’ / G.$

## Input / Output

Using python to run this program, and here are some parameters user can use to specify the input and output

```shell
usage: hw3.py [-h] [-i IMAGE] [-o OUTPUT] [-t TYPE]
options:
  -h,        --help           | show this help message and exit
  -i IMAGE,  --image IMAGE    | path to the image
  -o OUTPUT, --output OUTPUT  | name of the output image
  -t TYPE,   --type           | TYPE  type of the output image
```

## Test Results

Test case 1 將 Fig1.1 作為輸入來實作 histogram equalization。首先將輸入圖片轉成灰階，如 Fig1.2 所示，而 Fig1.3 與 Fig1.4 分別為灰階圖像及彩色圖像的 HE 圖片。從 Fig1.2 及 Fig1.3 的比較中可觀察到 Fig1.3 較 Fig1.2 要亮、對比度更明顯；同樣地，Fig1.4 也相較原圖 Fig1.1 呈現更鮮明的特徵。

| Fig1.1 Input / Original                                                              | Fig1.4 Color HE                                                                         |
|:------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------:|
| ![](/Users/huaish/Desktop/111-2/Image_Processing/HW3/doc/img/default_original.jpeg)  | ![](/Users/huaish/Desktop/111-2/Image_Processing/HW3/doc/img/default_color_he.jpeg)     |
| **Fig1.2 GraySacle**                                                                 | **Fig1.3 GrayScale HE**                                                                 |
| ![](/Users/huaish/Desktop/111-2/Image_Processing/HW3/doc/img/default_grayscale.jpeg) | ![](/Users/huaish/Desktop/111-2/Image_Processing/HW3/doc/img/default_grayscale_he.jpeg) |

## Comment & Discuss

這項作業中我使用 `cv2` 的 `equalizeHist` 函式將灰階圖像做 histogram equalization，最後再使用題目敘述的公式將彩色圖像做 histogram equalization。其中，由於 $G'/G$ 之值會超過 1，使部分 rgb 在轉換時會 overflow，造成轉換後的彩色圖片有許多不自然的綠色區塊，因此我使用 `np.clip` 方法，將轉換後的值限制於 0 ~ 255 之間，避免 overflow 的狀況發生。另外，我也匯出個圖片之 Histogram 以進行比較和觀察。從下方圖表可以看出，圖片未做均衡化處理前數值偏低( Fig1.5, Fig1.6 )，i.e. 圖片偏暗，而在做均衡化處理後( Fig1.7, Fig1.8 )，數值均勻分佈，i.e. 圖片對比較高。這些現象皆與上述圖片結果一致。

| Fig1.5 Original Histogram                                                   | Fig1.8 Color HE Histogram                                                      |
|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| ![](/Users/huaish/Desktop/111-2/Image_Processing/HW3/doc/img/color.png)     | ![](/Users/huaish/Desktop/111-2/Image_Processing/HW3/doc/img/color_he.png)     |
| **Fig1.6 GrayScale Histogram**                                              | **Fig1.7 GrayScale HE Histogram**                                              |
| ![](/Users/huaish/Desktop/111-2/Image_Processing/HW3/doc/img/grayscale.png) | ![](/Users/huaish/Desktop/111-2/Image_Processing/HW3/doc/img/grayscale_he.png) |

<div STYLE="page-break-after: always;"></div>

## Source Code

```python
import numpy as np
import cv2
import argparse

# parse the command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--image', type=str,
                    default='img/default.jpeg', help='path to the image')
parser.add_argument('-o', '--output', type=str,
                    default='', help='name of the output image')
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
```
