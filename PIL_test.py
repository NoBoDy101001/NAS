#!/usr/bin/python
# -*- coding: utf-8 -*-

from PIL import Image
import os
import numpy as np
#from matplotlib import pyplot as plt

data_path = '/home/data/ilsvrc_zip/train'
file_lists = os.listdir(data_path)
for file in file_lists[:1]:
    sub_path = os.path.join(data_path, file)
    sub_fold = os.listdir(sub_path)
    for images in sub_fold[:10]:
        image_path = os.path.join(sub_path, images)
        img = Image.open(image_path)
        w, h = img.size
        img = img.convert('RGB').resize((224, 224))
        arr = np.asarray(img, dtype=np.float32)
        print(arr.shape)
        arr = arr.transpose(2, 0, 1)
        print(arr.shape)







