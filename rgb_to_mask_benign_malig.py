import cv2
import numpy as np
import os
import shutil
import pandas as pd

from utils.image_utils import is_image_file, cv_imread, cv_write


def make_dir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)


def is_equal_blue(a):
    b = []
    for i in range(3):
        b.append(np.int(a[i]))

    if b[0] >= 250 and b[1] <= 0 and b[2] <= 0:
        return True
    if b[0] > b[1] + b[2] + 30 and b[0] >= 200:
        return True
    # m = 3
    # if b[0] <= 204 + m and b[0] >= 204 - m \
    #         and b[1] <= 72 + m and b[1] >= 72 - m \
    #         and b[2] <= 63 + m and b[2] >= 63 - m:
    #     return True
    return False


def is_equal_green(a):
    b = []
    for i in range(3):
        b.append(np.int(a[i]))
    # if b[0] <= 60 and b[1] >= 170 and b[2] <= 60:
    if b[0] <= 50 and b[1] >= 230 and b[2] <= 50:
        return True
    # elif 22 <= b[0] <= 109 and 214 >= b[1] >= 124 and 0 <= b[2] <= 59:
    #     return True

    return False


# BGR  ;malig
def is_equal_red(a):
    b = []
    for i in range(3):
        b.append(np.int(a[i]))
    # if b[0] <= 14 and b[1] <= 12 and b[2] >= 230:
    #     return True
    # elif 0 <= b[0] <= 107 and 19 <= b[1] <= 83 and b[2] >= 116:
    #     return True
    if b[0] <= 30 and b[1] <= 30 and b[2] >= 200:
        return True
    return False


# BGR
def is_equal_yellow(a):
    b = []
    for i in range(3):
        b.append(int(a[i]))
    if b[0] <= 150 and b[1] >= 210 and b[2] >= 210:
        return True
    return False


def is_equal_pink(a):  # 粉色：不确定结节
    b = []
    for i in range(3):
        b.append(np.int(a[i]))
    if b[0] >= 240 and b[1] <= 30 and b[2] >= 210:
        return True
    return False


def is_equal_purple(a):  # 紫色:淋巴结
    b = []
    for i in range(3):
        b.append(np.int(a[i]))
    if 123 <= b[0] <= 135 and b[1] <= 5 and 123 <= b[2] <= 135:
        return True
    return False


