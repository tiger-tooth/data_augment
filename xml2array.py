import xml.etree.ElementTree as ET
import time 
import os
import glob
import numpy as np
'''

'''
classes1={'Soldier':0,'Civilian':1,'Civilian_Vehicle':2,'Military_Vehicle':3}

def xml2array(path,xmlname):
    xmlfile=(path+'/'+xmlname)
    bnd_list=[]

    if not xmlfile.endswith('.xml'):
        print('Error!!!  Not xml file!!!')
    else:
        print('ok')

        tree=ET.parse(xmlfile)
        root=tree.getroot()

        for ele1 in root.findall('object'):
            c=classes1[ele1.find('name').text]
            for ele2 in ele1.findall('bndbox'):
                xmin=float(ele2.find('xmin').text)
                ymin=float(ele2.find('ymin').text)
                xmax=float(ele2.find('xmax').text)
                ymax=float(ele2.find('ymax').text)
            bnd_list.append([xmin,ymin,xmax,ymax,c])
    
    print(np.stack(bnd_list))
    return np.stack(bnd_list)
        

        

if __name__ == '__main__':
    xml2array('.','000213.xml')

