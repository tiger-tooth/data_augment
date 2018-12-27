import xml.etree.ElementTree as ET
import time 
import os
import glob
import numpy as np
'''

'''

def xml2array(xmlname,classes):
    xmlfile=xmlname
    bnd_list=[]

    if not xmlfile.endswith('.xml'):
        print('Error!!! Not xml file!!!')
    else:
        print('Load a xml file...')

        tree=ET.parse(xmlfile)
        root=tree.getroot()

        for ele1 in root.findall('object'):
            c=classes.index(ele1.find('name').text)
            for ele2 in ele1.findall('bndbox'):
                xmin=float(ele2.find('xmin').text)
                ymin=float(ele2.find('ymin').text)
                xmax=float(ele2.find('xmax').text)
                ymax=float(ele2.find('ymax').text)
            bnd_list.append([xmin,ymin,xmax,ymax,c])
            #print(bnd_list)
        return np.stack(bnd_list)

        

if __name__ == '__main__':
    classes=['Soldier','Civilian','Civilian_Vehicle','Military_Vehicle']
    xml2array('./000213.xml',classes)

