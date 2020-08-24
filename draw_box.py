# draw bbox using x, y, w, h

import cv2

img_path = "09999_000000135539.jpg"
txt_path = "./IMG_18.txt"
img = cv2.imread(img_path)
cv2.rectangle(img, (25,333), (119,460), (0, 255, 0), 3)
cv2.imshow("test", img)
cv2.waitKey(0)