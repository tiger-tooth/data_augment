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
from dataaug import *
from twilio.rest import Client

filelist=os.listdir('/home/lthpc/liuhy/Data/MandC_dataaug/')
filelist.sort()
total_num=len(filelist)/2

classes = ['Soldier', 'Civilian', 'Civilian_Vehicle', 'Military_Vehicle']


for item in filelist:
    if item.endswith('.jpg'):
        imgname=item
        xmlname=item[-10:-4]+'.xml'
        dataaug('/home/lthpc/liuhy/Data/MandC_dataaug/'+imgname,'/home/lthpc/liuhy/Data/MandC_dataaug/'+xmlname,'/home/lthpc/liuhy/Data/out/',classes)
        # print('%s and %s are done!'%(imgname,xmlname))



