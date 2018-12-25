from data_aug.data_aug import *
from data_aug.bbox_util import *
import cv2
import pickle as pkl
import numpy as np
import matplotlib.pyplot as plt
from xml2array import *

def dataaug(path1,img)

    img = cv2.imread("000204.jpg")[:, :, ::-1]  # OpenCV uses BGR channels
    #bboxes = pkl.load(open("messi_ann.pkl", "rb"))
    bboxes = xml2array('.', '000204.xml')

    print(bboxes)

    transforms = Sequence([RandomHorizontalFlip(
        1), RandomScale(0.2, diff=True), RandomRotate(10)])

    img, bboxes = transforms(img, bboxes)

    plt.imshow(draw_rect(img, bboxes))
    plt.show()









if __name__ == '__main__':
    xml2array('.','000213.xml')







