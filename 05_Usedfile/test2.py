import json
import numpy as np


filename = 'Assault001_x264_check.json'

with open(filename.format(1), 'r') as f:
    json_data = json.load(f)


print(range(len(json_data['frames'])))
print(json_data['frames'][556]['persons'])
print(len(json_data['frames'][556]['persons']))
print(len(json_data['frames'][620]['persons']))
print(type(json_data['frames'][556]['persons']))
