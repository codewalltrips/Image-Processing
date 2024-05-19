import numpy as np
import matplotlib.pyplot as plt



image = plt.imread('lenna.jpg')  
ratios = np.array([0.28,0.59,0.10])
image = np.dot(image,ratios)


def local_thresholding(image, block_size, constant):
    binary_image = np.zeros_like(image, dtype=int)
    for i in range(0, image.shape[0], block_size):
        for j in range(0, image.shape[1], block_size):
            block = image[i:i+block_size, j:j+block_size]
            threshold = np.mean(block) + constant
            binary_image[i:i+block_size, j:j+block_size] = np.where(block > threshold, 1, 0)
    return binary_image

def calculate_area_percentage(binary_image):
    total_pixels = binary_image.size
    white_pixels = np.sum(binary_image == 1)
    area_percentage = (white_pixels / total_pixels) * 100
    return area_percentage


block_size = 10
constant = 0.03  
local_binary_image = local_thresholding(image, block_size, constant)
plt.subplot(121)
plt.imshow(image,cmap ="gray")
plt.axis("off")
plt.subplot(122)
plt.imshow(local_binary_image,cmap="gray")
plt.axis("off")
plt.show()
area_percentage_local = calculate_area_percentage(local_binary_image)
print(f"Local Thresholding Area Percentage: {area_percentage_local}%")
