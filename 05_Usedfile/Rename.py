import os

folder_path = "C:\\Users\\dlwlt\\Desktop\\C041_평가CSV_rename"
folder_list = os.listdir(folder_path)
print(folder_list)

for i in range(0, 180):
    old_name = folder_path + '/' + folder_list[i]
    new_name = folder_path + '/' + '{0:02d}'.format(i+1)
    print(old_name, new_name)
    os.rename(old_name, new_name)



