import cv2
import numpy as np
import matplotlib.pyplot as plt

# Create an image g(x,y) whose pixels all have the same gray value of 100.
rows = 512
cols = 512
img = np.zeros((rows, cols), np.uint8)
img.fill(100)
noise = img.copy()

# Generate Gaussian noise n(x,y), with mean 0 and variance 25
mu = 0
sigma = 50

# for each pixel (x,y), (x,y+1) generate a pair of unipform random numbers r and phi in the range [0,1]
for i in range(0, rows):
    for j in range(0, cols-1, 2):
        r = np.random.uniform(0,1)
        phi = np.random.uniform(0,1)

        # compute z1 and z2 using the formula
        z1 = sigma * np.sqrt(-2 * np.log(r)) * np.cos(2 * np.pi * phi)
        z2 = sigma * np.sqrt(-2 * np.log(r)) * np.sin(2 * np.pi * phi)

        # add z1 to the pixel (x,y) and z2 to the pixel (x,y+1)
        noise[i,j] = np.clip(noise[i,j] + z1, 0, 255)
        noise[i,j+1] = np.clip(noise[i,j+1] + z2, 0, 255)

            
# save the image and noise
cv2.imwrite('image.png', img)
cv2.imwrite('noisy_image_' + str(sigma) + '.png', noise)

# Compute the histogram of the image g(x,y) and the histogram of the noisy image f(x,y).

plt.figure()
plt.title('Histogram of image')
plt.xlabel('Pixel value')
plt.ylabel('Probability')
plt.hist(img.ravel(), bins=256, range=(0, 256), density=True)
plt.xlim(0, 255)
plt.ylim(0, 0.1)
plt.savefig('image_histogram.png')

plt.figure()
plt.title('Histogram of noisy image')
plt.xlabel('Pixel value')
plt.ylabel('Probability')
plt.hist(noise.ravel(), bins=256, range=(0, 256), density=True)
plt.xlim(0, 255)
plt.ylim(0, 0.1)
plt.savefig('noisy_histogram_' + str(sigma) + '.png')










