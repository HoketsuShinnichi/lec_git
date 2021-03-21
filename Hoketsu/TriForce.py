import cv2
import numpy as np

image = np.ones((300, 300, 3), np.uint8) * 255

plt.axis("off")

pt1 = (150, 1)
pt2 = (1, 200)
pt3 = (300, 200)

pt4 = (75 ,100)
pt5 = (225, 100)
pt6 = (150, 200)

cv2.circle(image, pt1, 2, (0,0,255), -1)
cv2.circle(image, pt2, 2, (0,0,255), -1)
cv2.circle(image, pt3, 2, (0,0,255), -1)

cv2.circle(image, pt4, 2, (0,0,255), -1)
cv2.circle(image, pt5, 2, (0,0,255), -1)
cv2.circle(image, pt6, 2, (0,0,255), -1)

triangle_cnt = np.array( [pt1, pt2, pt3] )
triangle_cnt2 = np.array( [pt4, pt5, pt6] )

cv2.drawContours(image, [triangle_cnt], 0, (255,255,0), -1)
cv2.drawContours(image, [triangle_cnt2], 0, (0,0,0), -1)

plt.imshow(image)
cv2.waitKey()
