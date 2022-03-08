import numpy as np

#data = np.load('C:\\Users\\dlwlt\\Desktop\\E2ON_test\\testing\\frame_level_masks\\01\\01_01.npy')
data = np.load('C:\\Users\\dlwlt\\Desktop\\blockinfo_npy\\C042_A31_SY28_P09_B01_01DAS.npy')
print(data)
print(len(data))
i=0
while i < len(data):
    print(data[i])
    i += 1