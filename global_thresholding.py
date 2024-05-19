import numpy as np
import matplotlib.pyplot as plt



image = plt.imread('lenna.jpg')  
ratios = np.array([0.28,0.59,0.10])
image = np.dot(image,ratios)


def global_thresholding(image, threshold):
    binary_image = np.where(image > threshold, 1, 0)
    return binary_image

def calculate_area_percentage(binary_image):
    total_pixels = binary_image.size
    white_pixels = np.sum(binary_image == 1)
    area_percentage = (white_pixels / total_pixels) * 100
    return area_percentage

global_threshold_value = 0.5  
global_binary_image = global_thresholding(image, global_threshold_value)
area_percentage_global = calculate_area_percentage(global_binary_image)

plt.subplot(121)
plt.imshow(image,cmap ="gray")
plt.axis("off")
plt.subplot(122)
plt.imshow(global_binary_image,cmap="gray")
plt.axis("off")
plt.show()
area_percentage_global = calculate_area_percentage(global_binary_image)
print(f"Local Thresholding Area Percentage: {area_percentage_global}%")