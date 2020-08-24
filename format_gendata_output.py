import os
import shutil

train = "./train/"
gendata_out = "./train.csv"
image_width = 640
image_height = 480
if os.path.exists(train):
    shutil.rmtree(train)
os.makedirs(train)

with open(gendata_out) as file:
    for line in file:
        file_path, x1, y1, x2, y2, obj = line.split(",")
        name = file_path.split("/")[2][:-4]
        x1, y1, x2, y2 = float(x1), float(y1), float(x2), float(y2)
        abs_x = (x1 + x2) / (2 * image_width)
        abs_y = (y1 + y2) / (2* image_height)
        abs_w = (x2 - x1) / image_width
        abs_h = (y2 - y1) / image_height
        label = ""
        if obj.rstrip() == "stop":
            label = "0"
        else:
            label = "1"
        with open(train + name + ".txt", "a") as file:
            line = "{0} {1} {2} {3} {4}".format(label, abs_x, abs_y, abs_w, abs_h)
            file.write(line)
            file.write("\n")