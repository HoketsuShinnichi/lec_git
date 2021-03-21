import matplotlib.pyplot as plt
import cv2

img = cv2.imread("Lenna.jpg")

orgHeight, orgWidth = img.shape[:2]
size=(orgHeight//2,orgWidth//2)

plt.axis("off")
#img1 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img2 = cv2.resize(img,size)
plt.imshow(img2)
