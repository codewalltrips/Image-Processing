import numpy as np
import matplotlib.pyplot as plt

PATH = "lenna.jpg"
img = plt.imread(PATH)
weights = np.array([0.28,0.59,0.11])
g_img = np.dot(img,weights)
plt.imshow(g_img)
plt.axis("off")
plt.show()


plt.hist(g_img.flatten())
plt.show()