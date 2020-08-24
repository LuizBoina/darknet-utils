import os
import shutil

images_path = "/home/luizboina/aruco_yolo_benchmark/yolo/data/dataset/train/"
detection_path = "/home/luizboina/aruco_yolo_benchmark/yolo/scripts/detections"
file_names = [images_path + file for file in os.listdir(detection_path)]

for f in enumerate(file_names, 1):
    file_name = f[1].split("/")
    file_name = file_name[-1]
    dest = os.path.join("/home/luizboina/aruco_yolo_benchmark/yolo/scripts/groundtruths", file_name)
    shutil.copy(f[1], dest)

