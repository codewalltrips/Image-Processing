import numpy as np
import matplotlib.pyplot as plt

PATH = "lenna.jpg"
img = plt.imread(PATH)
ratios = np.array([0.28, 0.59, 0.10])
gray_img = np.dot(img, ratios)
inv_gray_img = np.zeros(img.shape, dtype=np.uint8)
for i in range(gray_img.shape[0]):
    for j in range(gray_img.shape[1]):
        inv_gray_img[i][j] = 255 - gray_img[i][j]

plt.subplot(121)
plt.title("Grayscale Image")
plt.imshow(gray_img, cmap="gray")
plt.axis("off")

plt.subplot(122)
plt.title("Inverted grayscale Image")
plt.imshow(inv_gray_img, cmap="gray")
plt.axis("off")
plt.show()
