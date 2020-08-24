import os

# This script delete all images and annotation that have only class "0", 
# erase all lines with class "0" in annotation and
# change class "1" to class "0" and class "2" to class "1"


# Path where dataset are
images_path = "/home/luizboina/Yolo-Annotation-Tool-New-/images/"
files = [images_path + file for file in os.listdir(images_path)]
count = 0
for file in files:
    if file[-3:] == "txt":
        with open(file, "r") as f:
            lines = f.readlines()
        with open(file, "w") as f:
            have_sign = False
            for line in lines:
                new_line = line
                if line[0] == "1" or line[0] == "2":
                    have_sign = True
                    if line[0] == "1":
                        new_line = "0" + line[1:]
                    else:
                        new_line = "1" + line[1:]
                    f.write(new_line)
            if not have_sign:
                img_name = file[:-3] + "JPG"
                os.remove(file)
                os.remove(img_name)
                count += 1

print("deleted files {}".format(count))
