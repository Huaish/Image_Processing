from PIL import Image
from PIL import ImageOps
from matplotlib import pyplot as plt
import argparse
import numpy as np

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

# 開啟圖片
img = Image.open('default_color_he.jpeg')

# # 均衡化直方圖處理
# img_eq = ImageOps.equalize(img)

# 轉換為灰度圖像
img_eq_gray = img.convert("L")

# 獲取像素值列表
pixel_values = list(img_eq_gray.getdata())

# 繪製直方圖
# plt.hist(pixel_values, bins=256, range=(0, 256), density=True)
hist, bins = np.histogram(pixel_values, bins=256, range=(0, 256), density=True)
print(hist)

# 顯示圖像
plt.bar(bins[:-1], hist, width=(bins[1]-bins[0]))
plt.ylim(0, 0.02)
plt.show()

