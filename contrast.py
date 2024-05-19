import numpy as np
import matplotlib.pyplot as plt

PATH = "lenna.jpg"
img = plt.imread(PATH)
img = np.dot(img,np.array([0.28,0.59,0.11]))

uniques,counts = np.unique(img,return_counts=True)
min = np.min(counts)
max = np.max(counts)

print(f"Contrast = {max-min}")