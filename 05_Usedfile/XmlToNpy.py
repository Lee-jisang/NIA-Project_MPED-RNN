from xml.etree.ElementTree import parse
import numpy as np
for i in range(15):
    tree = parse('C:\\Users\\dlwlt\\Desktop\\AI-Hub_xml2\\03.절도(burglary)\\' + str(i+1) + '.xml')
    npy = []

    header = tree.findall("header")
    frames = [x.findtext("frames") for x in header]
    event = tree.findall("event")
    starttime = [x.findtext("starttime") for x in event]
    starttime = ''.join(char for char in starttime[0] if char.isalnum())
    start_frame = int(starttime)*3
    duration = [x.findtext("duration") for x in event]
    duration = ''.join(char for char in duration[0] if char.isalnum())
    duration_frame = (int(int(duration)/1000)*600+int(duration)%1000)*3
    end_frame = start_frame + duration_frame

    for j in range(int(frames[0])):
        if start_frame <= j and end_frame >= j :
            npy.append(1)
        else:
            npy.append(0)

    npy = np.array(npy)
    #np.save('C:\\Users\\dlwlt\\Desktop\\AI-Hub_frame\\03.절도(burglary)\\' + str(i+1) + '.npy', npy)