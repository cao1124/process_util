import cv2
import numpy as np


def is_image_file(filename):
    return any(filename.endswith(extension) for extension in ['.png', '.PNG', '.jpg', '.jpeg', '.JPG', '.JPEG', '.bmp',
                                                              '.BMP', '.tiff', '.TIFF'])


def cv_imread(file_path):
    # 可读取图片（路径为中文）
    cv_img = cv2.imdecode(np.fromfile(file_path, dtype=np.uint8), flags=-1)
    # flag = -1,   8位深度，原通道
    # flag = 0，   8位深度，1通道
    # flag = 1，   8位深度，3通道
    # flag = 2，   原深度， 1通道
    # flag = 3，   原深度， 3通道
    # flag = 4，   8位深度，3通道
    return cv_img


def cv_write(file_path, file):
    cv2.imencode('.bmp', file)[1].tofile(file_path)