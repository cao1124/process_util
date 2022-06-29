import os
from enum import Enum
import pandas as pd
import tablib


class SkinDisease22(Enum):
    其他良性 = 0              # 其他良性 other benign
    神经源性肿瘤 = 1             # 神经源性肿瘤 Benign Neurogenic tumors
    良性毛囊肿瘤 = 2             # 良性毛囊肿瘤 Benign follicular tumor
    良性皮脂腺肿瘤 = 3            # 良性皮脂腺肿瘤   Benign sebaceous gland tumor
    良性角化病样病变 = 4            # 良性角化病样病变 Benign keratosis like lesions
    良性纤维母细胞和肌纤维母细胞肿瘤 = 5            # 良性纤维母细胞和肌纤维母细胞肿瘤  Benign fibroblastic and myofibroblastic tumors
    良性汗腺肿瘤 = 6            # 良性汗腺肿瘤  Benign sweat gland tumor
    血管瘤 = 7            # 血管瘤 Hemangioma
    囊肿 = 8            # 囊肿 cyst
    炎症 = 9            # 炎症 inflammation
    疣 = 10           # 疣  wart
    脂肪瘤 = 11           # 脂肪瘤 lipoma
    痣 = 12           # 痣 nevus

    其他恶性 = 13             # 其他恶性 Other malignancies
    BD = 14
    AK = 15
    MM = 16
    SCC = 17
    BCC = 18
    腺癌 = 19           # 腺癌 Adenocarcinoma
    隆突性皮肤纤维肉瘤 = 20           # 隆突性皮肤纤维肉瘤  Dermatofibrosarcoma protuberans
    Paget = 21


class SkinDisease27(Enum):
    神经源性肿瘤 = 0
    良性毛囊肿瘤 = 1
    化脓性肉芽肿 = 2
    皮脂腺痣 = 3
    囊肿 = 4
    良性角化病样病变 = 5
    炎症 = 6
    疣 = 7
    良性皮脂腺肿瘤 = 8
    甲下良性肿瘤 = 9
    皮肤纤维瘤 = 10
    痣 = 11
    毛母质瘤 = 12
    脂肪瘤 = 13
    瘢痕 = 14
    血管瘤 = 15
    良性汗腺肿瘤 = 16
    其他良性 = 17

    SCC = 18
    Paget = 19
    BD = 20
    BCC = 21
    腺癌 = 22
    隆突性皮肤纤维肉瘤 = 23
    AK = 24
    MM = 25
    其他恶性 = 26


def is_image_file(filename):
    return any(filename.endswith(extension) for extension in ['.png', '.PNG', '.jpg', '.jpeg',  '.JPG', '.JPEG', '.bmp',
                                                              '.BMP', '.tiff', '.TIFF', ])


def rename_file():
    img_dir = 'D:/MAD_File/上海_皮肤病/上海_皮肤病/us_img/'
    # images = [os.path.join(img_dir, x) for x in os.listdir(img_dir) if is_image_file(x)]
    images = os.listdir(img_dir)
    for name in images:
        new_name = name.replace('_', '.')
        os.rename(os.path.join(img_dir, name), os.path.join(img_dir, new_name))


