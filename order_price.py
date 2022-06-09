import os
import pandas as pd
import tablib
from collections import Counter
import numpy as np
from scipy.optimize import curve_fit
import math
import matplotlib.pyplot as plt


def order_analysis(csv_path):
    dataset = tablib.Dataset()
    dataset.headers = ['all', 'PC', 'mobile_app', 'mobile_app_iphone', 'mobile_app_android', 'mobile_web_vela']
    for i in csv_path:
        print('csv path: ', i)
        ff = open('C:/Users/cao/Desktop/订单商品价格/' + i)
        csv_data = pd.read_csv(ff)
        new_customer_all = old_customer_first_all = old_customer_again_all = 0
        new_customer_pc = new_customer_iphone = new_customer_android = new_customer_web = 0
        old_customer_first_pc = old_customer_first_iphone = old_customer_first_android = old_customer_first_web = 0
        old_customer_again_pc = old_customer_again_iphone = old_customer_again_android = old_customer_again_web =0
        # for row in new_customer.iterrows():
        #     print(row)
        print('========================' + i + '新用户统计分析=============================')
        # 新用户统计分析
        new_customer = csv_data[csv_data.CUSTOMER_NEW_TYPE == 1]
        for index, data in new_customer.iterrows():
            new_customer_all += data.tolist()[1]
            if data.tolist()[5] == 'pc':
                new_customer_pc += data.tolist()[1]
            elif data.tolist()[5] == 'mobile_app_iphone':
                new_customer_iphone += data.tolist()[1]
            elif data.tolist()[5] == 'mobile_app_android':
                new_customer_android += data.tolist()[1]
            elif data.tolist()[5] == 'mobile_web_vela':
                new_customer_web += data.tolist()[1]
        new_customer_app = new_customer_iphone + new_customer_android
        dataset.append([new_customer_all, new_customer_pc, new_customer_app,
                        new_customer_iphone, new_customer_android, new_customer_web])
        print(dataset)
        print('====================' + i + '老用户第一次下单统计分析=========================')
        # 老用户第一次下单统计分析
        old_customer_first = csv_data[csv_data.CUSTOMER_NEW_TYPE == 2]
        for index, data in old_customer_first.iterrows():
            old_customer_first_all += data.tolist()[1]
            if data.tolist()[5] == 'pc':
                old_customer_first_pc += data.tolist()[1]
            elif data.tolist()[5] == 'mobile_app_iphone':
                old_customer_first_iphone += data.tolist()[1]
            elif data.tolist()[5] == 'mobile_app_android':
                old_customer_first_android += data.tolist()[1]
            elif data.tolist()[5] == 'mobile_web_vela':
                old_customer_first_web += data.tolist()[1]
        old_customer_first_app = old_customer_first_iphone + old_customer_first_android
        dataset.append([old_customer_first_all, old_customer_first_pc, old_customer_first_app,
                        old_customer_first_iphone, old_customer_first_android, old_customer_first_web])
        print(dataset)
        print('======================' + i + '老用户再下单统计分析==========================')
        # 老用户再次下单统计分析
        old_customer_again = csv_data[csv_data.CUSTOMER_NEW_TYPE == 3]
        for index, data in old_customer_again.iterrows():
            old_customer_again_all += data.tolist()[1]
            if data.tolist()[5] == 'pc':
                old_customer_again_pc += data.tolist()[1]
            elif data.tolist()[5] == 'mobile_app_iphone':
                old_customer_again_iphone += data.tolist()[1]
            elif data.tolist()[5] == 'mobile_app_android':
                old_customer_again_android += data.tolist()[1]
            elif data.tolist()[5] == 'mobile_web_vela':
                old_customer_again_web += data.tolist()[1]
        old_customer_again_app = old_customer_again_iphone + old_customer_again_android
        dataset.append([old_customer_again_all, old_customer_again_pc, old_customer_again_app,
                        old_customer_again_iphone, old_customer_again_android, old_customer_again_web])
        print(dataset)
    print('==========================写入文件================================')
    print(dataset)
    with open('C:/Users/cao/Desktop/订单商品价格/result.csv', mode='w', encoding='UTF-8') as f:
        f.write(dataset.csv)


