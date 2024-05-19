import numpy as np
import matplotlib.pyplot as plt
import cv2

# histogram equalization


img = cv2.imread('lenna.jpg', cv2.IMREAD_GRAYSCALE)
hist = cv2.calcHist([img], [0], None, [256], [0, 256])
cdf = np.cumsum(hist)
cdf_norm = cdf / cdf.max()
equalized_img = cdf_norm[img] * 255.0

plt.subplot(121)
plt.imshow(img, cmap='gray')
plt.title('Original Image')

plt.subplot(122)
plt.imshow(equalized_img, cmap='gray')
plt.title('Equalized Image')

plt.show()