def data_prepare():
    dataset = tablib.Dataset()
    dataset.headers = ['id', 'class', 'disease']
    # img_dir = 'D:/MAD_File/上海_皮肤病/上海_皮肤病/us_img_2class/'
    # images = os.listdir(img_dir)
    excel_path = 'D:/MAD_File/上海_皮肤病/上海_皮肤病/训练组1361例.xlsx'
    excel_data = pd.read_excel(excel_path)
    num_list = excel_data.病原号.tolist()
    benign_malignant = excel_data.良恶性.tolist()
    disease_list = excel_data.病理分组.tolist()
    describe_list = excel_data.分组描述.tolist()
    for i in range(len(num_list)):
        img_id = num_list[i]
        img_class = benign_malignant[i]
        disease = disease_list[i]
        describe = describe_list[i]
        # img_class = int(img.split('_')[-1].split('.')[0])
        # print(img_class)
        if img_class == 0:          # 良性
            if '良性皮脂腺肿瘤' in disease or '皮脂腺痣' in disease:
                dataset.append([img_id, 3, '良性皮脂腺肿瘤'])
            elif '痣' in disease:
                dataset.append([img_id, 12, '痣'])
            elif '脂肪瘤' in disease:
                dataset.append([img_id, 11, '脂肪瘤'])
            elif '疣' in disease:
                dataset.append([img_id, 10, '疣'])
            elif '炎症' in disease:
                dataset.append([img_id, 9, '炎症'])
            elif '囊肿' in disease:
                dataset.append([img_id, 8, '囊肿'])
            elif '血管瘤' in disease or '化脓性肉芽肿' in disease:
                dataset.append([img_id, 7, '血管瘤'])
            elif '良性汗腺肿瘤' in disease:
                dataset.append([img_id, 6, '良性汗腺肿瘤'])
            elif '良性纤维母细胞' in disease or '肌纤维母细胞肿瘤' in disease or '瘢痕' in disease \
                    or '皮肤纤维瘤' in disease or describe == '血管平滑肌瘤':
                dataset.append([img_id, 5, '良性纤维母细胞和肌纤维母细胞肿瘤'])
            elif '良性角化病样病变' in disease:
                dataset.append([img_id, 4, '良性角化病样病变'])
            elif '良性毛囊肿瘤' in disease or '毛母质瘤' in disease:
                dataset.append([img_id, 2, '良性毛囊肿瘤'])
            elif '神经源性肿瘤' in disease:
                dataset.append([img_id, 1, '神经源性肿瘤'])
            else:
                dataset.append([img_id, 0, '其他良性'])
        elif img_class == 1:  # 恶性
            if 'Paget' in disease:
                dataset.append([img_id, 21, 'Paget'])
            elif '隆突性皮肤纤维肉瘤' in disease:
                dataset.append([img_id, 20, '隆突性皮肤纤维肉瘤'])
            elif '腺癌' in disease:
                dataset.append([img_id, 19, '腺癌'])
            elif 'BCC' in disease:
                dataset.append([img_id, 18, 'BCC'])
            elif 'SCC' in disease:
                dataset.append([img_id, 17, 'SCC'])
            elif 'MM' in disease:
                dataset.append([img_id, 16, 'MM'])
            elif 'AK' in disease:
                dataset.append([img_id, 15, 'AK'])
            elif 'BD' in disease:
                dataset.append([img_id, 14, 'BD'])
            else:
                dataset.append([img_id, 13, '其他恶性'])
    with open('D:/MAD_File/上海_皮肤病/上海_皮肤病/multi_class.csv', mode='w', encoding='UTF-8') as f:
        f.write(dataset.csv)