def order_price_analysis(csv_path):
    dataset = tablib.Dataset()
    dataset.headers = ['all', 'PC', 'mobile_app', 'mobile_app_iphone', 'mobile_app_android', 'mobile_web_vela']
    for i in csv_path:
        print('csv path: ', i)
        f = open('C:/Users/cao/Desktop/订单商品价格/' + i)
        csv_data = pd.read_csv(f)

        price_0_10 = csv_data[csv_data.PRODUCTS_PRICE < 10]
        new_customer_all = old_customer_first_all = old_customer_again_all = 0
        new_customer_pc = new_customer_iphone = new_customer_android = new_customer_web = 0
        old_customer_first_pc = old_customer_first_iphone = old_customer_first_android = old_customer_first_web = 0
        old_customer_again_pc = old_customer_again_iphone = old_customer_again_android = old_customer_again_web = 0
        print('==========================' + i + '0-10 新用户统计分析================================')
        new_customer = price_0_10[price_0_10.CUSTOMER_NEW_TYPE == 1]
        for index, data in new_customer.iterrows():
            new_customer_all += data.tolist()[1]
            if data.tolist()[5] == 'pc':
                new_customer_pc += data.tolist()[1]
            elif data.tolist()[5] == 'mobile_app_iphone':
                new_customer_iphone += data.tolist()[1]
            elif data.tolist()[5] == 'mobile_app_android':
                new_customer_android += data.tolist()[1]
            elif data.tolist()[5] == 'mobile_web_vela':
                new_customer_web += data.tolist()[1]
        new_customer_app = new_customer_iphone + new_customer_android
        dataset.append([new_customer_all, new_customer_pc, new_customer_app,
                        new_customer_iphone, new_customer_android, new_customer_web])
        print('====================' + i + '0-10 老用户第一次下单统计分析=========================')
        old_customer_first = price_0_10[price_0_10.CUSTOMER_NEW_TYPE == 2]
        for index, data in old_customer_first.iterrows():
            old_customer_first_all += data.tolist()[1]
            if data.tolist()[5] == 'pc':
                old_customer_first_pc += data.tolist()[1]
            elif data.tolist()[5] == 'mobile_app_iphone':
                old_customer_first_iphone += data.tolist()[1]
            elif data.tolist()[5] == 'mobile_app_android':
                old_customer_first_android += data.tolist()[1]
            elif data.tolist()[5] == 'mobile_web_vela':
                old_customer_first_web += data.tolist()[1]
        old_customer_first_app = old_customer_first_iphone + old_customer_first_android
        dataset.append([old_customer_first_all, old_customer_first_pc, old_customer_first_app,
                        old_customer_first_iphone, old_customer_first_android, old_customer_first_web])
        print('======================' + i + '0-10 老用户再下单统计分析==========================')
        old_customer_again = price_0_10[price_0_10.CUSTOMER_NEW_TYPE == 3]
        for index, data in old_customer_again.iterrows():
            old_customer_again_all += data.tolist()[1]
            if data.tolist()[5] == 'pc':
                old_customer_again_pc += data.tolist()[1]
            elif data.tolist()[5] == 'mobile_app_iphone':
                old_customer_again_iphone += data.tolist()[1]
            elif data.tolist()[5] == 'mobile_app_android':
                old_customer_again_android += data.tolist()[1]
            elif data.tolist()[5] == 'mobile_web_vela':
                old_customer_again_web += data.tolist()[1]
        old_customer_again_app = old_customer_again_iphone + old_customer_again_android
        dataset.append([old_customer_again_all, old_customer_again_pc, old_customer_again_app,
                        old_customer_again_iphone, old_customer_again_android, old_customer_again_web])

        price_10_20 = csv_data[(csv_data.PRODUCTS_PRICE < 20) & (csv_data.PRODUCTS_PRICE >= 10)]
        new_customer_all = old_customer_first_all = old_customer_again_all = 0
        new_customer_pc = new_customer_iphone = new_customer_android = new_customer_web = 0
        old_customer_first_pc = old_customer_first_iphone = old_customer_first_android = old_customer_first_web = 0
        old_customer_again_pc = old_customer_again_iphone = old_customer_again_android = old_customer_again_web = 0
        print('==========================' + i + '10-20 新用户统计分析================================')
        new_customer = price_10_20[price_10_20.CUSTOMER_NEW_TYPE == 1]
        for index, data in new_customer.iterrows():
            new_customer_all += data.tolist()[1]
            if data.tolist()[5] == 'pc':
                new_customer_pc += data.tolist()[1]
            elif data.tolist()[5] == 'mobile_app_iphone':
                new_customer_iphone += data.tolist()[1]
            elif data.tolist()[5] == 'mobile_app_android':
                new_customer_android += data.tolist()[1]
            elif data.tolist()[5] == 'mobile_web_vela':
                new_customer_web += data.tolist()[1]
        new_customer_app = new_customer_iphone + new_customer_android
        dataset.append([new_customer_all, new_customer_pc, new_customer_app,
                        new_customer_iphone, new_customer_android, new_customer_web])
        print('====================' + i + '10-20 老用户第一次下单统计分析=========================')
        old_customer_first = price_10_20[price_10_20.CUSTOMER_NEW_TYPE == 2]
        for index, data in old_customer_first.iterrows():
            old_customer_first_all += data.tolist()[1]
            if data.tolist()[5] == 'pc':
                old_customer_first_pc += data.tolist()[1]
            elif data.tolist()[5] == 'mobile_app_iphone':
                old_customer_first_iphone += data.tolist()[1]
            elif data.tolist()[5] == 'mobile_app_android':
                old_customer_first_android += data.tolist()[1]
            elif data.tolist()[5] == 'mobile_web_vela':
                old_customer_first_web += data.tolist()[1]
        old_customer_first_app = old_customer_first_iphone + old_customer_first_android
        dataset.append([old_customer_first_all, old_customer_first_pc, old_customer_first_app,
                        old_customer_first_iphone, old_customer_first_android, old_customer_first_web])
        print('======================' + i + '10-20 老用户再下单统计分析==========================')
        old_customer_again = price_10_20[price_10_20.CUSTOMER_NEW_TYPE == 3]
        for index, data in old_customer_again.iterrows():
            old_customer_again_all += data.tolist()[1]
            if data.tolist()[5] == 'pc':
                old_customer_again_pc += data.tolist()[1]
            elif data.tolist()[5] == 'mobile_app_iphone':
                old_customer_again_iphone += data.tolist()[1]
            elif data.tolist()[5] == 'mobile_app_android':
                old_customer_again_android += data.tolist()[1]
            elif data.tolist()[5] == 'mobile_web_vela':
                old_customer_again_web += data.tolist()[1]
        old_customer_again_app = old_customer_again_iphone + old_customer_again_android
        dataset.append([old_customer_again_all, old_customer_again_pc, old_customer_again_app,
                        old_customer_again_iphone, old_customer_again_android, old_customer_again_web])

        price_20_50 = csv_data[(csv_data.PRODUCTS_PRICE < 50) & (csv_data.PRODUCTS_PRICE >= 20)]
        new_customer_all = old_customer_first_all = old_customer_again_all = 0
        new_customer_pc = new_customer_iphone = new_customer_android = new_customer_web = 0
        old_customer_first_pc = old_customer_first_iphone = old_customer_first_android = old_customer_first_web = 0
        old_customer_again_pc = old_customer_again_iphone = old_customer_again_android = old_customer_again_web = 0
        print('==========================' + i + '20-50 新用户统计分析================================')
        new_customer = price_20_50[price_20_50.CUSTOMER_NEW_TYPE == 1]
        for index, data in new_customer.iterrows():
            new_customer_all += data.tolist()[1]
            if data.tolist()[5] == 'pc':
                new_customer_pc += data.tolist()[1]
            elif data.tolist()[5] == 'mobile_app_iphone':
                new_customer_iphone += data.tolist()[1]
            elif data.tolist()[5] == 'mobile_app_android':
                new_customer_android += data.tolist()[1]
            elif data.tolist()[5] == 'mobile_web_vela':
                new_customer_web += data.tolist()[1]
        new_customer_app = new_customer_iphone + new_customer_android
        dataset.append([new_customer_all, new_customer_pc, new_customer_app,
                        new_customer_iphone, new_customer_android, new_customer_web])
        print('====================' + i + '20-50 老用户第一次下单统计分析=========================')
        old_customer_first = price_20_50[price_20_50.CUSTOMER_NEW_TYPE == 2]
        for index, data in old_customer_first.iterrows():
            old_customer_first_all += data.tolist()[1]
            if data.tolist()[5] == 'pc':
                old_customer_first_pc += data.tolist()[1]
            elif data.tolist()[5] == 'mobile_app_iphone':
                old_customer_first_iphone += data.tolist()[1]
            elif data.tolist()[5] == 'mobile_app_android':
                old_customer_first_android += data.tolist()[1]
            elif data.tolist()[5] == 'mobile_web_vela':
                old_customer_first_web += data.tolist()[1]
        old_customer_first_app = old_customer_first_iphone + old_customer_first_android
        dataset.append([old_customer_first_all, old_customer_first_pc, old_customer_first_app,
                        old_customer_first_iphone, old_customer_first_android, old_customer_first_web])
        print('======================' + i + '20-50 老用户再下单统计分析==========================')
        old_customer_again = price_20_50[price_20_50.CUSTOMER_NEW_TYPE == 3]
        for index, data in old_customer_again.iterrows():
            old_customer_again_all += data.tolist()[1]
            if data.tolist()[5] == 'pc':
                old_customer_again_pc += data.tolist()[1]
            elif data.tolist()[5] == 'mobile_app_iphone':
                old_customer_again_iphone += data.tolist()[1]
            elif data.tolist()[5] == 'mobile_app_android':
                old_customer_again_android += data.tolist()[1]
            elif data.tolist()[5] == 'mobile_web_vela':
                old_customer_again_web += data.tolist()[1]
        old_customer_again_app = old_customer_again_iphone + old_customer_again_android
        dataset.append([old_customer_again_all, old_customer_again_pc, old_customer_again_app,
                        old_customer_again_iphone, old_customer_again_android, old_customer_again_web])

        price_50_100 = csv_data[(csv_data.PRODUCTS_PRICE < 100) & (csv_data.PRODUCTS_PRICE >= 50)]
        new_customer_all = old_customer_first_all = old_customer_again_all = 0
        new_customer_pc = new_customer_iphone = new_customer_android = new_customer_web = 0
        old_customer_first_pc = old_customer_first_iphone = old_customer_first_android = old_customer_first_web = 0
        old_customer_again_pc = old_customer_again_iphone = old_customer_again_android = old_customer_again_web = 0
        print('==========================' + i + '20-50 新用户统计分析================================')
        new_customer = price_50_100[price_50_100.CUSTOMER_NEW_TYPE == 1]
        for index, data in new_customer.iterrows():
            new_customer_all += data.tolist()[1]
            if data.tolist()[5] == 'pc':
                new_customer_pc += data.tolist()[1]
            elif data.tolist()[5] == 'mobile_app_iphone':
                new_customer_iphone += data.tolist()[1]
            elif data.tolist()[5] == 'mobile_app_android':
                new_customer_android += data.tolist()[1]
            elif data.tolist()[5] == 'mobile_web_vela':
                new_customer_web += data.tolist()[1]
        new_customer_app = new_customer_iphone + new_customer_android
        dataset.append([new_customer_all, new_customer_pc, new_customer_app,
                        new_customer_iphone, new_customer_android, new_customer_web])
        print('====================' + i + '50-100 老用户第一次下单统计分析=========================')
        old_customer_first = price_50_100[price_50_100.CUSTOMER_NEW_TYPE == 2]
        for index, data in old_customer_first.iterrows():
            old_customer_first_all += data.tolist()[1]
            if data.tolist()[5] == 'pc':
                old_customer_first_pc += data.tolist()[1]
            elif data.tolist()[5] == 'mobile_app_iphone':
                old_customer_first_iphone += data.tolist()[1]
            elif data.tolist()[5] == 'mobile_app_android':
                old_customer_first_android += data.tolist()[1]
            elif data.tolist()[5] == 'mobile_web_vela':
                old_customer_first_web += data.tolist()[1]
        old_customer_first_app = old_customer_first_iphone + old_customer_first_android
        dataset.append([old_customer_first_all, old_customer_first_pc, old_customer_first_app,
                        old_customer_first_iphone, old_customer_first_android, old_customer_first_web])
        print('======================' + i + '20-50 老用户再下单统计分析==========================')
        old_customer_again = price_50_100[price_50_100.CUSTOMER_NEW_TYPE == 3]
        for index, data in old_customer_again.iterrows():
            old_customer_again_all += data.tolist()[1]
            if data.tolist()[5] == 'pc':
                old_customer_again_pc += data.tolist()[1]
            elif data.tolist()[5] == 'mobile_app_iphone':
                old_customer_again_iphone += data.tolist()[1]
            elif data.tolist()[5] == 'mobile_app_android':
                old_customer_again_android += data.tolist()[1]
            elif data.tolist()[5] == 'mobile_web_vela':
                old_customer_again_web += data.tolist()[1]
        old_customer_again_app = old_customer_again_iphone + old_customer_again_android
        dataset.append([old_customer_again_all, old_customer_again_pc, old_customer_again_app,
                        old_customer_again_iphone, old_customer_again_android, old_customer_again_web])

        price_100 = csv_data[csv_data.PRODUCTS_PRICE >= 100]
        new_customer_all = old_customer_first_all = old_customer_again_all = 0
        new_customer_pc = new_customer_iphone = new_customer_android = new_customer_web = 0
        old_customer_first_pc = old_customer_first_iphone = old_customer_first_android = old_customer_first_web = 0
        old_customer_again_pc = old_customer_again_iphone = old_customer_again_android = old_customer_again_web = 0
        print('==========================' + i + '100+ 新用户统计分析================================')
        new_customer = price_100[price_100.CUSTOMER_NEW_TYPE == 1]
        for index, data in new_customer.iterrows():
            new_customer_all += data.tolist()[1]
            if data.tolist()[5] == 'pc':
                new_customer_pc += data.tolist()[1]
            elif data.tolist()[5] == 'mobile_app_iphone':
                new_customer_iphone += data.tolist()[1]
            elif data.tolist()[5] == 'mobile_app_android':
                new_customer_android += data.tolist()[1]
            elif data.tolist()[5] == 'mobile_web_vela':
                new_customer_web += data.tolist()[1]
        new_customer_app = new_customer_iphone + new_customer_android
        dataset.append([new_customer_all, new_customer_pc, new_customer_app,
                        new_customer_iphone, new_customer_android, new_customer_web])
        print('====================' + i + '100+ 老用户第一次下单统计分析=========================')
        old_customer_first = price_100[price_100.CUSTOMER_NEW_TYPE == 2]
        for index, data in old_customer_first.iterrows():
            old_customer_first_all += data.tolist()[1]
            if data.tolist()[5] == 'pc':
                old_customer_first_pc += data.tolist()[1]
            elif data.tolist()[5] == 'mobile_app_iphone':
                old_customer_first_iphone += data.tolist()[1]
            elif data.tolist()[5] == 'mobile_app_android':
                old_customer_first_android += data.tolist()[1]
            elif data.tolist()[5] == 'mobile_web_vela':
                old_customer_first_web += data.tolist()[1]
        old_customer_first_app = old_customer_first_iphone + old_customer_first_android
        dataset.append([old_customer_first_all, old_customer_first_pc, old_customer_first_app,
                        old_customer_first_iphone, old_customer_first_android, old_customer_first_web])
        print('======================' + i + '100+ 老用户再下单统计分析==========================')
        old_customer_again = price_100[price_100.CUSTOMER_NEW_TYPE == 3]
        for index, data in old_customer_again.iterrows():
            old_customer_again_all += data.tolist()[1]
            if data.tolist()[5] == 'pc':
                old_customer_again_pc += data.tolist()[1]
            elif data.tolist()[5] == 'mobile_app_iphone':
                old_customer_again_iphone += data.tolist()[1]
            elif data.tolist()[5] == 'mobile_app_android':
                old_customer_again_android += data.tolist()[1]
            elif data.tolist()[5] == 'mobile_web_vela':
                old_customer_again_web += data.tolist()[1]
        old_customer_again_app = old_customer_again_iphone + old_customer_again_android
        dataset.append([old_customer_again_all, old_customer_again_pc, old_customer_again_app,
                        old_customer_again_iphone, old_customer_again_android, old_customer_again_web])

    print('==========================写入文件================================')
    print(dataset)
    with open('C:/Users/cao/Desktop/订单商品价格/result.csv', mode='w', encoding='UTF-8') as f:
        f.write(dataset.csv)


