# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : test.py
# Time       ：2022/4/11 19:16
# Author     ：caoxu
# version    ：python 3.9
# Description：
"""
import os
from collections import Counter
from enum import Enum
import tablib


def is_image_file(filename):
    return any(filename.endswith(extension) for extension in ['.png', '.jpg', '.jpeg', '.PNG', '.JPG', '.JPEG'])


class VersionSortID(Enum):
    CamisoleTops = 10
    CamiSpaghettiTops = 20
    CamiTops = 30
    PaddedTops = 40
    TankTops = 50


if __name__ == '__main__':
    with open('D:/PycharmProjects/data/skin_data/us_label_mask1/1351-27classes.txt', 'r', encoding='utf-8') as txt_file:
        for item in txt_file:
            print(item)
            print(item.split(',')[1])
    import cv2 as cv

    # 1 读取图像
    img = cv.imread('C:/Users/cao_1/Desktop/1.png', 0)
    flip_img = cv.flip(img, -1)
    img_bright = cv.convertScaleAbs(flip_img, alpha=2.5, beta=0)
    cv.imwrite('result.png', img_bright)
    # 2 计算Sobel卷积结果
    x = cv.Sobel(img, cv.CV_16S, 1, 0, ksize=-1)
    y = cv.Sobel(img, cv.CV_16S, 0, 1, ksize=-1)
    # 3 将数据进行转换
    Scale_absX = cv.convertScaleAbs(x)  # convert 转换  scale 缩放
    Scale_absY = cv.convertScaleAbs(y)
    # 4 结果合成
    result = cv.addWeighted(Scale_absX, 0.5, Scale_absY, 0.5, 0)

    cv.imwrite('result.png', result)
    # a = [1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6]
    # print(a[0:10])
    # print(a[10:20])
    # for i in range(int(108 / 100) + 1):
    #     print(i* 100)
    #     print( (i+1) * 100)

    # for pid, sim_infos in res_pid_sims.items():
    #     sim_infos.sort(key=lambda x: x[1], reverse=True)
    #     id_list = []
    #     sim_id_list = []
    #     for sim_info in sim_infos:
    #         if int(sim_info[0] / 1000) not in id_list:
    #             id_list.append(int(sim_info[0] / 1000))
    #             sim_id_list.append((int(sim_info[0] / 1000), sim_info[1]))
    #     sim_id_list.sort(key=lambda x: x[1], reverse=True)
    #     result = sim_id_list[:20]
    #
    #     for a in result:
    #         print(a[0])
    #         print(a[1])
    #     print(sim_id_list)

    query_img_dir = 'C:/Users/cao/Desktop/WomensTankTops/'
    version_images = [os.path.join(query_img_dir, x) for x in os.listdir(query_img_dir) if is_image_file(x)]
    version_images.sort()
    for i in range(int(len(version_images) / 100) + 1):
        vectors = []
        ids = []
        step_images = version_images[i * 100: (i + 1) * 100]
        for full_img_path in step_images:
            print(full_img_path)
            obj_dir = os.path.dirname(full_img_path) + "/object"
            os.makedirs(obj_dir, exist_ok=True)

    sim_id_list = [1,2,2,4,5,6,7,8,9,2,3,4,3,2,4,5,6,7,4,5,3,2,4,5,6]
    a = len(Counter(sim_id_list))

    image_list = ['https://images-na.ssl-images-amazon.com/images/I/51zbWfs-XvL.jpg',
                  'https://images-na.ssl-images-amazon.com/images/I/51ZzBroXE1L.jpg',
                  'https://images-na.ssl-images-amazon.com/images/I/51ke6OiNS6L.jpg',
                  'https://images-na.ssl-images-amazon.com/images/I/41O7HwKpQ7L.jpg']
    result = {1: {14: 0.6122448979591837, 11: 0.20408163265306123, 41: 0.1836734693877551},
         2: {42: 0.44680851063829785, 14: 0.3191489361702128, 40: 0.23404255319148937},
         3: {14: 0.41379310344827586, 40: 0.3103448275862069, 42: 0.27586206896551724}}
    dataset = tablib.Dataset()
    dataset.headers = ["id", "score"]
    for key, val in result.items():
        dataset.append([image_list[key-1], val])
    with open('result.csv', mode='w', encoding='UTF-8') as f:
        f.write(dataset.csv)

    import time
    print(time.time())
    image_list = ['https://m.media-amazon.com/images/I/71BvR56a5PL._AC_UX569_.jpg',
                  'https://m.media-amazon.com/images/I/617ibXBP57L._AC_UX569_.jpg',
                  'https://m.media-amazon.com/images/I/61DV7pMClWL._AC_UX569_.jpg']
    for idx, image_url in enumerate(image_list, start=1):
        print(idx)
        print(image_url)

    sort_id = VersionSortID['TankTops'].value

    query_img_dir = os.path.join('C:/Users/cao/Desktop/version_images', 'TankTops')
    version_images = [os.path.join(query_img_dir, x) for x in os.listdir(query_img_dir) if is_image_file(x)]

