# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : csv_file_analysis.py
# Time       ：2022/3/28 17:49
# Author     ：caoxu
# version    ：python 3.9
# Description：  cid1  cid2  pid1 pid2 score
"""
from collections import Counter
import pandas as pd
import tablib


def is_image_file(filename):
    return any(filename.endswith(extension) for extension in ['.png', '.jpg', '.jpeg', '.PNG', '.JPG', '.JPEG'])


def csv_analysis():
    dataset = tablib.Dataset()
    dataset.headers = ["pid", "sales", "cid1", "cid2", "cid3", "同款商品pid", "score"]

    sim_pros_path = 'C:/Users/cao/Desktop/sim_pros.csv'
    sim_pros_data = pd.read_csv(sim_pros_path, header=None, names=["cid1", "cid2", "pid1", "pid2", "score"])
    sim_pros_result = sim_pros_data[sim_pros_data.score > 0.90]
    sim_pros_pid1 = sim_pros_result.pid1.tolist()
    sim_pros_pid2 = sim_pros_result.pid2.tolist()
    sim_pros_score = sim_pros_result.score.tolist()


    sales_path = 'C:/Users/cao/Desktop/Result_1.csv'
    sales_data = pd.read_csv(sales_path)
    for sales_index, sales_row in sales_data.iterrows():
        if sim_pros_pid1.count(sales_row[0]):
            index = [x for x in range(len(sim_pros_pid1)) if sim_pros_pid1[x] == sales_row[0]]
            for i in index:
                dataset.append([sales_row[0], sales_row[1], sales_row[2], sales_row[3], sales_row[4],
                            sim_pros_pid2[i], sim_pros_score[i]])
    with open('C:/Users/cao/Desktop/sales-count.csv', mode='w', encoding='UTF-8') as f:
        f.write(dataset.csv)


if __name__ == '__main__':
    maid_path = 'C:/Users/cao/Desktop/maid.csv'
    maid_data = pd.read_csv(maid_path)

    # android
    android_list = maid_data[(maid_data.client == 'ANDROID') & (maid_data.dt == '2022-03-25')]
    android_id_list = android_list['customerid']
    android_count = Counter(android_id_list)
    print(android_count)
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    # iphone
    iphone_list = maid_data[(maid_data.client == 'IPHONE') & (maid_data.dt == '2022-03-25')]
    iphone_id_list = iphone_list['customerid']
    iphone_count = Counter(iphone_id_list)
    print(iphone_count)


    # s = [8697443, 8536180, 8676165, 8697443, 3716215, 9017026, 8697443, 8626732, 8697443]
    # print(s.count(8697443))
    # aa = [x for x in range(len(s)) if s[x] == 8697443]  # 一次获得所有位置
    # index = s.index(8697443)

    # csv_analysis()
