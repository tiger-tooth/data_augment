import xml.etree.ElementTree as ET
import time 
import os

path = '.'
filelist = os.listdir(path)
filelist.sort()
i=1
for item in filelist:
    if item.endswith('.xml'):
        tree=ET.parse(item)
        root=tree.getroot()

        for ele1 in root.findall('size'):
            for ele2 in ele1.iter('img_width'):
                ele2.tag='width'
            for ele2 in ele1.iter('img_height'):
                ele2.tag='height'
            for ele2 in ele1.iter('img_depth'):
                ele2.tag='depth'
            
        for ele3 in root.findall('object'): 
            ele3.find('name').text='Military_Vehicle'
        #     for ele4 in ele3.iter('bounding_box'):
        #         ele4.tag='bndbox'
        #     for ele4 in ele3.iter('x_left_top'):
        #         ele4.tag='xmin'
        #     for ele4 in ele3.iter('y_left_top'):
        #         ele4.tag='ymin'
        #     for ele4 in ele3.iter('width'):
        #         ele4.tag='xmax'
        #     for ele4 in ele3.iter('height'):
        #         ele4.tag='ymax'
        # for ele5 in root.findall('object'):
        #     for ele6 in ele5.findall('bndbox'):               
        #         xmin = int(ele6.find('xmin').text)
        #         ymin=int(ele6.find('ymin').text)
        #         w=int(ele6.find('xmax').text)
        #         h=int(ele6.find('ymax').text)
        #         xmax=xmin+w
        #         ymax=ymin+h

        #         ele6.find('xmax').text=str(xmax)
        #         ele6.find('ymax').text=str(ymax)




        tree.write(item)
        print('total= %d',i)
        print('%s is changed'%item)
        i=i+1

