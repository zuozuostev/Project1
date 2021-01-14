# -*- coding = utf-8 -*-
# @Time: 14:03
# @Author:LEE
# @Software:PyCharm
import matplotlib.pyplot as plt  # 导入模块 matplotlib.pyplot，并简写成 plt
import math
import copy
import pandas as pd
import exe1         # 导入实验1，主要是相关系数计算的函数
import heapq     # 处理列表
import seaborn as sn    # 混淆矩阵模块


# 画散点图
def draw_scatter(d):
    plt.xlabel("x_C1")      # 定义x坐标
    plt.ylabel("y_Con")     # 定义y坐标
    plt.scatter(d['C1_x'].values, d['Constitution_x'].values)       # 传入数据
    plt.show()


# 画直方图
def draw_hist(d):
    plt.xlabel("x")         # 定义x坐标
    plt.ylabel("y")         # 定义y坐标

    # 固定5为间隔
    a = (max(d['C1_x'].values) - min(d['C1_x'].values)) / 5
    if 5 - a > 0:
        plt.hist(d['C1_x'].values, bins=int(a) + 1)
    else:
        plt.hist(d['C1_x'].values, bins=int(a))
    plt.show()


# 数据归一化
def z_score(d, num):
    z_d = {}
    c = []
    i = 0
    # 十成绩归一化
    for k in range(1, 11):
        u = sum(d['C%d_x' % k].values) / len(d['C%d_x' % k].values)  # 计算平均值
        a = math.sqrt(sum([(x - u) ** 2 for x in d['C%d_x' % k].values]) / len(d['C%d_x' % k].values))
        for x in d['C%d_x' % k].values:
            z_x = (x - u) / a     # 归一化公式
            c.append(z_x)
        a = copy.deepcopy(c)
        z_d['C%d' % k] = a
        c.clear()
    # 体能成绩归一化
    u = sum(d['Constitution_x'].values) / len(d['Constitution_x'].values)
    a = math.sqrt(sum([(x - u) ** 2 for x in d['Constitution_x'].values]) / len(d['Constitution_x'].values))
    for x in d['Constitution_x'].values:
        z_x = (x - u) / a
        c.append(z_x)
    a = copy.deepcopy(c)
    z_d['Constitution'] = a
    # 构成归一化的数据矩阵
    z_d = pd.DataFrame(z_d)
    z_d = z_d.fillna(0)
    z_d.to_csv('Lee_data.txt', index=False, sep='\t', header=None, encoding='utf_8')
    return z_d


# 4、计算学生的相关矩阵
def stu_cor(z_d, num):
    cor_stus = []  # 所有学生的相关矩阵
    cor_stu = []  # 一个学生与其他学生的相关矩阵
    # 历遍每个学生，每个学生都与其他学生计算一个相关系数值
    for r in range(0, num):
        for c in range(0, num):
            cor_stu.append(exe1.cor(z_d.ix[r].values, z_d.ix[c].values))
        temp = copy.deepcopy(cor_stu)
        cor_stus.append(temp)
        cor_stu.clear()

    # 可视化混淆矩阵
    d_stu = pd.DataFrame(cor_stus)
    d_stu = d_stu.astype(float)     # 把数据转换为float类型
    sn.heatmap(d_stu)
    plt.show()
    return d_stu


# 5. 根据相关矩阵，找到距样本最离每个近的三个样本，得到100x3的矩阵
def find_ID(d, d_stu, num):
    id = []
    ids = []
    for i in range(0,num):
        a = list(d_stu.ix[i].values)
        m= heapq.nlargest(4, a)   # 取四个最大相关系数出来
        for k in range(0,4):
            id.append(a.index(m[k]))  # 找出相关系数对应的序号
        id.pop(0)     # 把1去掉
        t_id=copy.deepcopy(id)
        id.clear()
        ids.append(t_id)
    # print(ids)
    # print(d)
    s_ID=[]
    for i in ids:
        for k in range(0,3):
            id.append(d.at[i[k],'ID'])   # 找id
        t_id = copy.deepcopy(id)
        s_ID.append(t_id)
        id.clear()
    df_ID=pd.DataFrame(s_ID)
    # print(df_ID)
    # 存入文档
    df_ID.to_csv('Lee_ID.txt', index=False, sep='\t',header=None, encoding='utf_8')
