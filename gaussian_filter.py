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
sigma = float(input("Enter sigma (e.g., 1.5): "))

if filter_size % 2 ==0:
    filter_size  += 1

def gaussian_kernel(size,sigma):
    kernel = np.fromfunction(lambda x,y: (1/(2*np.pi*sigma*2))*np.exp(-((x-(size-1)/2)*2 + (y - (size - 1 )/2)*2)/(2*sigma **2)),(size,size))
    return kernel/np.sum(kernel)

gaussian_filter_kernel = gaussian_kernel(filter_size,sigma)

g_filtered_image = convolve2d(n_img,gaussian_filter_kernel,mode = 'same',boundary = 'symm')

plt.figure()
plt.subplot(221)
plt.title("Salt and pepper image")
plt.imshow(n_img,cmap = "gray")
plt.axis("off")

plt.subplot(222)
plt.title("Guassian filtered image")
plt.imshow(g_filtered_image,cmap = "gray")
plt.axis("off")
plt.show()