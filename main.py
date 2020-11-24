import pandas as pd
import copy
import math


#   相关系数计算
def cor(a, b):
    a_adv = sum(a) / len(a)
    b_adv = sum(b) / len(b)
    # 计算分子，协方差————按照协方差公式
    cov_ab = sum([(x - a_adv) * (y - b_adv) for x, y in zip(a, b)])
    # 计算分母，标准差乘积
    sq = math.sqrt(sum([(x - a_adv) ** 2 for x in a]) * sum([(x - b_adv) ** 2 for x in b]))
    r = cov_ab / sq
    return r


#   导入数据源1
d1 = pd.read_excel('一.数据源1.xlsx')
#   导入数据源2
d2 = pd.read_csv('一.数据源2-逗号间隔.txt', sep=',')
#   统一ID
d1['ID'] = d1['ID'] + 202000

#   数据清洗与处理
#   去重
d1 = d1.drop_duplicates(['ID'])
d2 = d2.drop_duplicates(['ID'])

#   数据合并
d = pd.merge(d1, d2, on='ID', how='outer')  # 外连接
#   数据统一
num = d.shape[0]  # 统计d中学生人数
i = 0
while i < num:
    if str(d['Name_x'][i]) == "nan":
        d.loc[i, 'Name_x'] = d['Name_y'][i]
    if str(d['City_x'][i]) == "nan":
        d.loc[i, 'City_x'] = d['City_y'][i]
    if str(d['Gender_x'][i]) == "nan":
        d.loc[i, 'Gender_x'] = d['Gender_y'][i]
    if str(d['Gender_x'][i]) == "female":
        d.loc[i, 'Gender_x'] = "girl"
    if str(d['Gender_x'][i]) == "male":
        d.loc[i, 'Gender_x'] = "boy"
    if str(d['Height_x'][i]) == "nan":
        d.loc[i, 'Height_x'] = d['Height_y'][i]
    if d['Height_x'][i] < 3:
        d.loc[i, 'Height_x'] = d['Height_x'][i] * 100
    if str(d['C1_x'][i]) == "nan":
        d.loc[i, 'C1_x'] = d['C1_y'][i]
    if str(d['C2_x'][i]) == "nan":
        d.loc[i, 'C2_x'] = d['C2_y'][i]
    if str(d['C3_x'][i]) == "nan":
        d.loc[i, 'C3_x'] = d['C3_y'][i]
    if str(d['C4_x'][i]) == "nan":
        d.loc[i, 'C4_x'] = d['C4_y'][i]
    if str(d['C5_x'][i]) == "nan":
        d.loc[i, 'C5_x'] = d['C5_y'][i]
    if str(d['C6_x'][i]) == "nan":
        d.loc[i, 'C6_x'] = d['C6_y'][i]
    if str(d['C7_x'][i]) == "nan":
        d.loc[i, 'C7_x'] = d['C7_y'][i]
    if str(d['C8_x'][i]) == "nan":
        d.loc[i, 'C8_x'] = d['C8_y'][i]
    if str(d['C9_x'][i]) == "nan":
        d.loc[i, 'C9_x'] = d['C9_y'][i]
    if str(d['C10_x'][i]) == "nan":
        d.loc[i, 'C10_x'] = d['C10_y'][i]
    if str(d['Constitution_x'][i]) == "nan":
        d.loc[i, 'Constitution_x'] = d['Constitution_y'][i]
    i += 1
#   去掉连接后产生的列
d = d.drop(
    ['Name_y', 'City_y', 'Gender_y', 'Height_y', 'C1_y', 'C2_y', 'C3_y', 'C4_y', 'C5_y', 'C6_y', 'C7_y', 'C8_y', 'C9_y',
     'C10_y', 'Constitution_y'], axis=1)
#   替换空值:把d中所有nan值替换为0
d = d.fillna(0)
#   统一成绩
d['C6_x'] = d['C6_x'] * 10
d['C7_x'] = d['C7_x'] * 10
d['C8_x'] = d['C8_x'] * 10
d['C9_x'] = d['C9_x'] * 10
d['C10_x'] = d['C10_x'] * 10
#   变换体能成绩
d.loc[d['Constitution_x'] == "excellent", 'Constitution_x'] = 90.0
d.loc[d['Constitution_x'] == "good", 'Constitution_x'] = 80.0
d.loc[d['Constitution_x'] == "general", 'Constitution_x'] = 70.0
d.loc[d['Constitution_x'] == "bad", 'Constitution_x'] = 60.0

# 1.	学生中家乡在Beijing的所有课程的平均成绩。
i = 0
adv = []  # 存放一个学生的平均成绩
stus = []  # 存放学生
while i < num:
    if str(d['City_x'][i]) == "Beijing":
        adv.append(d['ID'][i])
        adv.append(d['Name_x'][i])
        sum1 = (d['C1_x'][i] + d['C2_x'][i] + d['C3_x'][i] + d['C4_x'][i] + d['C5_x'][i] + d['C6_x'][i] + d['C7_x'][i] +
                d['C8_x'][i] + d['C9_x'][i] + (d['C10_x'][i])) / 10
        adv.append(sum1)
        a = copy.deepcopy(adv)
        stus.append(a)
        adv.clear()
    i += 1
print("学生中家乡在Beijing的所有课程的平均成绩如下")
print("{}\t\t{}\t\t{}".format("id", "name", "adv"))
for stu in stus:
    print("%-8s%-12s%s" %(stu[0], stu[1], stu[2]))
print("-" * 30)

# 2.	学生中家乡在广州，课程1在80分以上，且课程9在9分以上的男同学的数量。
i = 0
k = 0
while i < num:
    if str(d['City_x'][i]) == "Guangzhou" and d['C1_x'][i] >= 80 and d['C9_x'][i] >= 90 and str(
            d['Gender_x'][i]) == "boy":
        k += 1
    i += 1
print("学生中家乡在广州，课程1在80分以上，且课程9在9分以上的男同学的数量为：%d" % k)
print("-" * 30)

# 3.	比较广州和上海两地女生的平均体能测试成绩，哪个地区的更强些？
i = 0
k1 = 0
k2 = 0
adv2 = 0
adv1 = 0
while i < num:
    if str(d['City_x'][i]) == "Guangzhou" and str(d['Gender_x'][i]) == "girl":
        k1 += 1
        adv1 += d['Constitution_x'][i]
    if str(d['City_x'][i]) == "Shanghai" and str(d['Gender_x'][i]) == "girl":
        k2 += 1
        adv2 += d['Constitution_x'][i]
    i += 1
adv1 = adv1 / k1
adv2 = adv2 / k2
print("比较广州和上海两地女生的平均体能测试成绩，哪个地区的更强些")
print("广州女生的平均体能测试成绩：%.2f" % adv1)
print("上海女生的平均体能测试成绩：%.2f" % adv2)
if adv1 > adv2:
    print("结论：广州地区女生强")
elif adv1 < adv2:
    print("结论：上海地区女生强")
else:
    print("广州 上海两地的女生一样强")
print("-" * 30)

# 4.	学习成绩和体能测试成绩，两者的相关性是多少？
r = []
y_constitution = []
i = 0
while i < num:   # 体能成绩
    y_constitution.append(d['Constitution_x'][i])
    i += 1
for k in range(1, 10):    # 9门成绩
    x_score = d['C%d_x' % k].values
    #   计算9个相关性
    r.append(cor(x_score, y_constitution))
for k in range(0, 9):
    print("成绩C%d和体能测试成绩，两者的相关性是: %f" % (k+1, r[k]))
