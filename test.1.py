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
    img1, bboxes1 = RandomHSV(100, 100, 100)(img, bboxes)

    print(bboxes1)
    newimg_name1 = outputdir+imgname[-10:-4]+'Horizontal.jpg'
    cv2.imwrite(newimg_name1, cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))

    newxml_name1 = outputdir+xmlname[-10:-4]+'Horizontal.xml'
    copyfile(xmlname, newxml_name1)

    array2xml(bboxes1, newxml_name1, classes)

    plt.imshow(draw_rect(img1, bboxes1))
    plt.show()


if __name__ == '__main__':

    classes = ['Soldier', 'Civilian', 'Civilian_Vehicle', 'Military_Vehicle']
    dataaug('./000213.jpg', './000213.xml', 'out/', classes)
