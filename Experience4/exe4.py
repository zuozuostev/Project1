# -*- coding = utf-8 -*-
# @Time: 23:45
# @Author:LEE
# @Software:PyCharm

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# 导入逻辑回归模型函数库
from sklearn.linear_model import LogisticRegression


def sigmoid(z):
    phi_z = 1.0 / (1.0 + np.exp(-z))
    return phi_z


def plt_sigmoid(data, w):
    # 其拟合方程形式为f(x)=w0+w1*x1+w2*x2....
    # 生成两个矩阵
    data = np.mat(data)
    w = np.array(w)
    z = data * np.transpose(w)  # 矩阵转置，相乘后得到z值
    z.sort(axis=0)

    # 画sigmoid函数
    phi_z = sigmoid(z)
    plt.plot(z, phi_z)
    plt.axvline(0.0, color='k')
    plt.axhspan(0.0, 1.0, facecolor='1.0', alpha=1.0, ls='dotted')
    plt.yticks([0.0, 0.5, 1.0])
    plt.ylim(-0.1, 1.1)
    plt.xlabel('z')
    plt.ylabel('$\phi (z)$')
    plt.show()


# 训练效果可视化
def train_plt(data, label, lr_clf):
    plt.figure()
    plt.scatter(data[:, 0], data[:, 1], s=50, c=label, cmap='viridis')
    # 可视化决策边界
    nx, ny = 200, 100
    x_min, x_max = plt.xlim()
    y_min, y_max = plt.ylim()
    x_grid, y_grid = np.meshgrid(np.linspace(x_min, x_max, nx), np.linspace(y_min, y_max, ny))
    z_proba = lr_clf.predict_proba(np.c_[x_grid.ravel(), y_grid.ravel()])
    z_proba = z_proba[:, 1].reshape(x_grid.shape)

    plt.contour(x_grid, y_grid, z_proba, [0.5], colors='blue', linewidths=3)
    plt.show()


# 可视化预测新样本
def test_plt(data, label, lr_clf):
    plt.figure()
    print("请输入要预测点的坐标：")
    x = int(input("x="))
    y = int(input("y="))
    new_point1 = np.array([[x, y]])
    plt.scatter(new_point1[:, 0], new_point1[:, 1], cmap='viridis', s=50)
    plt.annotate(s='the new point 1', xy=(0, -1), xytext=(-2, 0), color='blue',
                 arrowprops=dict(arrowstyle='-|>', connectionstyle='arc3', color='red'))
    plt.scatter(data[:, 0], data[:, 1], s=50, c=label, cmap='viridis')
    plt.title('Dataset')

    # 可视化决策边界
    nx, ny = 200, 100
    x_min, x_max = plt.xlim()
    y_min, y_max = plt.ylim()
    x_grid, y_grid = np.meshgrid(np.linspace(x_min, x_max, nx), np.linspace(y_min, y_max, ny))
    z_proba = lr_clf.predict_proba(np.c_[x_grid.ravel(), y_grid.ravel()])
    z_proba = z_proba[:, 1].reshape(x_grid.shape)
    plt.contour(x_grid, y_grid, z_proba, [0.5], colors='blue', linewidths=3)
    plt.show()


def exe4(clusterAssment):
    # 构造数据集
    df = pd.read_table("teacher_data.txt", header=None, sep='\t')
    df.columns = ['x', 'y']
    data = df.values.tolist()  # 把dataframe数据转变为list类型
    data = np.array(data)
    # 给数据源打标签
    label = []
    for i in range(len(clusterAssment)):
        label.append(clusterAssment[i][0])
    label = np.array(label)

    # 调用逻辑回归模型，并拟合所构造的数据集
    lr_clf = LogisticRegression()
    lr_clf = lr_clf.fit(data, label)  # 其拟合方程形式为f(x)=w0+w1*x1+w2*x2

    # 学习并画出sigmoid函数
    w = lr_clf.coef_  # 使用coef_ 查看对应模型的系数w
    plt_sigmoid(data, w)

    # 可视化模型
    train_plt(data, label, lr_clf)

    # 用学习好的模型对(2,6)分类。
    # 可视化预测点
    test_plt(data, label, lr_clf)
