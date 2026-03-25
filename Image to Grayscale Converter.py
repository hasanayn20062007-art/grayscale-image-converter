import numpy as np , matplotlib.pyplot as plt , matplotlib.image as mpimg
ph = mpimg.imread("Hasanayn .jpeg")
print(ph.shape)
r = ph[:,:,0]
g = ph[:,:,1]
b = ph[:,:,2]
print(r.shape)
gray_img = r*0.299 + g*0.587 + b*0.114
print(gray_img.shape)
plt.imshow(gray_img , cmap='gray')
plt.axis('off') 
plt.show()