def purchase_behavior(csv_path):
    dataset = tablib.Dataset()
    dataset.headers = ['all', 'PC', 'mobile_app', 'mobile_app_iphone', 'mobile_app_android', 'mobile_web_vela']
    csv_path = 'C:/Users/cao/Desktop/订单商品价格/1218-0118.csv'
    csv_data = pd.read_csv(csv_path)
    purchase_all_1 = purchase_all_2 = purchase_all_3 = purchase_all_4 = 0
    purchase_pc_1 = purchase_pc_2 = purchase_pc_3 = purchase_pc_4 = 0
    purchase_app_1 = purchase_app_2 = purchase_app_3 = purchase_app_4 = 0
    purchase_iphone_1 = purchase_iphone_2 = purchase_iphone_3 = purchase_iphone_4 = 0
    purchase_android_1 = purchase_android_2 = purchase_android_3 = purchase_android_4 = 0
    purchase_web_1 = purchase_web_2 = purchase_web_3 = purchase_web_4 = 0

    print('==========================CUSTOMER_NEW_TYPE == 3================================')
    new_customer = csv_data[csv_data.CUSTOMER_NEW_TYPE == 3]
    # 订单金额分析
    new_price_all = new_customer.SALES.tolist()
    max_price = max(new_price_all)
    min_price = min(new_price_all)
    average_price = np.mean(new_price_all)
    median_price = np.median(new_price_all)
    print(round(min_price, 2), round(max_price, 2), round(average_price, 2), round(median_price, 2))
    print('==========================APPLICATION_TYPE == pc================================')
    new_price_pc = new_customer[new_customer.APPLICATION_TYPE == 'pc'].SALES.tolist()
    max_price = max(new_price_pc)
    min_price = min(new_price_pc)
    average_price = np.mean(new_price_pc)
    median_price = np.median(new_price_pc)
    print(round(min_price, 2), round(max_price, 2), round(average_price, 2), round(median_price, 2))
    print('==========================APPLICATION_TYPE == app================================')
    new_price_app = new_customer[new_customer.APPLICATION_TYPE == 'mobile_app_iphone'].SALES.tolist() +\
                    new_customer[new_customer.APPLICATION_TYPE == 'mobile_app_android'].SALES.tolist()
    max_price = max(new_price_app)
    min_price = min(new_price_app)
    average_price = np.mean(new_price_app)
    median_price = np.median(new_price_app)
    print(round(min_price, 2), round(max_price, 2), round(average_price, 2), round(median_price, 2))
    print('==========================APPLICATION_TYPE == iphone================================')
    new_price_iphone = new_customer[new_customer.APPLICATION_TYPE == 'mobile_app_iphone'].SALES.tolist()
    max_price = max(new_price_iphone)
    min_price = min(new_price_iphone)
    average_price = np.mean(new_price_iphone)
    median_price = np.median(new_price_iphone)
    print(round(min_price, 2), round(max_price, 2), round(average_price, 2), round(median_price, 2))
    print('==========================APPLICATION_TYPE == android================================')
    new_price_android = new_customer[new_customer.APPLICATION_TYPE == 'mobile_app_android'].SALES.tolist()
    max_price = max(new_price_android)
    min_price = min(new_price_android)
    average_price = np.mean(new_price_android)
    median_price = np.median(new_price_android)
    print(round(min_price, 2), round(max_price, 2), round(average_price, 2), round(median_price, 2))
    print('==========================APPLICATION_TYPE == web================================')
    new_price_web = new_customer[new_customer.APPLICATION_TYPE == 'mobile_web_vela'].SALES.tolist()
    max_price = max(new_price_web)
    min_price = min(new_price_web)
    average_price = np.mean(new_price_web)
    median_price = np.median(new_price_web)
    print(round(min_price, 2), round(max_price, 2), round(average_price, 2), round(median_price, 2))

    # 下单次数分析
    new_all_list = new_customer.CUSTOMERS_ID.tolist()
    new_pc_list = new_customer[new_customer.APPLICATION_TYPE == 'pc'].CUSTOMERS_ID.tolist()
    new_iphone_list = new_customer[new_customer.APPLICATION_TYPE == 'mobile_app_iphone'].CUSTOMERS_ID.tolist()
    new_android_list = new_customer[new_customer.APPLICATION_TYPE == 'mobile_app_android'].CUSTOMERS_ID.tolist()
    new_web_list = new_customer[new_customer.APPLICATION_TYPE == 'mobile_web_vela'].CUSTOMERS_ID.tolist()
    all_count = Counter(new_all_list)
    pc_count = Counter(new_pc_list)
    iphone_count = Counter(new_iphone_list)
    android_count = Counter(new_android_list)
    web_count = Counter(new_web_list)
    for customer_id, purchases in all_count.items():
        if purchases == 1:
            purchase_all_1 += 1
        elif purchases == 2:
            purchase_all_2 += 1
        elif purchases == 3:
            purchase_all_3 += 1
        elif purchases >= 4:
            purchase_all_4 += 1
    for customer_id, purchases in pc_count.items():
        if purchases == 1:
            purchase_pc_1 += 1
        elif purchases == 2:
            purchase_pc_2 += 1
        elif purchases == 3:
            purchase_pc_3 += 1
        elif purchases >= 4:
            purchase_pc_4 += 1
    for customer_id, purchases in iphone_count.items():
        if purchases == 1:
            purchase_iphone_1 += 1
        elif purchases == 2:
            purchase_iphone_2 += 1
        elif purchases == 3:
            purchase_iphone_3 += 1
        elif purchases >= 4:
            purchase_iphone_4 += 1
    for customer_id, purchases in android_count.items():
        if purchases == 1:
            purchase_android_1 += 1
        elif purchases == 2:
            purchase_android_2 += 1
        elif purchases == 3:
            purchase_android_3 += 1
        elif purchases >= 4:
            purchase_android_4 += 1
    for customer_id, purchases in web_count.items():
        if purchases == 1:
            purchase_web_1 += 1
        elif purchases == 2:
            purchase_web_2 += 1
        elif purchases == 3:
            purchase_web_3 += 1
        elif purchases >= 4:
            purchase_web_4 += 1
    dataset.append([purchase_all_1, purchase_pc_1, purchase_iphone_1 + purchase_android_1,
                    purchase_iphone_1, purchase_android_1, purchase_web_1])
    dataset.append([purchase_all_2, purchase_pc_2, purchase_iphone_2 + purchase_android_2,
                    purchase_iphone_2, purchase_android_2, purchase_web_2])
    dataset.append([purchase_all_3, purchase_pc_3, purchase_iphone_3 + purchase_android_3,
                    purchase_iphone_3, purchase_android_3, purchase_web_3])
    dataset.append([purchase_all_4, purchase_pc_4, purchase_iphone_4 + purchase_android_4,
                    purchase_iphone_4, purchase_android_4, purchase_web_4])
    print(dataset)
    with open('C:/Users/cao/Desktop/订单商品价格/result.csv', mode='w', encoding='UTF-8') as f:
        f.write(dataset.csv)


