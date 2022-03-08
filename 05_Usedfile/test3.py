import json
import numpy as np


filename = 'C:/Users/dlwlt/Desktop/UCF-Crime/UCF-Crime_Assault/Assault001_x264_check.json'

with open(filename.format(1), 'r') as f:
    json_data = json.load(f)

npy = []

for j in range(len(json_data['frames'])):
    if (len(json_data['frames'][j]['persons'])>=2): #사람 2명이상일때
         npy.append(1)
    else:
         npy.append(0)

print(npy[620])
print(len(npy))
#npy = np.array(npy)
#np.save('test1.npy'.format(1), npy)