def data_prepare2():
    dataset = tablib.Dataset()
    dataset.headers = ['id', 'class', 'disease']
    excel_path = 'D:/MAD_File/上海_皮肤病/上海_皮肤病/1326_multi_class.xlsx'
    excel_data = pd.read_excel(excel_path)
    id_list = excel_data.id.tolist()
    class_list = excel_data.multi_class.tolist()
    for i in range(len(id_list)):
        img_class = class_list[i]
        disease = id_list[i]
        # img_class = int(img.split('_')[-1].split('.')[0])
        # print(img_class)
        if img_class < 13:  # 良性
            if '良性皮脂腺肿瘤' in disease or '皮脂腺痣' in disease:
                dataset.append([disease, 3, '良性皮脂腺肿瘤'])
            elif '痣' in disease:
                dataset.append([disease, 12, '痣'])
            elif '脂肪瘤' in disease:
                dataset.append([disease, 11, '脂肪瘤'])
            elif '疣' in disease:
                dataset.append([disease, 10, '疣'])
            elif '炎症' in disease:
                dataset.append([disease, 9, '炎症'])
            elif '囊肿' in disease:
                dataset.append([disease, 8, '囊肿'])
            elif '血管瘤' in disease or '化脓性肉芽肿' in disease:
                dataset.append([disease, 7, '血管瘤'])
            elif '良性汗腺肿瘤' in disease:
                dataset.append([disease, 6, '良性汗腺肿瘤'])
            elif '良性纤维母细胞' in disease or '肌纤维母细胞肿瘤' in disease or '瘢痕' in disease \
                    or '皮肤纤维瘤' in disease or '血管平滑肌瘤' in disease:
                dataset.append([disease, 5, '良性纤维母细胞和肌纤维母细胞肿瘤'])
            elif '良性角化病样病变' in disease:
                dataset.append([disease, 4, '良性角化病样病变'])
            elif '良性毛囊肿瘤' in disease or '毛母质瘤' in disease:
                dataset.append([disease, 2, '良性毛囊肿瘤'])
            elif '神经源性肿瘤' in disease:
                dataset.append([disease, 1, '神经源性肿瘤'])
            else:
                dataset.append([disease, 0, '其他良性'])
        else:  # 恶性
            if 'Paget' in disease:
                dataset.append([disease, 21, 'Paget'])
            elif '隆突性皮肤纤维肉瘤' in disease:
                dataset.append([disease, 20, '隆突性皮肤纤维肉瘤'])
            elif '腺癌' in disease:
                dataset.append([disease, 19, '腺癌'])
            elif 'BCC' in disease:
                dataset.append([disease, 18, 'BCC'])
            elif 'SCC' in disease:
                dataset.append([disease, 17, 'SCC'])
            elif 'MM' in disease:
                dataset.append([disease, 16, 'MM'])
            elif 'AK' in disease:
                dataset.append([disease, 15, 'AK'])
            elif 'BD' in disease:
                dataset.append([disease, 14, 'BD'])
            else:
                dataset.append([disease, 13, '其他恶性'])
    with open('D:/MAD_File/上海_皮肤病/上海_皮肤病/multi_class.csv', mode='w', encoding='UTF-8') as f:
        f.write(dataset.csv)


