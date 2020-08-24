import os
import cv2
from pandas import *

# This script make a copy of all images used during darknet validation and
# draw a bounding box using validation output information on that images

stop_sign = 0
go_sign   = 1
# Detections with porbability lower than threshold will not be drawed
threshold = 0.25
header = ['name', 'prob', 'x1', 'y1', 'x2', 'y2']
# Path to images used on validation
file_path = '/home/luizboina/aruco_yolo_benchmark/yolo/data/dataset/valid/' 
# Path to where marked images will be saved
save_file_path = '/home/luizboina/aruco_yolo_benchmark/yolo/data/obj_validacao/imgs_marks/'
# Image extension
ext = '.JPG'
# Path to validation output for go_sign class
comp_go_sign_path = '/home/luizboina/Desktop/results/comp4_det_test_go_sign.txt'
# Path to validation output for stop_sign class
comp_stop_sign_path = '/home/luizboina/Desktop/results/comp4_det_test_stop_sign.txt'

go_df = read_table(comp_go_sign_path, header=None, sep=' ', names=header)
go_df['type'] = go_sign
go_df = go_df.loc[go_df['prob'] >= threshold]

stop_df = read_table(comp_stop_sign_path, header=None, sep=' ', names=header)
stop_df['type'] = stop_sign
stop_df = stop_df.loc[stop_df['prob'] >= threshold]

df = concat([stop_df, go_df], sort=True)
df.sort_values('name', inplace=True)
# Index:
# 0 - index
# 1 - name
# 2 - prob
# 3 - type
# 4/7 - points
file_name = str(df['name'].iloc[0])
go_coords = []
stop_coords = []
thickness = 2
for row in df.itertuples():
    if file_name != row.name:
        filename_path = file_path + file_name + ext
        img = cv2.imread(filename_path)
        filename_save_path = save_file_path + file_name + ext
        for coord in go_coords:
            cv2.rectangle(img, coord[0], coord[1], (0, 255 * row.prob, 0), thickness)
        for coord in stop_coords:
            cv2.rectangle(img, coord[0], coord[1], (0, 0, 255 * row.prob), thickness)
        cv2.imwrite(filename_save_path, img)
        # cv2.imshow(filename_save_path, img)
        # if cv2.waitKey(0) & 0xFF == ord('q'):
        #     break
        file_name = row.name
        go_coords = []
        stop_coords = []
    point1 = (int(row.x1), int(row.y1))
    point2 = (int(row.x2), int(row.y2))
    if row.type == go_sign:
        go_coords.append([point1, point2])
    else:
        stop_coords.append([point1, point2])
