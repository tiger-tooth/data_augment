from data_aug.data_aug import *
from data_aug.bbox_util import *
import cv2
import os
import pickle as pkl
import numpy as np
import matplotlib.pyplot as plt
from xml2array import *
from shutil import copyfile
from array2xml import *

# def dataaug(path1,imgname,path2,xmlname,outputdir):

#     if not os.path.exists(outputdir):
#         os.makedirs(outputdir)

#     img = cv2.imread(path1+imgname)[:, :, ::-1]  # OpenCV uses BGR channels
#     bboxes = xml2array(path2,xmlname)

#     print(bboxes)

#     # transforms = Sequence([RandomHorizontalFlip(
#     #     1), RandomScale(0.2, diff=True), RandomRotate(10)])

#     # img, bboxes = transforms(img, bboxes)


#     img,bboxes=RandomHorizontalFlip(1)(img,bboxes)
#     newimg_name=outputdir+imgname[0:6]+'test.jpg'
#     cv2.imwrite(newimg_name,cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
    
#     newxml_name=outputdir+xmlname[0:6]+'test.xml'
#     copyfile(path2+xmlname,newxml_name)
    
#     plt.imshow(draw_rect(img, bboxes))
#     plt.show()









# if __name__ == '__main__':
#     dataaug('./','000204.jpg','./','000204.xml','out/')




def dataaug(imgname,xmlname,outputdir,classes):

    if not os.path.exists(outputdir):
        os.makedirs(outputdir)

    img = cv2.imread(imgname)[:, :, ::-1]  # OpenCV uses BGR channels
    bboxes = xml2array(xmlname,classes)

    print(bboxes)

    # transforms = Sequence([RandomHorizontalFlip(
    #     1), RandomScale(0.2, diff=True), RandomRotate(10)])

    # img, bboxes = transforms(img, bboxes)


    img,bboxes=RandomHorizontalFlip(1)(img,bboxes)

    print(bboxes)
    newimg_name=outputdir+imgname[-10:-4]+'test.jpg'
    cv2.imwrite(newimg_name,cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
    
    newxml_name=outputdir+xmlname[-10:-4]+'test.xml'
    copyfile(xmlname,newxml_name)

    array2xml(bboxes,newxml_name,classes)
    
    plt.imshow(draw_rect(img, bboxes))
    plt.show()









if __name__ == '__main__':

    classes=['Soldier','Civilian','Civilian_Vehicle','Military_Vehicle']
    dataaug('./000213.jpg','./000213.xml','out/',classes)