def mixing_gaussian():
    x_71 =[]
    y_71 = []
    # 混合高斯模型，多个高斯函数相加
    def func3(x, a1, a2, a3, m1, m2, m3, s1, s2, s3):
        return a1 * np.exp(-((x - m1) / s1) ** 2) + a2 * np.exp(-((x - m2) / s2) ** 2) + a3 * np.exp(
            -((x - m3) / s3) ** 2)

    popt, pcov = curve_fit(func3, x_71, y_71)
    a1 = popt[0]
    u1 = popt[1]
    sig1 = popt[2]
    a2 = popt[3]
    u2 = popt[4]
    sig2 = popt[5]
    a3 = popt[6]
    u3 = popt[7]
    sig3 = popt[8]

    for k in x_71:
        print('original values', k)
        print('polyfit values', func3(k))
    # 绘图
    yvals = func3(x_71, a1, u1, sig1, a2, u2, sig2, a3, u3, sig3)  # 拟合y值
    plot3 = plt.plot(x_71, y_71, 's', label='original values')
    plot4 = plt.plot(x_71, yvals, 'r', label='polyfit values')
    plt.legend(loc=4)  # 指定legend的位置右下角
    plt.title('poly fitting')
    plt.show()


def cid1_analysis():
    # 单个高斯模型
    def gaussian_func(x, a, u, sig):
        return a * np.exp(-(x - u) ** 2 / (2 * sig ** 2)) / (sig * math.sqrt(2 * math.pi))

    ahunt = 2686808.8844860797
    uhunt = 16.92849780388349
    sighunt = 8.416499193640043
    a = gaussian_func(uhunt, ahunt, uhunt, sighunt)   # a 为峰值
    price_score = gaussian_func(9.9, ahunt, uhunt, sighunt) / gaussian_func(uhunt, ahunt, uhunt, sighunt)
    price_score2 = gaussian_func(16, ahunt, uhunt, sighunt) / gaussian_func(uhunt, ahunt, uhunt, sighunt)
    price_score3 = gaussian_func(26.7, ahunt, uhunt, sighunt) / gaussian_func(uhunt, ahunt, uhunt, sighunt)
    price_score4 = gaussian_func(50.2, ahunt, uhunt, sighunt) / gaussian_func(uhunt, ahunt, uhunt, sighunt)

    # 公式：math.exp(-(x - uhunt) ** 2 / (2 * sighunt ** 2))
    price_score_1 = math.exp(-(9.9 - uhunt) ** 2 / (2 * sighunt ** 2))
    price_score_2 = math.exp(-(16 - uhunt) ** 2 / (2 * sighunt ** 2))
    price_score_3 = math.exp(-(26.7 - uhunt) ** 2 / (2 * sighunt ** 2))
    price_score_4 = math.exp(-(50.2 - uhunt) ** 2 / (2 * sighunt ** 2))
    # price_score (0, 1]

    # dataset = tablib.Dataset()
    # dataset.headers = ['all', 'PC', 'mobile_app', 'mobile_app_iphone', 'mobile_app_android', 'mobile_web_vela']
    csv_path = 'E:/LITB_file/数据统计分析/一级品类价格区间分布/ALL_CMS_CATID1.csv'
    csv_data = pd.read_csv(csv_path)
    cms_catid1 = csv_data.CMS_CATID1.tolist()
    cat_qty = csv_data.PRODUCTS_QTY.tolist()
    cat_price = csv_data.PRODUCTS_PRICE.tolist()
    # 全站商品分布计算
    cat_price_all = []
    for i in range(len(cms_catid1)):
        for j in range(0, cat_qty[i]):
            cat_price_all.append(round(cat_price[i]))
    all_re = Counter(cat_price_all)
    x_all = []
    y_all = []
    for keys, values in all_re.items():
        x_all.append(keys)
        y_all.append(values)
    print("len(x_cid):", len(x_all), "  len(Y_cid):", len(y_all))
    if len(x_all) > 0:
        opthunt, pcovhunt = curve_fit(gaussian_func, x_all, y_all, p0=[2, 2, 2])

        ahunt = opthunt[0]
        uhunt = opthunt[1]
        sighunt = opthunt[2]
        print("---ahunt:", ahunt, "---uhunt:", uhunt, "----sighunt:", sighunt)

    # 分一级品类计算
    cid_list = [71, 75, 76, 2619, 2623, 3349, 1015, 10333, 1180, 229, 5585, 5830, 59321, 62902]
    # cid = 3349    # 一级品类 ：71 75 76 2619 2623 3349 1015 10333 1180 229 5585 5830 59321 62902；
    for cid in cid_list:
        print(cid)
        cat_price_cid = []
        for i in range(len(cms_catid1)):
            if cms_catid1[i] == cid:
                for j in range(0, cat_qty[i]):
                    cat_price_cid.append(round(cat_price[i]))
        re = Counter(cat_price_cid)
        print(re)
        x_cid =[]
        y_cid = []
        for keys, values in re.items():
            x_cid.append(keys)
            y_cid.append(values)
        print("len(x_cid):", len(x_cid), "  len(Y_cid):", len(y_cid))
        if len(x_cid) > 0:
            opthunt, pcovhunt = curve_fit(gaussian_func, x_cid, y_cid, p0=[2, 2, 2])

            ahunt = opthunt[0]
            uhunt = opthunt[1]
            sighunt = opthunt[2]
            print("---ahunt:", ahunt, "---uhunt:", uhunt, "----sighunt:", sighunt)

            price_score = gaussian_func(x_cid, ahunt, uhunt, sighunt)

            # 绘图
            plot1 = plt.plot(x_cid, y_cid, 'ob', label='original values')
            plot2 = plt.plot(x_cid, price_score, 'or', label='polyfit values')
            plt.legend(loc=4)  # 指定legend的位置右下角
            plt.title('cid = ' + str(cid) + 'ploy fitting')
            plt.show()

    # set1 = set(cms_catid1)
    # print(set1)
    # cat_id_1 = cat_id_71 = cat_id_75 = cat_id_76 = cat_id_10333 = cat_id_10381 = cat_id_229 = cat_id_2394 = \
    #     cat_id_2619 = cat_id_2623 = cat_id_2624 = cat_id_4676 = cat_id_4685 = cat_id_4739 = cat_id_6829 = \
    #     cat_id_4861 = cat_id_4921 = cat_id_3019 = cat_id_3021 = cat_id_3026 = cat_id_1180 = cat_id_13496 = \
    #     cat_id_1015 = cat_id_3303 = cat_id_13398 = cat_id_3349 = cat_id_5488 = cat_id_62902 = cat_id_5585 = \
    #     cat_id_112645 = cat_id_15895 = cat_id_5830 = cat_id_8017 = cat_id_59321 = cat_id_109491 = 0
    # for i in range(len(cms_catid1)):
    #     if 100 <= cat_price[i]:
    #         if cms_catid1[i] == 1:
    #             cat_id_1 += cat_qty[i]
    #         elif cms_catid1[i] == 71:
    #             cat_id_71 += cat_qty[i]
    #         elif cms_catid1[i] == 75:
    #             cat_id_75 += cat_qty[i]
    #         elif cms_catid1[i] == 76:
    #             cat_id_76 += cat_qty[i]
    #         elif cms_catid1[i] == 10333:
    #             cat_id_10333 += cat_qty[i]
    #         elif cms_catid1[i] == 10381:
    #             cat_id_10381 += cat_qty[i]
    #         elif cms_catid1[i] == 229:
    #             cat_id_229 += cat_qty[i]
    #         elif cms_catid1[i] == 2394:
    #             cat_id_2394 += cat_qty[i]
    #         elif cms_catid1[i] == 2619:
    #             cat_id_2619 += cat_qty[i]
    #         elif cms_catid1[i] == 2623:
    #             cat_id_2623 += cat_qty[i]
    #         elif cms_catid1[i] == 2624:
    #             cat_id_2624 += cat_qty[i]
    #         elif cms_catid1[i] == 4676:
    #             cat_id_4676 += cat_qty[i]
    #         elif cms_catid1[i] == 4685:
    #             cat_id_4685 += cat_qty[i]
    #         elif cms_catid1[i] == 4739:
    #             cat_id_4739 += cat_qty[i]
    #         elif cms_catid1[i] == 6829:
    #             cat_id_6829 += cat_qty[i]
    #         elif cms_catid1[i] == 4861:
    #             cat_id_4861 += cat_qty[i]
    #         elif cms_catid1[i] == 4921:
    #             cat_id_4921 += cat_qty[i]
    #         elif cms_catid1[i] == 3019:
    #             cat_id_3019 += cat_qty[i]
    #         elif cms_catid1[i] == 3021:
    #             cat_id_3021 += cat_qty[i]
    #         elif cms_catid1[i] == 3026:
    #             cat_id_3026 += cat_qty[i]
    #         elif cms_catid1[i] == 1180:
    #             cat_id_1180 += cat_qty[i]
    #         elif cms_catid1[i] == 13496:
    #             cat_id_13496 += cat_qty[i]
    #         elif cms_catid1[i] == 1015:
    #             cat_id_1015 += cat_qty[i]
    #         elif cms_catid1[i] == 3303:
    #             cat_id_3303 += cat_qty[i]
    #         elif cms_catid1[i] == 13398:
    #             cat_id_13398 += cat_qty[i]
    #         elif cms_catid1[i] == 3349:
    #             cat_id_3349 += cat_qty[i]
    #         elif cms_catid1[i] == 5488:
    #             cat_id_5488 += cat_qty[i]
    #         elif cms_catid1[i] == 62902:
    #             cat_id_62902 += cat_qty[i]
    #         elif cms_catid1[i] == 5585:
    #             cat_id_5585 += cat_qty[i]
    #         elif cms_catid1[i] == 112645:
    #             cat_id_112645 += cat_qty[i]
    #         elif cms_catid1[i] == 15895:
    #             cat_id_15895 += cat_qty[i]
    #         elif cms_catid1[i] == 5830:
    #             cat_id_5830 += cat_qty[i]
    #         elif cms_catid1[i] == 8017:
    #             cat_id_8017 += cat_qty[i]
    #         elif cms_catid1[i] == 59321:
    #             cat_id_59321 += cat_qty[i]
    #         elif cms_catid1[i] == 109491:
    #             cat_id_109491 += cat_qty[i]
    print('all')


if __name__ == '__main__':
    print('==========~start~=============')
    csv_path = 'C:/Users/cao/Desktop/select_la.csv'
    csv_data = pd.read_csv(csv_path)
    merchant_data = csv_data.merchant.tolist()
    print(Counter(merchant_data))
    # cid1_analysis()
    # csv_path = os.listdir('C:/Users/cao/Desktop/')
    # order_analysis(csv_path)
    # order_price_analysis(csv_path)
    # purchase_behavior(csv_path)
    print('==========~done~=============')