# Import Libraries
import matplotlib.pyplot as plt
import cv2
import numpy as np

baboon = cv2.imread("baloon.jpg")
plt.figure(figsize=(10,10))
plt.imshow(cv2.cvtColor(baboon, cv2.COLOR_BGR2RGB))
plt.show()

B = baboon.copy()


##################################################################################
# Fliping Images


A = cv2.imread("cat.png")
image =A.copy()
plt.figure(figsize=(10,10))
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()

h = image.shape[0]
w = image.shape[1]

# loop over the image, pixel by pixel
for y in range(0, h):
	for x in range(0, w):
    		# threshold the pixel
    		image[y, x] =  0

im = np.zeros((w, h, 3), dtype=np.uint8)

for y in range(0, h):
	for x in range(0, w):
#    		threshold the pixel
    		im[x, y] =  A[y,x]

plt.figure(figsize=(10,10))
plt.imshow(cv2.cvtColor(im, cv2.COLOR_BGR2RGB))
plt.show()

print(image.type())



