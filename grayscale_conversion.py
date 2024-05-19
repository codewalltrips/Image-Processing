import numpy as np
import matplotlib.pyplot as plt

PATH = "lenna.jpg"
img = plt.imread(PATH)

weights = np.array([0.28,0.59,0.11])
gray_img = np.dot(img,weights)

plt.subplot(2,1,1)
plt.imshow(img)
plt.axis("off")


plt.subplot(2,1,2)
plt.imshow(gray_img,cmap = "gray")
plt.axis("off")
plt.show()