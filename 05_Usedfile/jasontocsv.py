import json
import numpy as np

json_data = []

#
for i in range(50):
    with open('C:/Users/dlwlt/Desktop/Assault_check_jason/Assault{0:03d}_x264_check.json'.format(i + 1), 'r') as f:
        json_data.append(json.load(f))

#
for j in range(50):
    line = []
    for i in range(len(json_data[j]['frames'])):
        point = []
        if (len(json_data[j]['frames'][i]['persons']) > 0):
            point.append('{:.2e}'.format(float(json_data[j]['frames'][i]['frame_index'])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][0]['keypoints'][0].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][0]['keypoints'][15].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][0]['keypoints'][16].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][0]['keypoints'][17].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][0]['keypoints'][18].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][0]['keypoints'][5].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][0]['keypoints'][2].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][0]['keypoints'][6].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][0]['keypoints'][3].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][0]['keypoints'][7].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][0]['keypoints'][4].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][0]['keypoints'][12].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][0]['keypoints'][9].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][0]['keypoints'][13].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][0]['keypoints'][10].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][0]['keypoints'][14].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][0]['keypoints'][11].split(',')[k])))

            line.append(point)

    line = np.array(line)
    #
    np.savetxt('C:/Users/dlwlt/Desktop/UCF-Crime/UCF-Crime_Assault/Test/{:04d}/0001.csv'.format(j + 1), line, fmt="%s", delimiter=",")

#
for j in range(50):
    line = []
    for i in range(len(json_data[j]['frames'])):
        point = []
        if (len(json_data[j]['frames'][i]['persons']) > 1):
            point.append('{:.2e}'.format(float(json_data[j]['frames'][i]['frame_index'])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][1]['keypoints'][0].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][1]['keypoints'][15].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][1]['keypoints'][16].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][1]['keypoints'][17].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][1]['keypoints'][18].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][1]['keypoints'][5].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][1]['keypoints'][2].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][1]['keypoints'][6].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][1]['keypoints'][3].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][1]['keypoints'][7].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][1]['keypoints'][4].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][1]['keypoints'][12].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][1]['keypoints'][9].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][1]['keypoints'][13].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][1]['keypoints'][10].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][1]['keypoints'][14].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][1]['keypoints'][11].split(',')[k])))

            line.append(point)

    line = np.array(line)
    #
    np.savetxt('C:/Users/dlwlt/Desktop/UCF-Crime/UCF-Crime_Assault/Test/{:04d}/0002.csv'.format(j + 1), line, fmt="%s", delimiter=",")

#
for j in range(50):
    line = []
    for i in range(len(json_data[j]['frames'])):
        point = []
        if (len(json_data[j]['frames'][i]['persons']) > 2):
            point.append('{:.2e}'.format(float(json_data[j]['frames'][i]['frame_index'])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][2]['keypoints'][0].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][2]['keypoints'][15].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][2]['keypoints'][16].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][2]['keypoints'][17].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][2]['keypoints'][18].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][2]['keypoints'][5].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][2]['keypoints'][2].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][2]['keypoints'][6].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][2]['keypoints'][3].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][2]['keypoints'][7].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][2]['keypoints'][4].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][2]['keypoints'][12].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][2]['keypoints'][9].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][2]['keypoints'][13].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][2]['keypoints'][10].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][2]['keypoints'][14].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][2]['keypoints'][11].split(',')[k])))

            line.append(point)

    line = np.array(line)
    #
    np.savetxt('C:/Users/dlwlt/Desktop/UCF-Crime/UCF-Crime_Assault/Test/{:04d}/0003.csv'.format(j + 1), line, fmt="%s", delimiter=",")

#
for j in range(50):
    line = []
    for i in range(len(json_data[j]['frames'])):
        point = []
        if (len(json_data[j]['frames'][i]['persons']) > 3):
            point.append('{:.2e}'.format(float(json_data[j]['frames'][i]['frame_index'])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][3]['keypoints'][0].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][3]['keypoints'][15].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][3]['keypoints'][16].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][3]['keypoints'][17].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][3]['keypoints'][18].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][3]['keypoints'][5].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][3]['keypoints'][2].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][3]['keypoints'][6].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][3]['keypoints'][3].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][3]['keypoints'][7].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][3]['keypoints'][4].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][3]['keypoints'][12].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][3]['keypoints'][9].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][3]['keypoints'][13].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][3]['keypoints'][10].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][3]['keypoints'][14].split(',')[k])))
            for k in range(2):
                point.append(
                    '{:.2e}'.format(float(json_data[j]['frames'][i]['persons'][3]['keypoints'][11].split(',')[k])))

            line.append(point)

    line = np.array(line)
    #
    np.savetxt('C:/Users/dlwlt/Desktop/UCF-Crime/UCF-Crime_Assault/Test/{:04d}/0004.csv'.format(j + 1), line, fmt="%s", delimiter=",")

