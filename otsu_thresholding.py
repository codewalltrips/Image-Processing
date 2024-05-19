import numpy as np
import matplotlib.pyplot as plt



image = plt.imread('lenna.jpg')  
ratios = np.array([0.28,0.59,0.10])
image = np.dot(image,ratios)

def calculate_area_percentage(binary_image):
    total_pixels = binary_image.size
    white_pixels = np.sum(binary_image == 1)
    area_percentage = (white_pixels / total_pixels) * 100
    return area_percentage

def otsu_thresholding(image):

    bins = 256  
    hist, _ = np.histogram(image.flatten(), bins=bins, density=True)
    variances = []

    for i in range(1, bins - 1):
        t = i
        w0 = np.sum(hist[:i])
        w1 = np.sum(hist[i:])
        mu0 = np.sum(np.arange(0, t) * hist[:i]) / (w0 + 1e-10)  
        mu1 = np.sum(np.arange(t, bins) * hist[i:]) / (w1 + 1e-10)  
        variances.append(w0 * w1 * (mu0 - mu1)**2)

    optimal_threshold = np.argmax(variances)
    binary_image = np.where(image > optimal_threshold, 1, 0)

    return binary_image

otsu_binary_image = otsu_thresholding(image)
area_percentage_otsu = calculate_area_percentage(otsu_binary_image)

plt.subplot(121)
plt.imshow(image,cmap ="gray")
plt.axis("off")
plt.subplot(122)
plt.imshow(otsu_binary_image,cmap="gray")
plt.axis("off")
plt.show()
area_percentage_global = calculate_area_percentage(otsu_binary_image)
print(f"Local Thresholding Area Percentage: {area_percentage_otsu}%")
