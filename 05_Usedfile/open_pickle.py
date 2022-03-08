import pickle

#with open('./sk-cnn-00/ntu_npy_after_txt/S001C001P001R001A001.skeleton.npy.pickle', 'rb') as f:
#    data = pickle.load(f)

#print(data)
#print(type(data))
#print("shape: {}".format(data.shape))
#print("dtype: {}".format(data.dtype))

#import numpy as np

#data = np.load('/home/NIA_AI_DATASET_2021-MPED-RNN/SK-CNN-master/network/ntu_npy/S001C001P001R001A002.skeleton.npy', allow_pickle=True)


#data = np.reshape(data, newshape=(-1, 25, 3))
#print(data)
#print(type(data))
#print("shape: {}".format(data.shape))
#print("dtype: {}".format(data.dtype))

# pickle = npy

with open('C:\\Users\\dlwlt\\Desktop\\ntu_npy_after_txt\\S001C001P001R001A001.skeleton.npy.pickle', 'rb') as f:
    data = pickle.load(f)

print(data[1])
print(type(data))
print("shape: {}".format(data.shape)) #A001.pickle->25행 3열 데이터가 103개 있다는 뜻


#data = [[[0]*3 for _ in range(25)] for _ in range(25)]

#data = [[[0]*3]*3]*3
#print('{}, {}, {}'.format(id(data[0]), id(data[1]), id(data[2])))