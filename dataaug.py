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

#########################################################################
    img1, bboxes1 = RandomHorizontalFlip(1)(img, bboxes)

    print(bboxes1)
    newimg_name1 = outputdir+imgname[-10:-4]+'Horizontal.jpg'
    cv2.imwrite(newimg_name1, cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))

    newxml_name1 = outputdir+xmlname[-10:-4]+'åHorizontal.xml'
    copyfile(xmlname, newxml_name1)

    array2xml(bboxes1, newxml_name1, classes)

    plt.imshow(draw_rect(img1, bboxes1))
    plt.show()
#########################################################################
#########################################################################
    img2, bboxes2 = RandomScale(0.3, diff=True)(img, bboxes)

    print(bboxes2)
    newimg_name2 = outputdir+imgname[-10:-4]+'Scale.jpg'
    cv2.imwrite(newimg_name2, cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))

    newxml_name2 = outputdir+xmlname[-10:-4]+'Scale.xml'
    copyfile(xmlname, newxml_name2)

    array2xml(bboxes2, newxml_name2, classes)

    plt.imshow(draw_rect(img2, bboxes2))
    plt.show()
#########################################################################
#########################################################################
    img3, bboxes3 = RandomTranslate(0.3, diff=True)(img, bboxes)

    print(bboxes3)
    newimg_name3 = outputdir+imgname[-10:-4]+'Translate.jpg'
    cv2.imwrite(newimg_name3, cv2.cvtColor(img3, cv2.COLOR_BGR2RGB))

    newxml_name3 = outputdir+xmlname[-10:-4]+'Translate.xml'
    copyfile(xmlname, newxml_name1)

    array2xml(bboxes3, newxml_name3, classes)

    plt.imshow(draw_rect(img3, bboxes3))
    plt.show()
#########################################################################
#########################################################################
    img4, bboxes4 = RandomRotate(20)(img, bboxes)

    print(bboxes4)
    newimg_name4 = outputdir+imgname[-10:-4]+'Rotate.jpg'
    cv2.imwrite(newimg_name4, cv2.cvtColor(img4, cv2.COLOR_BGR2RGB))

    newxml_name4 = outputdir+xmlname[-10:-4]+'Rotate.xml'
    copyfile(xmlname, newxml_name4)

    array2xml(bboxes4, newxml_name4, classes)

    plt.imshow(draw_rect(img4, bboxes4))
    plt.show()
#########################################################################
#########################################################################
    img5, bboxes5 = RandomShear(0.2)(img, bboxes)

    print(bboxes5)
    newimg_name5 = outputdir+imgname[-10:-4]+'Shear.jpg'
    cv2.imwrite(newimg_name5, cv2.cvtColor(img5, cv2.COLOR_BGR2RGB))

    newxml_name5 = outputdir+xmlname[-10:-4]+'Shear.xml'
    copyfile(xmlname, newxml_name5)

    array2xml(bboxes5, newxml_name5, classes)

    plt.imshow(draw_rect(img5, bboxes5))
    plt.show()
#########################################################################
#########################################################################
    img6, bboxes6 = Resize(608)(img, bboxes)

    print(bboxes6)
    newimg_name6 = outputdir+imgname[-10:-4]+'Resize.jpg'
    cv2.imwrite(newimg_name6, cv2.cvtColor(img6, cv2.COLOR_BGR2RGB))

    newxml_name6 = outputdir+xmlname[-10:-4]+'Resize.xml'
    copyfile(xmlname, newxml_name6)

    array2xml(bboxes6, newxml_name6, classes)

    plt.imshow(draw_rect(img6, bboxes6))
    plt.show()
#########################################################################
#########################################################################
    img7, bboxes7 = RandomHSV(100, 100, 100)(img, bboxes)

    print(bboxes7)
    newimg_name7 = outputdir+imgname[-10:-4]+'HSV.jpg'
    cv2.imwrite(newimg_name7, cv2.cvtColor(img7, cv2.COLOR_BGR2RGB))

    newxml_name7 = outputdir+xmlname[-10:-4]+'HSV.xml'
    copyfile(xmlname, newxml_name7)

    array2xml(bboxes7, newxml_name7, classes)

    plt.imshow(draw_rect(img7, bboxes7))
    plt.show()
#########################################################################


if __name__ == '__main__':

    classes = ['Soldier', 'Civilian', 'Civilian_Vehicle', 'Military_Vehicle']
    dataaug('./000213.jpg', './000213.xml', 'out/', classes)
