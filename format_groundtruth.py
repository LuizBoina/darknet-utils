from PIL import Image
import os

imgs_path = "/home/luizboina/aruco_yolo_benchmark/yolo/data/dataset/train/"
ground_path = "/home/luizboina/aruco_yolo_benchmark/yolo/scripts/groundtruths/"
file_path = [ground_path + file for file in os.listdir(ground_path)]

for file in file_path:
    name = file.split("/")[-1][:-4]
    img = Image.open(imgs_path + name + ".JPG")
    width, height = img.size
    lines = ""
    with open(file) as f:
        lines = f.readlines()
    with open(file, "w") as f:
        for line in lines:
            name, x, y, w, h = line.split(" ")
            x, y, w, h = float(x), float(y), float(w), float(h)
            x *= width
            w *= width
            y *= height
            h *= height
            x, y, w, h = int(x), int(y), int(w), int(h)
            if name == "0":
                name = "stop_sign"
            else:
                name = "go_sign"
            new_line = "{0} {1} {2} {3} {4}".format(name, x, y, w, h)
            f.write(new_line)
            f.write("\n")
