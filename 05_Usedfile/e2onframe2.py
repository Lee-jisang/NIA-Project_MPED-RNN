import json
import numpy as np



    filename = 'C:\Users\ticta\Desktop\json\' + str(i+1) + '.json'

    with open(filename.format(i), 'r') as f:
        json_data = json.load(f)

    npy = []

    for j in range(int(json_data['block_information'][len(json_data['block_information'])-1]['end_frame_index'])+1):
        if j>int(json_data['block_information'][1]['start_frame_index']) and j<int(json_data['block_information'][len(json_data['block_information'])-2]['end_frame_index']):
            npy.append(1)
        else:
            npy.append(0)



    npy = np.array(npy)
    #np.save('C:\Users\ticta\Desktop\json\' + str(i+1) + '.npy' , npy)