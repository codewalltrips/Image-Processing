import numpy as np
import matplotlib.pyplot as plt

PATH = "lenna.jpg"
img = plt.imread(PATH)

plt.imshow(img)
plt.axis("off")
plt.show()

# Image Translation 
x = int(input("Enter new X-coordinate for the origin: "))
y = int(input("Enter new Y-coordinate for the origin: "))
img_t = np.zeros(img.shape, dtype =np.uint8)

for i in range(img_t.shape[0]):
    for j in range(img_t.shape[1]):
        if i>=x and j>=y:
            img_t[i][j] = img[i-x][j-y]

plt.imshow(img_t)
plt.axis("off")
plt.show()