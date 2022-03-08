import json
import numpy as np

for i in range(2, 101):
    filename = 'C:/Users/dlwlt/Desktop/UCF-Crime_Fighting/Fighting{0:03d}_x264_check.json'

    with open(filename.format(i), 'r') as f:
        json_data = json.load(f)

    npy = []

    for j in range(len(json_data['frames'])):
        if (len(json_data['frames'][j]['persons']) >= 2):  #사람 두명이상일때
            npy.append(1)
        else:
            npy.append(0)

    npy = np.array(npy)
    np.save('./Fighting_npy/01_{0:02d}.npy'.format(i), npy)