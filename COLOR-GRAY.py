import cv2
import numpy as np
import matplotlib.pyplot as plt

image = plt.imread("oip.jpeg")

print(image.shape)


def grayscale(image):
    gray_image = np.dot(image[..., :3], [0.28, 0.59, 0.11])
    return gray_image


def negative(gray_image):
    negative_image = 255 - gray_image
    return negative_image


gray = grayscale(image)
plt.imshow(gray, cmap="gray")
plt.show()
plt.imshow(negative(gray), cmap="gray")
plt.show()
