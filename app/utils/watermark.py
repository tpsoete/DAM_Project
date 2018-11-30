from PIL import Image
import numpy as np


def wm_mix(pix, mark):
    pix |= 1
    if mark < 128:
        pix -= 1
    return pix


def add_watermark(src, src_wm, dst):
    im_origin = Image.open(src)
    im_wm = Image.open(src_wm)
    w = min(im_origin.width, im_wm.width)
    h = min(im_origin.height, im_wm.height)

    im = np.array(im_origin)
    wm = np.array(im_wm)

    for i in range(h):
        for j in range(w):
            for k in range(3):
                im[i][j][k] = wm_mix(im[i][j][k], wm[i][j][k])

    im_mixed = Image.fromarray(im)
    im_mixed.save(dst)


def get_watermark(src, dst, width=None, height=None):
    im = np.array(Image.open(src))
    # print(im.shape)
    if width is None:
        width = im.shape[1]
    if height is None:
        height = im.shape[0]
    wm = np.zeros((height, width, 3), dtype=np.uint8)

    for i in range(height):
        for j in range(width):
            for k in range(3):
                wm[i][j][k] = np.uint8(-(im[i][j][k] & 1))

    im_get = Image.fromarray(wm)
    im_get.save(dst)


if __name__ == '__main__':
    print(np.array([1, 2]))