def draw_mask(mark):
    # remove_small_objects( mark, min_size=35, connectivity=2, in_place=True)
    # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    # mark = cv2.morphologyEx(mark, cv2.MORPH_CLOSE, kernel, iterations=2)
    cnts, hier = cv2.findContours(
        mark, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # for i in range(len(cnts)):
    #     area = cv2.contourArea(cnts[i])
    #     if area > 10:
    #         cv2.drawContours(mark, cnts[i], -1, 255, thickness=-1)
    cv2.drawContours(mark, cnts, -1, 255, thickness=-1)

    return [mark, len(cnts)]


def extract_marks(mark):
    [h, w, _] = mark.shape
    # h =576 , w = 704 ;
    mark_combine = np.zeros((h, w), dtype=np.uint8)
    # mark_combine.shape = (576, 704)  ;
    mark_yellow = np.zeros((h, w), dtype=np.uint8)
    mark_green = np.zeros((h, w), dtype=np.uint8)
    mark_red = np.zeros((h, w), dtype=np.uint8)
    mark_blue = np.zeros((h, w), dtype=np.uint8)
    mark_pink = np.zeros((h, w), dtype=np.uint8)
    mark_purple = np.zeros((h, w), dtype=np.uint8)
    for ii in range(h):
        for jj in range(w):
            # # 良性
            # if is_equal_green(mark[ii, jj]):
            #     mark_green[ii, jj] = 255
            #
            # # 恶性
            # if is_equal_red(mark[ii, jj]):
            #     mark_red[ii, jj] = 255

            if is_equal_yellow(mark[ii, jj]):
                mark_yellow[ii, jj] = 255

            # elif is_equal_blue(mark[ii, jj]):
            #     mark_blue[ii, jj] = 255
            # elif is_equal_pink(mark[ii, jj]):
            #     mark_pink[ii, jj] = 255
            # elif is_equal_purple(mark[ii, jj]):
            #     mark_purple[ii, jj] = 255

    # [mark_green, count_green] = draw_mask(mark_green)
    # [mark_red, count_red] = draw_mask(mark_red)
    [mark_yellow, count_yellow] = draw_mask(mark_yellow)
    # [mark_blue, count_blue] = draw_mask(mark_blue)
    # [mark_pink, count_pink] = draw_mask(mark_pink)
    # [mark_purple, count_purple] = draw_mask(mark_purple)

    # mark_combine[mark_green == 255] = 192  # 绿色
    # mark_combine[mark_red == 255] = 220  # 红色
    mark_combine[mark_yellow == 255] = 128  # 黄色
    # mark_combine[mark_blue == 255] = 150  # 蓝色
    # mark_combine[mark_pink == 255] = 110  # 粉色
    # mark_combine[mark_purple == 255] = 80  # 紫色

    # return [mark_combine, count_red, count_green, count_yellow, count_blue, count_pink, count_purple]
    return [mark_combine, count_yellow]


def mask2txt():
    # mask_path = './VOC_上海10院/上海10院_crop/超声窗口mask_crop/'
    # save_txt = './VOC_上海10院/上海10院_crop/超声窗口mask_txt/'
    # mask_path = '../整理后乳腺3D/2D/mask/'
    # save_txt = '../整理后乳腺3D/2D/mask2txt/'

    mask_path = 'D:/MAD_File/上海_皮肤病/上海_皮肤病/us_label/'
    save_path = './从新标注后的数据/新增数据/3d/3d_mask2txt/'
    for cla in ['benign', 'malig']:
        new_save_txt = os.path.join(save_path, cla)
        # mk_dir(new_save_txt)

        imgs_path = os.path.join(mask_path, cla)
        img_list = os.listdir(imgs_path)
        for idx, img_name in enumerate(img_list):
            count = 0
            im_path = os.path.join(imgs_path, img_name)

            img_gray = cv2.imread(im_path, 0)

            thresh = cv2.threshold(
                img_gray, 170, 255, cv2.THRESH_BINARY)[1]  # 180

            # 结节轮廓
            conts = cv2.findContours(
                thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]  # cv2.CHAIN_APPROX_NONE
            # print(len(conts))
            for j, cnts in enumerate(conts):

                # 找到边界坐标
                x, y, w, h = cv2.boundingRect(cnts)  # 计算点集最外面的矩形边界
                # cv2.rectangle(img, (x, y), (x + w, y + h), colors[j], 3)
                if w * h > 25:
                    count += 1
                    # if j >= 1:
                    #     print(img_name)
                    if cla == 'benign':
                        txt_list = [str(0), str(x), str(y), str(w), str(h)]
                    elif cla == 'malig':
                        txt_list = [str(1), str(x), str(y), str(w), str(h)]
                    txt_content = ' '.join(txt_list)

                    # print(txt_content)
                    dst_path = os.path.join(new_save_txt, img_name[:-4]+'.txt')
                    # ------------写入txt-------------
                    with open(dst_path, 'a') as f:
                        f.write(txt_content+'\n')
                    # ------------写入txt-------------
                    # ----------显示结节外接矩形框------------
                    # cv2.rectangle(img_gray, (x, y),
                    #               (x + w, y + h), (255, 255, 255), 4)
                    # img_show('mask_img', img_gray)
                    # ----------显示结节外接矩形框------------
            if count >= 2:
                print("{}  有{}个符合条件的结节".format(img_name, count))
            elif count < 1:
                print("{}  未找到符合条件的结节".format(img_name))


def get_pixel_RGB_HSV():
    image = cv_imread("D:/MAD_File/上海_皮肤病/上海_皮肤病/photo_label/D75465-全（右颞部）：皮肤鳞状细胞癌。.jpg")
    image_res = cv2.resize(image, (640, 640))
    HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    def getpos(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:  # 定义一个鼠标左键按下去的事件
            print(HSV[y, x])
    # cv2.namedWindow("imageHSV", cv2.WINDOW_FREERATIO)

    cv2.namedWindow("image", cv2.WINDOW_FREERATIO)
    # cv2.imshow("imageHSV", HSV)
    cv2.imshow("image", image_res)
    cv2.setMouseCallback("image", getpos)
    cv2.waitKey(0)


def show_image():
    lift_dir = "D:/MAD_File/上海_皮肤病/上海_皮肤病/us_label_crop/"
    right_dir = "D:/MAD_File/上海_皮肤病/上海_皮肤病/us_label_mask/"

    images = [x for x in os.listdir(lift_dir) if is_image_file(x)]
    for img_name in images:
        print(img_name)
        left_img = cv_imread(lift_dir + img_name)
        if os.path.exists(right_dir + img_name):
            right_img = cv_imread(right_dir + img_name)

            img1 = cv2.resize(left_img, (640, 640))
            img2 = cv2.resize(right_img, (640, 640))

            new_img = np.hstack([img1, img2])
            cv2.imshow('new_img', new_img)
            cv2.waitKey(0)


def change_endwith():
    dir = "D:/MAD_File/上海_皮肤病/上海_皮肤病/us_label_mask/"
    out_dir = "D:/MAD_File/上海_皮肤病/上海_皮肤病/us_label_mask1/"
    images = [x for x in os.listdir(dir) if is_image_file(x)]
    for img_name in images:
        print(img_name)
        img = cv_imread(dir + img_name)

        if img_name.endswith('jpg'):
            new_path = out_dir + img_name
        else:
            if img_name.endswith('tiff'):
                new_path = out_dir + img_name.split('.tiff')[0] + '.jpg'
            elif img_name.endswith('.png'):
                new_path = out_dir + img_name.split('.png')[0] + '.jpg'
            elif img_name.endswith('.bmp'):
                new_path = out_dir + img_name.split('.bmp')[0] + '.jpg'
            elif img_name.endswith('.jpeg'):
                new_path = out_dir + img_name.split('.jpeg')[0] + '.jpg'
        cv_write(new_path, img)


def cnt_area(cnt):
    """返回轮廓的面积"""
    area = cv2.contourArea(cnt)
    return area


def crop_image_by_hsv():
    '''
        颜色标注说明：
        恶性	                红色	红色255   绿色0	    蓝色0
        良性结节	            绿色	红色0     绿色255   蓝色0
        导管	                黄色	红色255	 绿色255	    蓝色0
        浆乳、肉芽肿、乳汁淤积	蓝色	红色0     绿色0     蓝色255

        不确定	            粉色	红色255   绿色0   蓝色255
        淋巴结	            紫色	红色128   绿色0   蓝色128


        '''
    orig_dir = "D:/MAD_File/上海_皮肤病/上海_皮肤病/photo_img/"
    label_dir = "D:/MAD_File/上海_皮肤病/上海_皮肤病/photo_label/"

    dst_dir = "D:/MAD_File/上海_皮肤病/上海_皮肤病/photo1/"
    make_dir(dst_dir)

    images = [x for x in os.listdir(orig_dir) if is_image_file(x)]
    print(len(images))

    # 无结节
    no_node_count = 0
    count_green, count_red, count_yellow, count_blue, count_pink, count_purple = 0, 0, 0, 0, 0, 0

    for img_name in images:
        print(img_name)
        # img = cv2.imread(orig_img_dir + name, cv2.IMREAD_COLOR)
        ori_img = cv_imread(orig_dir + img_name)
        if os.path.exists(label_dir + img_name):
            label_img = cv_imread(label_dir + img_name)
        else:
            if img_name.endswith('.jpeg'):
                label_img = cv_imread(label_dir + img_name.split('.jpeg')[0] + '.jpg')

        # 设定颜色HSV范围，假定为红色
        # redLower = np.array([156, 43, 46])
        # redUpper = np.array([179, 255, 255])
        yellowLower = np.array([10, 100, 100])    # [26, 43, 46]
        yellowUpper = np.array([34, 255, 255])
        hsv = cv2.cvtColor(label_img, cv2.COLOR_BGR2HSV)
        # 去除颜色范围外的其余颜色
        mask = cv2.inRange(hsv, yellowLower, yellowUpper)
        # 二值化操作
        ret, binary = cv2.threshold(mask, 0, 255, cv2.THRESH_BINARY)

        # 膨胀操作，因为是对线条进行提取定位，所以腐蚀可能会造成更大间隔的断点，将线条切断，因此仅做膨胀操作
        kernel = np.ones((5, 5), np.uint8)
        dilation = cv2.dilate(binary, kernel, iterations=1)

        # 获取图像轮廓坐标，其中contours为坐标值，此处只检测外形轮廓
        contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if len(contours) > 0:
            area = []
            # 找到最大的轮廓
            for k in range(len(contours)):
                area.append(cv2.contourArea(contours[k]))
            max_idx = np.argmax(np.array(area))
            max_area = contours[max_idx]
            x, y, w, h = cv2.boundingRect(contours[max_idx])
            crop_img = ori_img[y:y + h, x:x + w]

            # img1 = cv2.resize(label_img, (640, 640))
            # img2 = cv2.resize(crop_img, (640, 640))
            # new_img = np.hstack([img1, img2])
            # cv2.imshow(img_name, new_img)
            # cv2.waitKey(0)

            cv_write(dst_dir + img_name, crop_img)

            # cv2.boundingRect()返回轮廓矩阵的坐标值，四个值为x, y, w, h， 其中x, y为左上角坐标，w,h为矩阵的宽和高
            # boxes = [cv2.boundingRect(c) for c in contours[0]]
            # for box in boxes:
            #     x, y, w, h = box
            #     if h > 50 and w > 50:
            #         # 绘制矩形框对轮廓进行定位
            #         cv2.rectangle(ori_img, (x, y), (x + w, y + h), (153, 153, 0), 2)
            #         # 将绘制的图像保存并展示
            #         crop_img = ori_img[y:y + h, x:x + w]
            #
            #         img1 = cv2.resize(ori_img, (640, 640))
            #         img2 = cv2.resize(crop_img, (640, 640))
            #         new_img = np.hstack([img1, img2])
            #         cv2.imshow(img_name, new_img)
            #         cv2.waitKey(0)
            #
            #         cv_write(dst_dir + img_name, crop_img)
    #     # [mark_combine, c_red, c_green, c_yellow, c_blue,
    #     #     c_pink, c_purple] = extract_marks(mark)
    #     [mark_combine,  c_yellow] = extract_marks(img)
    #
    #     # count_green += c_green
    #     # count_red += c_red
    #     count_yellow += c_yellow
    #     # count_blue += c_blue
    #     # count_pink += c_pink
    #     # count_purple += c_purple
    #
    #     # if count_red == 1 and count_green == 0:
    #     #     print('malig:',img_name)
    #     # if count_red == 0 and count_green == 1:
    #     #     print('benign:',img_name)
    #
    #     # print(mark_combine.shape)
    #
    #     # plt.imshow(mark_combine)
    #     # plt.show()
    #     cv_show('mask', mark_combine)
    #     cv2.waitKey(255)
    #     print(img_name, c_yellow)
    #     cv_write(dst_dir + img_name, mark_combine)
    #     # if c_green == 0 and c_red == 0:
    #     #     no_node_count += 1
    #
    # print('良性：{}，恶性：{}，导管：{}，浆乳_肉芽肿:{}，不确定：{}，淋巴结：{},无结节:{}'.format(
    #     count_green, count_red, count_yellow, count_blue, count_pink, count_purple,no_node_count))


def get_csv_file():
    ori_dir = 'D:/MAD_File/上海_皮肤病/上海_皮肤病/ori/补90（us+外观）/补90（us+外观）'
    file_name_list = os.listdir(ori_dir)
    i = 0
    for file in file_name_list:
        csv_file = os.path.join(ori_dir, file, '外观.csv')
        if os.path.exists(csv_file):
            out_dir = 'D:/MAD_File/上海_皮肤病/上海_皮肤病/ori/csv_file/' + file + '.csv'
            shutil.copy(csv_file, out_dir)
            i += 1
    print(i)


def make_photo_mask():
    # a = os.path.exists('D:/MAD_File/上海_皮肤病/上海_皮肤病/photo_img/D46461 全 肢端黏液样囊肿.jpg')
    csv_list = os.listdir('D:/MAD_File/上海_皮肤病/上海_皮肤病/photo_csv_file/')
    for csv_file in csv_list:
        print(csv_file)
        image_path = 'D:/MAD_File/上海_皮肤病/上海_皮肤病/photo_img/' + csv_file.split('.csv')[0] + '.jpg'
        if os.path.exists(image_path):
            image = cv_imread(image_path)
        else:
            image_path = 'D:/MAD_File/上海_皮肤病/上海_皮肤病/photo_img/' + csv_file.split('.csv')[0] + '.jpeg'
            if os.path.exists(image_path):
                image = cv_imread(image_path)
            else:
                image_path = 'D:/MAD_File/上海_皮肤病/上海_皮肤病/photo_img/' + csv_file.split('.csv')[0] + ' .jpg'
                if os.path.exists(image_path):
                    image = cv_imread(image_path)
                else:
                    image_path = 'D:/MAD_File/上海_皮肤病/上海_皮肤病/photo_img/' + csv_file.split('.csv')[0] + ' .jpeg'
                    image = cv_imread(image_path)
        # img1 = cv2.resize(image, (640, 640))
        # cv2.imshow('img1', img1)

        csv_data = pd.read_csv('D:/MAD_File/上海_皮肤病/上海_皮肤病/photo_csv_file/' + csv_file,
                               header=None, names=['X', 'Y', 'Red', 'Green', 'Blue'])
        x_list = csv_data.X.tolist()
        y_list = csv_data.Y.tolist()
        mask_image = np.zeros(image.shape)
        for i in range(1, len(x_list)):
            mask_image[int(y_list[i]), int(x_list[i])] = 255
        out_path = 'D:/MAD_File/上海_皮肤病/上海_皮肤病/photo_mask/' + csv_file.split('.csv')[0] + '.jpg'
        print(out_path)
        cv_write(out_path, mask_image)
        # img2 = cv2.resize(mask_image, (640, 640))
        # cv2.imshow('mask', img2)
        # cv2.waitKey(200)


def crop_by_mask():
    orig_dir = "D:/MAD_File/上海_皮肤病/上海_皮肤病/photo_img/"
    mask_dir = "D:/MAD_File/上海_皮肤病/上海_皮肤病/photo_mask/"

    dst_dir = "D:/MAD_File/上海_皮肤病/上海_皮肤病/photo_img_crop/"
    make_dir(dst_dir)

    images = [x for x in os.listdir(mask_dir) if is_image_file(x)]
    print(len(images))

    for img_name in images:
        mask_img = cv_imread(mask_dir + img_name)
        if os.path.exists(orig_dir + img_name):
            ori_img = cv_imread(orig_dir + img_name)
        elif os.path.exists(orig_dir + img_name.split('.jpg')[0] + '.jpeg'):
            ori_img = cv_imread(orig_dir + img_name.split('.jpg')[0] + '.jpeg')
        else:
            print(img_name)

        # 二值化操作
        gray = cv2.cvtColor(mask_img, cv2.COLOR_BGR2GRAY)
        ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)
        # 获取图像轮廓坐标，其中contours为坐标值，此处只检测外形轮廓
        contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if len(contours) > 0:
            area = []
            # 找到最大的轮廓
            for k in range(len(contours)):
                area.append(cv2.contourArea(contours[k]))
            max_idx = np.argmax(np.array(area))
            x, y, w, h = cv2.boundingRect(contours[max_idx])
            crop_img = ori_img[y:y + h, x:x + w]
            # img1 = cv2.resize(ori_img, (640, 640))
            # img2 = cv2.resize(crop_img, (640, 640))
            # new_img = np.hstack([img1, img2])
            # cv2.imshow('crop', new_img)
            # cv2.waitKey(200)
            cv_write(dst_dir + img_name, crop_img)


def merge_us_rgb():
    rgb_dir = "D:/MAD_File/上海_皮肤病/上海_皮肤病/photo_img_crop/"
    us_dir = "D:/MAD_File/上海_皮肤病/上海_皮肤病/us_label_mask"
    images = [x for x in os.listdir(rgb_dir) if is_image_file(x)]
    print(len(images))

    for img_name in images:
        print(img_name)
        if os.path.exists(us_dir + img_name):
            us_img_path = us_dir + img_name
        elif os.path.exists(us_dir + img_name.split('.jpg')[0] + '.bmp'):
            us_img_path = us_dir + img_name.split('.jpg')[0] + '.bmp'
        elif os.path.exists(us_dir + img_name.split('.jpg')[0] + '.png'):
            us_img_path = us_dir + img_name.split('.jpg')[0] + '.png'
        elif os.path.exists(us_dir + img_name.split('.jpg')[0] + '.tiff'):
            us_img_path = us_dir + img_name.split('.jpg')[0] + '.tiff'

        if us_img_path:
            im1 = cv_imread(rgb_dir + img_name)
            im2 = cv_imread(us_img_path)
            merged = np.concatenate((im1, im2), axis=2)  # creates a numpy array with 6 channels
            cv2.imwrite('merged.tiff', merged)


if __name__ == '__main__':
    # change_endwith()
    # show_image()
    # get_pixel_RGB_HSV()
    # get_csv_file()
    # crop_image_by_hsv()
    # make_photo_mask()
    # crop_by_mask()
    merge_us_rgb()

