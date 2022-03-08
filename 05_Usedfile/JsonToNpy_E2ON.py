import json
import numpy as np
import os

json_data = []

path_dir = 'C:\\Users\\dlwlt\\Desktop\\C041_평가_FLM'  # 경로 변경 가능, json파일이 있는 폴더로 지정
file_list = os.listdir(path_dir)

# json_data
# list of json file
for name in file_list:
    with open(path_dir + '/' + name, 'r') as f:
        json_data.append(json.load(f))

for i in range(len(file_list)):
    #
    block = len(json_data[i]['block_information'])
    frame_level_masks = 0
    npy = []

    # file name
    name = file_list[i]
    name = name.replace("_blockinfo.json", "")

    for j in range(block):
        start = int(json_data[i]['block_information'][j]['start_frame_index'])
        end = int(json_data[i]['block_information'][j]['end_frame_index']) + 1

        if (json_data[i]['block_information'][j]['block_type'] == 'action'):
            frame_level_masks = 1
        elif (json_data[i]['block_information'][j]['block_type'] == 'symptom'):
            frame_level_masks = 1

        for k in range(start, end):
            npy.append(frame_level_masks)

    for i in range(200):
        npy.append(0)

    npy = np.array(npy)
    np.save(path_dir + '/' + name + '.npy', npy)
    # 저장위치 변경 가능, path_dir만 변경 가능
