import os

count_file = 0

path = 'D:\\etude_en_france\\Garbageproject\\dataset\\archive\\Images_of_Waste\\YOLO_imgs'
dir_list = os.listdir(path)
os.chdir(path)

for file in dir_list:
    if '.txt' in file:
        with open(file, 'r') as f:
            lines = f.readlines()
            if len(lines)>1:
                count_file += 1
            f.close()

os.chdir('D:\\etude_en_france\\Garbageproject')
print(count_file)