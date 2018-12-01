# coding=utf-8
import cv2
import numpy as np
import random


def main():
    img = 'ori.png'
    wm = 'watermark.png'
    res = 'result.png'
    p = 1
    encode(img, wm, res, p)


def encode(ori_path, wmk_path, res_path, p):
    # 读取原始图像
    ori_img = cv2.imread(ori_path)
    # 快速傅里叶变换得到频谱图
    ori_f = np.fft.fft2(ori_img)
    # 获取尺寸信息
    height, width, channel = np.shape(ori_img)
    # 读取水印图像
    wmk_img = cv2.imread(wmk_path)
    wmk_height, wmk_width = wmk_img.shape[0], wmk_img.shape[1]

    x, y = list(range(int(height / 2))), list(range(int(width)))

    random.seed(height + width)
    random.shuffle(x)
    random.shuffle(y)
    d_wmk = np.zeros(ori_img.shape)
    # 生成数字水印
    for i in range(int(height / 2)):
        for j in range(int(width)):
            if x[i] < wmk_height and y[j] < wmk_width:
                d_wmk[i][j] = wmk_img[x[i]][y[j]]
                d_wmk[height - 1 - i][width - 1 - j] = d_wmk[i][j]
    # 将数字水印附加到频率域
    res_f = ori_f + p * d_wmk
    res = np.fft.ifft2(res_f)
    res = np.real(res)
    # 保存添加数字水印后的图像
    cv2.imwrite(res_path, res, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])


if __name__ == '__main__':
    main()
