import numpy as np
import matplotlib.pyplot as plt



image = plt.imread('lenna.jpg')  
ratios = np.array([0.28,0.59,0.10])
image = np.dot(image,ratios)


def apply_operator(image, operator):
    result = np.abs(np.convolve(image.flatten(), operator.flatten(), mode='same').reshape(image.shape))
    return result


kirsch_operator_1 = np.array([[-3, -3, 5], [-3, 0, 5], [-3, -3, 5]])
kirsch_operator_2 = np.array([[-3, 5, 5], [-3, 0, 5], [-3, -3, -3]])
kirsch_operator_3 = np.array([[5, 5, 5], [-3, 0, -3], [-3, -3, -3]])
kirsch_operator_4 = np.array([[5, 5, -3], [5, 0, -3], [-3, -3, -3]])
kirsch_edges = np.maximum.reduce([apply_operator(image, op) for op in [kirsch_operator_1, kirsch_operator_2, kirsch_operator_3, kirsch_operator_4]])

plt.subplot(121)
plt.imshow(image,cmap = "gray")
plt.axis("off")
plt.subplot(122)
plt.imshow(kirsch_edges,cmap ="gray")
plt.axis("off")
plt.show()