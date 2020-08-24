import os
import shutil
import glob
import random
import math
from os.path import isfile, join


dataset = "/home/luizboina/aruco_yolo_benchmark/yolo/utils/train/"
train_perc = 0.7
valid_perc = 0.2
test_perc = 0.1
img_count = len([name for name in os.listdir(dataset) if isfile(join(dataset, name))]) / 2
print(img_count)
my_glob = glob.glob(dataset + "*.jpg")
train_count = math.ceil(img_count * train_perc)
print(my_glob.__len__(), train_count)
to_be_moved = random.sample(my_glob, train_count)

for f in enumerate(to_be_moved, 1):
    file_name = f[1].split("/")[-1]
    annotation_path = f[1][:-3] + "txt"
    annotation_name = file_name[:-3] + "txt"
    img_dest = os.path.join(dataset + "train", file_name)
    shutil.move(f[1], img_dest)
    annotation_dest = os.path.join(dataset + "train", annotation_name)
    shutil.move(annotation_path, annotation_dest)

my_glob = glob.glob(dataset + "*.jpg")
valid_count = math.floor(img_count * valid_perc)
print(my_glob.__len__(), valid_count)
to_be_moved = random.sample(my_glob, valid_count)

for f in enumerate(to_be_moved, 1):
    file_name = f[1].split("/")[-1]
    annotation_path = f[1][:-3] + "txt"
    annotation_name = file_name[:-3] + "txt"
    img_dest = os.path.join(dataset + "valid", file_name)
    shutil.move(f[1], img_dest)
    annotation_dest = os.path.join(dataset + "valid", annotation_name)
    shutil.move(annotation_path, annotation_dest)

my_glob = glob.glob(dataset + "*.jpg")
test_count = math.floor(img_count * test_perc)
print(my_glob.__len__(), test_count)
to_be_moved = random.sample(my_glob, test_count)

for f in enumerate(to_be_moved, 1):
    file_name = f[1].split("/")[-1]
    annotation_path = f[1][:-3] + "txt"
    annotation_name = file_name[:-3] + "txt"
    img_dest = os.path.join(dataset + "test", file_name)
    shutil.move(f[1], img_dest)
    annotation_dest = os.path.join(dataset + "test", annotation_name)
    shutil.move(annotation_path, annotation_dest)