def data_prepare_all():
    dataset = tablib.Dataset()
    dataset.headers = ['id', 'class', 'disease']
    excel_path = 'D:/MAD_File/上海_皮肤病/训练组1361例.xlsx'
    excel_data = pd.read_excel(excel_path)
    num_list = excel_data.病原号.tolist()
    benign_malignant = excel_data.良恶性.tolist()
    disease_list = excel_data.病理分组.tolist()
    for i in range(len(num_list)):
        img_id = num_list[i]
        img_class = benign_malignant[i]
        disease = disease_list[i]
        if img_class == 0:  # 良性
            if '神经源性肿瘤' in disease:
                dataset.append([img_id, SkinDisease27.神经源性肿瘤.value, SkinDisease27.神经源性肿瘤.name])
            elif '良性毛囊肿瘤' in disease:
                dataset.append([img_id, SkinDisease27.良性毛囊肿瘤.value, SkinDisease27.良性毛囊肿瘤.name])
            elif '化脓性肉芽肿' in disease:
                dataset.append([img_id, SkinDisease27.化脓性肉芽肿.value, SkinDisease27.化脓性肉芽肿.name])
            elif '皮脂腺痣' in disease:
                dataset.append([img_id, SkinDisease27.皮脂腺痣.value, SkinDisease27.皮脂腺痣.name])
            elif '良性角化病样病变' in disease:
                dataset.append([img_id, SkinDisease27.良性角化病样病变.value, SkinDisease27.良性角化病样病变.name])
            elif '炎症' in disease:
                dataset.append([img_id, SkinDisease27.炎症.value, SkinDisease27.炎症.name])
            elif '疣' in disease:
                dataset.append([img_id, SkinDisease27.疣.value, SkinDisease27.疣.name])
            elif '良性皮脂腺肿瘤' in disease:
                dataset.append([img_id, SkinDisease27.良性皮脂腺肿瘤.value, SkinDisease27.良性皮脂腺肿瘤.name])
            elif '甲下良性肿瘤' in disease:
                dataset.append([img_id, SkinDisease27.甲下良性肿瘤.value, SkinDisease27.甲下良性肿瘤.name])
            elif '皮肤纤维瘤' in disease:
                dataset.append([img_id, SkinDisease27.皮肤纤维瘤.value, SkinDisease27.皮肤纤维瘤.name])
            elif '毛母质瘤' in disease:
                dataset.append([img_id, SkinDisease27.毛母质瘤.value, SkinDisease27.毛母质瘤.name])
            elif '脂肪瘤' in disease:
                dataset.append([img_id, SkinDisease27.脂肪瘤.value, SkinDisease27.脂肪瘤.name])
            elif '瘢痕' in disease:
                dataset.append([img_id, SkinDisease27.瘢痕.value, SkinDisease27.瘢痕.name])
            elif '血管瘤' in disease:
                dataset.append([img_id, SkinDisease27.血管瘤.value, SkinDisease27.血管瘤.name])
            elif '良性汗腺肿瘤' in disease:
                dataset.append([img_id, SkinDisease27.良性汗腺肿瘤.value, SkinDisease27.良性汗腺肿瘤.name])
            elif '囊肿' in disease:
                dataset.append([img_id, SkinDisease27.囊肿.value, SkinDisease27.囊肿.name])
            elif '痣' in disease:
                dataset.append([img_id, SkinDisease27.痣.value, SkinDisease27.痣.name])
            else:
                dataset.append([img_id, SkinDisease27.其他良性.value, SkinDisease27.其他良性.name])
        elif img_class == 1:  # 恶性
            if 'SCC' in disease:
                dataset.append([img_id, SkinDisease27.SCC.value, SkinDisease27.SCC.name])
            elif 'Paget' in disease:
                dataset.append([img_id, SkinDisease27.Paget.value, SkinDisease27.Paget.name])
            elif 'BD' in disease:
                dataset.append([img_id, SkinDisease27.BD.value, SkinDisease27.BD.name])
            elif 'BCC' in disease:
                dataset.append([img_id, SkinDisease27.BCC.value, SkinDisease27.BCC.name])
            elif '腺癌' in disease:
                dataset.append([img_id, SkinDisease27.腺癌.value, SkinDisease27.腺癌.name])
            elif '隆突性皮肤纤维肉瘤' in disease:
                dataset.append([img_id, SkinDisease27.隆突性皮肤纤维肉瘤.value, SkinDisease27.隆突性皮肤纤维肉瘤.name])
            elif 'AK' in disease:
                dataset.append([img_id, SkinDisease27.AK.value, SkinDisease27.AK.name])
            elif 'MM' in disease:
                dataset.append([img_id, SkinDisease27.MM.value, SkinDisease27.MM.name])
            else:
                dataset.append([img_id, SkinDisease27.其他恶性.value, SkinDisease27.其他恶性.name])
    with open('similarity_calculate.xlsx', mode='wb') as f:
        f.write(dataset.xlsx)


def prepare_txt():
    excel_path = 'C:/Users/cao_1/Desktop/skin.xlsx'
    excel_data = pd.read_excel(excel_path)
    num_list = excel_data.id.tolist()
    class_list = excel_data.classes.tolist()
    disease_list = excel_data.disease.tolist()

    image_dir = "D:/PycharmProjects/data/skin_data/us_label_mask1/expand_images/square"
    images = [x for x in os.listdir(image_dir) if is_image_file(x)]
    result = []
    for i in images:
        image_id = int(''.join(list(filter(str.isdigit, i))))
        if image_id not in num_list:
            print(i)
        else:
            idx = num_list.index(image_id)
            res_str = i + ',' + str(class_list[idx]) + ',' + disease_list[idx]
            result.append(res_str)
    with open('27classes.txt', 'w') as file:
        for i in result:
            file.write(i + '\n')
        file.close()


if __name__ == '__main__':
    prepare_txt()
    # data_prepare_all()
    # a , n = SkinDisease27.神经源性肿瘤.value, SkinDisease27.神经源性肿瘤.name
    # excel_path = 'D:/MAD_File/上海_皮肤病/上海_皮肤病/训练组1361例.xlsx'
    # excel_data = pd.read_excel(excel_path)
    # img_list = excel_data.id.tolist()
    # label_list = excel_data.multi_class.tolist()
    # filename = 'hh.txt'
    # with open(filename, 'w') as file:
    #     for i in range(len(img_list)):
    #         a = img_list[i]
    #         b = label_list[i]
    #         file.write(str(a))
    #         file.write(',' + str(b) + '\n')
    # rename_file()




