import pandas as pd
import exe1
import exe2
import exe3
import exe4
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

#   实验1
exe1.show_exe1(d,num)

#  实验2
# 1. 请以课程1成绩为x轴，体能成绩为y轴，画出散点图。
print("1.散点图如下：")
exe2.draw_scatter(d)
print("-" * 30)

# 2. 以5分为间隔，画出课程1的成绩直方图。
print("2.直方图如下：")
exe2.draw_hist(d)
print("-" * 30)

# 3. 对每门成绩进行z-score归一化，得到归一化的数据矩阵。
print("3.每门成绩归一化的矩阵如下：")
z_d = exe2.z_score(d, num)
print(z_d)
print("-" * 30)

# 4. 计算出106x106的相关矩阵，并可视化出混淆矩阵。（为避免歧义，这里“协相关矩阵”进一步细化更正为100x100的相关矩阵，100为学生样本数目，视实际情况而定）
print("4.每个学生的相关矩阵，及其可视化出的混淆矩阵：")
d_stu = exe2.stu_cor(z_d, num)
print(d_stu)
print("-" * 30)

# 5. 根据相关矩阵，找到距样本最离每个近的三个样本，得到100x3的矩阵（每一行为对应三个样本的ID）输出到txt文件中，以\t,\n间隔。
print("5.已保存....")
exe2.find_ID(d, d_stu, num)


# 实验3
clusterAssment = exe3.exe3()

# # 实验4
exe4.exe4(clusterAssment)