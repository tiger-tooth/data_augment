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


def dataaug(imgname, xmlname, outputdir, classes):

    if not os.path.exists(outputdir):
        os.makedirs(outputdir)

    img = cv2.imread(imgname)[:, :, ::-1]  # OpenCV uses BGR channels
    bboxes = xml2array(xmlname, classes)

    print(bboxes)

    # transforms = Sequence([RandomHorizontalFlip(
    #     1), RandomScale(0.2, diff=True), RandomRotate(10)])

    # img, bboxes = transforms(img, bboxes)

####################RandomHorizontalFlip#################################
    img_, bboxes_ = RandomHorizontalFlip(1)(img.copy(), bboxes.copy())

    print(bboxes_)
    newimg_name= outputdir+imgname[-10:-4]+'Horizontal.jpg'
    cv2.imwrite(newimg_name, cv2.cvtColor(img_, cv2.COLOR_BGR2RGB))

    newxml_name = outputdir+xmlname[-10:-4]+'Horizontal.xml'
    copyfile(xmlname, newxml_name)

    array2xml(bboxes_, newxml_name, classes)

    plt.imshow(draw_rect(img_, bboxes_))
    plt.show()
#########################################################################
####################RandomScale##########################################
    img_, bboxes_ = RandomScale(0.3, diff = True)(img.copy(), bboxes.copy())

    print(bboxes_)
    newimg_name= outputdir+imgname[-10:-4]+'Scale.jpg'
    cv2.imwrite(newimg_name, cv2.cvtColor(img_, cv2.COLOR_BGR2RGB))

    newxml_name = outputdir+xmlname[-10:-4]+'Scale.xml'
    copyfile(xmlname, newxml_name)

    array2xml(bboxes_, newxml_name, classes)

    plt.imshow(draw_rect(img_, bboxes_))
    plt.show()
#########################################################################
####################RandomTranslate######################################
    img_, bboxes_ = RandomTranslate(0.3, diff = True)(img.copy(), bboxes.copy())

    print(bboxes_)
    newimg_name= outputdir+imgname[-10:-4]+'Translate.jpg'
    cv2.imwrite(newimg_name, cv2.cvtColor(img_, cv2.COLOR_BGR2RGB))

    newxml_name = outputdir+xmlname[-10:-4]+'Translate.xml'
    copyfile(xmlname, newxml_name)

    array2xml(bboxes_, newxml_name, classes)

    plt.imshow(draw_rect(img_, bboxes_))
    plt.show()
#########################################################################
####################RandomRotate#########################################
    img_, bboxes_ = RandomRotate(20)(img.copy(), bboxes.copy())

    print(bboxes_)
    newimg_name= outputdir+imgname[-10:-4]+'Rotate.jpg'
    cv2.imwrite(newimg_name, cv2.cvtColor(img_, cv2.COLOR_BGR2RGB))

    newxml_name = outputdir+xmlname[-10:-4]+'Rotate.xml'
    copyfile(xmlname, newxml_name)

    array2xml(bboxes_, newxml_name, classes)

    plt.imshow(draw_rect(img_, bboxes_))
    plt.show()
#########################################################################
####################RandomShear##########################################
    img_, bboxes_ = RandomShear(0.2)(img.copy(), bboxes.copy())

    print(bboxes_)
    newimg_name= outputdir+imgname[-10:-4]+'Shear.jpg'
    cv2.imwrite(newimg_name, cv2.cvtColor(img_, cv2.COLOR_BGR2RGB))

    newxml_name = outputdir+xmlname[-10:-4]+'Shear.xml'
    copyfile(xmlname, newxml_name)

    array2xml(bboxes_, newxml_name, classes)

    plt.imshow(draw_rect(img_, bboxes_))
    plt.show()
#########################################################################
####################Resize###############################################
    img_, bboxes_ = Resize(608)(img.copy(), bboxes.copy())

    print(bboxes_)
    newimg_name= outputdir+imgname[-10:-4]+'Resize.jpg'
    cv2.imwrite(newimg_name, cv2.cvtColor(img_, cv2.COLOR_BGR2RGB))

    newxml_name = outputdir+xmlname[-10:-4]+'Resize.xml'
    copyfile(xmlname, newxml_name)

    array2xml(bboxes_, newxml_name, classes)

    plt.imshow(draw_rect(img_, bboxes_))
    plt.show()
#########################################################################
####################RandomHSV############################################
    img_, bboxes_ = RandomHSV(100, 100, 100)(img.copy(), bboxes.copy())

    print(bboxes_)
    newimg_name= outputdir+imgname[-10:-4]+'RandomHSV.jpg'
    cv2.imwrite(newimg_name, cv2.cvtColor(img_, cv2.COLOR_BGR2RGB))

    newxml_name = outputdir+xmlname[-10:-4]+'RandomHSV.xml'
    copyfile(xmlname, newxml_name)

    array2xml(bboxes_, newxml_name, classes)

    plt.imshow(draw_rect(img_, bboxes_))
    plt.show()
#########################################################################






if __name__ == '__main__':

    classes = ['Soldier', 'Civilian', 'Civilian_Vehicle', 'Military_Vehicle']
    dataaug('./000213.jpg', './000213.xml', 'out/', classes)
    dataaug('./000204.jpg', './000204.xml', 'out/', classes)
