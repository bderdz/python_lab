import numpy as np
import matplotlib.pyplot as plt

SIZE = (100, 100)
IMSHOW_ARGS = {'cmap': 'gray', 'vmin': 0, 'vmax': 255}


def ex1():
    array_1d = np.array([1, 2, 3, 4, 5], dtype=np.uint32)
    array_2d = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

    print(f'array_1d:\n {array_1d}\n shape: {array_1d.shape}\n dtype: {array_1d.dtype}\n')
    print(f'array_2d:\n {array_2d}\n shape: {array_2d.shape}\n dtype: {array_2d.dtype}\n')


def ex2():
    img = np.zeros((100, 100), dtype=np.uint8)
    img[50, 50] = 255
    plt.imshow(img, cmap='gray')
    plt.show()


def ex3():
    img = np.random.randint(0, 256, size=SIZE)
    plt.imshow(img, cmap='gray')
    plt.show()


def ex4(show=False):
    img_uniform = np.random.randint(0, 256, size=SIZE, dtype=np.uint8)
    img_normal = np.random.normal(loc=127, scale=1, size=SIZE)

    if show:
        _, (ax1, ax2) = plt.subplots(1, 2)
        ax1.imshow(img_uniform, cmap='gray')
        ax2.imshow(img_normal, cmap='gray')
        plt.show()

    return img_uniform, img_normal


def ex5(img, brightness, contrast):
    img = np.clip(img.copy().astype(np.float32) * contrast + brightness, 0, 255).astype(np.uint8)
    return img


def ex7(img):
    img = img.copy()
    y = 20
    x = 30
    h = 40
    w = 50
    img[y:y + h, x:x + w] = 255
    return img


def ex8(img):
    img = img.copy()
    img = 255 - img
    return img


def ex9():
    line = np.linspace(0, 255, SIZE[0], dtype=np.uint8)
    img = np.tile(line, (SIZE[1], 1))
    return img


if __name__ == '__main__':
    img, _ = ex4(False)
    img_rect = ex7(img)

    # _, (ax1, ax2) = plt.subplots(1, 2)
    # ax1.imshow(img, **IMSHOW_ARGS)
    # ax2.imshow(ex5(img, 100, 1.2), **IMSHOW_ARGS)
    # ax1.imshow(img_rect, **IMSHOW_ARGS)
    # ax2.imshow(ex8(img_rect), **IMSHOW_ARGS)
    plt.imshow(ex9(), **IMSHOW_ARGS)
    plt.show()
