import numpy as np
import matplotlib.pyplot as plt

PATH = "lenna.jpg"
img = plt.imread(PATH)

uniques, counts = np.unique(img, return_counts=True)
min = np.min(counts)
max = np.max(counts)
p = ((counts - min) / (max - min)) * 255
p = p * np.log2(p)
p = p[~np.isnan(p)]
entropy = -1 * np.sum(p)

print("Entropy of image is: {entropy}")
