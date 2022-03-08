import json
import numpy as np



filename = 'C:\\Users\\dlwlt\\Desktop\\c042\\C042_A31_SY28_P09_B01_01DAS_blockinfo.json'

with open(filename.format(0), 'r') as f:
    json_data = json.load(f)

npy = []
print(json_data['block_information'])
print(json_data['block_information'][1]['start_frame_index'])
print(json_data['block_information'][len(json_data['block_information'])-2]['end_frame_index'])

#for j in range(int(json_data['block_information'][len(json_data['block_information'])-1]['end_frame_index'])+1):
 #   if j>int(json_data['block_information'][1]['start_frame_index']) and j<int(json_data['block_information'][len(json_data['block_information'])-2]['end_frame_index']):
  #      npy.append(1)
 #   else:
      #  npy.append(0)



#npy = np.array(npy)
#np.save('C:\\Users\\dlwlt\Desktop\\' + str(1) + '.npy' , npy)