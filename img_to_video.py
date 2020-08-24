import cv2
import numpy as np
import glob
 
img_array = []
for filename in glob.glob('/home/luizboina/aruco_yolo_benchmark/yolo/data/obj_validacao/imgs_marks/*.JPG'):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)
 
out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'), 1, size)

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()
