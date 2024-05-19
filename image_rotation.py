import numpy as np
import matplotlib.pyplot as plt
import math

PATH = "lenna.jpg"
img = plt.imread(PATH)

angle = float(input("Enter angle(in degrees): "))

def rotate(img,angle):
    rads = math.radians(angle)
    rot_img = np.uint8(np.zeros(img.shape))
    h = rot_img.shape[0]
    w = rot_img.shape[1]
    mx = w//2
    my = h//2
    for i in range(rot_img.shape[0]):
        for j in range(rot_img.shape[1]):
            x= (i-mx)*math.cos(rads)+(j-my)*math.sin(rads)
            y= -(i-mx)*math.sin(rads)+(j-my)*math.cos(rads)

            x=round(x)+mx 
            y=round(y)+my 

            if (x>=0 and y>=0 and x<img.shape[0] and  y<img.shape[1]):
                rot_img[i,j] = img[x,y]
    return rot_img

rot_img = rotate(img,angle)

plt.imshow(rot_img)
plt.axis("off")
plt.show()