import numpy as np
import matplotlib.pyplot as plt

PATH = "lenna.jpg"
img = plt.imread(PATH)
plt.imshow(img)
#plt.axis("off")
plt.show()

size = int(input("Enter padding size: "))
img_p = np.zeros(shape=(img.shape[0]+2*size,img.shape[1]+2*size,img.shape[2]),dtype = np.uint8)

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        img_p[i+size][j+size] = img[i][j]

plt.imshow(img_p)
#plt.axis("off")
plt.show()