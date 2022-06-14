import os
import scipy.spatial.distance as dist
import tablib

from resnet_feature import ResnetFeature
from utils.image_utils import is_image_file


def resnet_feature():
    img_path = 'C:/Users/cao/Desktop/image/5485725.jpg'
    detect_obj_dir = 'C:/Users/cao/Desktop/image/result/'

    # load resnet50
    model = ResnetFeature()

    # resnet50模型生成商品原图片向量
    vectors = []
    feature = model.execute(img_path)
    vectors.append(feature)

    # resnet50模型生成目标检测子图片向量
    obj_images = os.listdir(detect_obj_dir)
    obj_images.sort()
    for obj_image in obj_images:
        vector = model.execute(detect_obj_dir + '/' + obj_image)
        vectors.append(vector)
    print('特征数量：', len(vectors))


def similarity_calculate(target_img, query_img_dir):
    dataset = tablib.Dataset()
    dataset.headers = ["target_id"]

    image_filenames = [x for x in os.listdir(query_img_dir) if is_image_file(x)]
    for query_img in image_filenames:
        query_id = int(''.join(list(filter(str.isdigit, query_img))))
        dataset.headers.insert(len(dataset.headers), str(query_id))
    model = ResnetFeature()
    for target_img in image_filenames:
        print('target_img:', target_img)
        target_id = int(''.join(list(filter(str.isdigit, target_img))))
        # 特征抽取网络生成target image向量
        target_feature = model.execute(os.path.join(query_img_dir, target_img))
        res_list = [target_id]
        for query_img in image_filenames:
            # print(query_img)
            # 特征抽取网络生成query image向量
            query_feature = model.execute(os.path.join(query_img_dir, query_img))

            # 向量相似度计算
            # 欧几里德距离   衡量两个向量距离的远近
            # dis = dist.euclidean(query_feature, target_feature)
            # similarity_score = 1 / (1 + dis)

            # 内积距离   夹角余弦[-1,1]衡量两个向量方向的差异  similarity_score = cos(θ)
            dis = dist.cosine(query_feature, target_feature)
            similarity_score = 1 - dis
            res_list.extend([similarity_score])
            # print('similarity_score:', similarity_score)
        dataset.append(res_list)
    with open('similarity_calculate.xlsx', mode='wb') as f:
        f.write(dataset.xlsx)


if __name__ == '__main__':
    target_img = 'merged.tiff'
    query_img_dir = '/home/ai1000/project/skin-disease-classification-by-ride/data/us_label_mask1/'
    similarity_calculate(target_img, query_img_dir)
