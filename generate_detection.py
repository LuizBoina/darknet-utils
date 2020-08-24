import os
import shutil

# This script take darknet validation output and generate 
# a detection file for each image that have at least one class detected in that
# The format o each is class_name <left> <top> <width> <height>

# Path where new files will be saved
detection = "./detections/"
# Path where darknet detection output is locate
det_files = "./det_files/"

if os.path.exists(detection):
    shutil.rmtree(detection)
os.makedirs(detection)

with open(det_files + "/comp4_det_test_go_sign.txt") as go_det:
    for line in go_det:
        name, prob, x1, y1, x2, y2 = line.split(" ")
        width = int(float(x2) - float(x1))
        height = int(float(y2) - float(y1))
        x1, y1 = int(float(x1)), int(float(y1))
        with open(detection + name + ".txt", "a") as file:
            line = "go_sign {0} {1} {2} {3} {4}".format(prob, x1, y1, width, height)
            file.write(line)
            file.write("\n")
            file.close()
with open(det_files + "/comp4_det_test_stop_sign.txt") as stop_det:
    for line in stop_det:
        name, prob, x1, y1, x2, y2 = line.split(" ")
        width = abs(int(float(x2) - float(x1)))
        height = abs(int(float(y2) - float(y1)))
        x1, y1 = int(float(x1)), int(float(y1))
        with open(detection + name + ".txt", "a") as file:
            line = "stop_sign {0} {1} {2} {3} {4}".format(prob, x1, y1, width, height)
            file.write(line)
            file.write("\n")
            file.close()
