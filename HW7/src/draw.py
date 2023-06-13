from PIL import Image
from PIL import ImageOps
from matplotlib import pyplot as plt
import numpy as np

# 開啟圖片
img = Image.open('noise.png')

# # 均衡化直方圖處理
# img_eq = ImageOps.equalize(img)

# 轉換為灰度圖像
img_eq_gray = img.convert("L")

# 獲取像素值列表
pixel_values = list(img_eq_gray.getdata())

# 繪製直方圖
# plt.hist(pixel_values, bins=256, range=(0, 256), density=True)
hist, bins = np.histogram(pixel_values, bins=256, range=(0, 256), density=True)

# 顯示圖像
plt.bar(bins[:-1], hist, width=(bins[1]-bins[0]))
plt.ylim(0, 0.02)
plt.show()

