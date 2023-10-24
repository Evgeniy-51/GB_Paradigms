import numpy as np


def pearson_corr_coeff(x, y):
    XY = np.vstack([x, y])
    return np.corrcoef(XY)


if __name__ == '__main__':
    x = np.array([32, 6, 87, 2, 89, 4, 2, 6, 7, 5])
    y = np.array([34, 5, 76, 3, 8, 3, 0, 2, 45, 66])
    print(pearson_corr_coeff(x, y))
