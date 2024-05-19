import numpy as np
import matplotlib.pyplot as plt



image = plt.imread('lenna.jpg')  
ratios = np.array([0.28,0.59,0.10])
image = np.dot(image,ratios)


def apply_operator(image, operator):
    result = np.abs(np.convolve(image.flatten(), operator.flatten(), mode='same').reshape(image.shape))
    return result

sobel_operator_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
sobel_operator_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
sobel_x = apply_operator(image, sobel_operator_x)
sobel_y = apply_operator(image, sobel_operator_y)
sobel_edges = np.sqrt(sobel_x**2 + sobel_y**2)

plt.subplot(121)
plt.imshow(image,cmap = "gray")
plt.axis("off")
plt.subplot(122)
plt.imshow(sobel_edges,cmap ="gray")
plt.axis("off")
plt.show()