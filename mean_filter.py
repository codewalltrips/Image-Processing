import matplotlib.pyplot as plt
import numpy as np
import random
from scipy.signal import convolve2d

PATH = "lenna.jpg"

img = plt.imread(PATH)
ratios = np.array([0.28,0.59,0.10])
if img.shape[-1] == 3:
    img = img@ratios
r,c = img.shape
n_img = img

n_pnts_black = random.randint(950,10000)
for i in range(n_pnts_black):
    x = random.randint(1,r-1)
    y = random.randint(1,c-1)
    n_img[x][y] = 255

n_pnts_white = random.randint(950,10000)
for i in range(n_pnts_black):
    x = random.randint(1,r-1)
    y = random.randint(1,c-1)
    n_img[x][y] = 0

filter_size = int(input("Enter filter size (odd integer): "))

if filter_size % 2 ==0:
    filter_size  += 1
    
def MeanFilter(image, filter_size):

    output = np.zeros(image.shape, np.uint8)
    result = 0
    if filter_size == 9:
        for j in range(1, image.shape[0]-1):
            for i in range(1, image.shape[1]-1):
                for y in range(-1, 2):
                    for x in range(-1, 2):
                        result = result + image[j+y, i+x]
                output[j][i] = int(result / filter_size)
                result = 0

    elif filter_size == 25:
        for j in range(2, image.shape[0]-2):
            for i in range(2, image.shape[1]-2):
                for y in range(-2, 3):
                    for x in range(-2, 3):
                        result = result + image[j+y, i+x]
                output[j][i] = int(result / filter_size)
                result = 0
    return output

m_filtered_image = MeanFilter(n_img,9)
plt.figure()
plt.subplot(221)
plt.title("Salt and pepper image")
plt.imshow(n_img,cmap = "gray")
plt.axis("off")

plt.subplot(222)
plt.title("Mean filtered Image")
plt.imshow(m_filtered_image,cmap = "gray")
plt.axis("off")
plt.show()