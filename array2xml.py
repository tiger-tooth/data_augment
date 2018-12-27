import xml.etree.ElementTree as ET
import time
import os
import glob
import numpy as np


def array2xml(bndarray, xmlname, classes):
    xmlfile = xmlname

    if not xmlfile.endswith('.xml'):
        print('Error!!! Not xml file!!!')
    else:
        print('Load a newxml file...')

        tree = ET.parse(xmlfile)
        root = tree.getroot()
        #print(bndarray)

        i = 0
        #print(bndarray)

        # if bndarray.size==0:
        #     print("WARNING!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        #     root.remove(object)

        # else:
            
        for ele1 in root.findall('object'):
            if bndarray.size==0:
                root.remove(ele1)
            else:

                ele1.find('name').text = classes[int(bndarray[i][4])]
                for ele2 in ele1.findall('bndbox'):
                    ele2.find('xmin').text = str(int(bndarray[i][0]))
                    ele2.find('ymin').text = str(int(bndarray[i][1]))
                    ele2.find('xmax').text = str(int(bndarray[i][2]))
                    ele2.find('ymax').text = str(int(bndarray[i][3]))
                i=i+1
                if i == bndarray.shape[0]:
                    break
        
        tree.write(xmlfile)

if __name__ == '__main__':
    b = np.array([[0., 0., 0., 0., 0.], [336., 200.,
                                                 503., 503., 0.], [368., 105., 671., 537., 0.], ])
    classes = ['Soldier', 'Civilian', 'Civilian_Vehicle', 'Military_Vehicle']
    array2xml(b, 'out/000213test.xml', classes)
