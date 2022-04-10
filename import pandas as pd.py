from pickle import TRUE
from xml.dom import WRONG_DOCUMENT_ERR
import pandas as pd
import numpy as np
from pyparsing import col

courses = ["语文","数学","英语"]#list
data = pd.Series(data=courses)
print(data)#list->series
print("----------------------")

grades = {"语文":80,"数学":90,"英语":85}#dict
data = pd.Series(data=grades)
print(data)#dict->series
print("----------------------")


# Series2list
numbers = data.tolist()
print(numbers)#series->list
print("----------------------")

# Series2dataframe
df = pd.DataFrame(data,columns=['grade'])
print(df)#series->dataframe
print("----------------------")

# 用Numpy创建Series
s = pd.Series(
    # 数值：10~90，间隔10
    np.arange(10,91,10),
    # 索引：101~109
    index=np.arange(101,110),
    # 类型：float64 
    dtype="float"
)
print(s)
print("----------------------")

# string series -> int series 
s = pd.Series(
    data= ['001','002','003','004'],
    index=list('abcd')
)
#  两种方法
s = s.astype('int') 
s = s.map(int)
print(s)
print("----------------------")

# 给Series添加元素
data = data.append(pd.Series({
    '物理':100,
    "化学":90
}))
print(data)
print("----------------------")


# Series转换成DataFrame
df = data.reset_index()
df.columns = ['courses','grade']
print(df)
print("----------------------")


# 创建一个DataFrame
df = pd.DataFrame({
    "姓名":["小张","小王","小李","小赵"],
    "性别":["男","女","男","女"],
    "年龄":[18,19,20,21]})
print(df)#创建 dataframe 
print("----------------------")


# 设置DataFrame的索引列
df.set_index('姓名',inplace = True)
print(df)



# 生成一个月份所有天
date_range = pd.date_range(start='2022-01-01',end='2022-01-31')
date_range = pd.date_range(start='2022-01-01',periods=31)
print(date_range)
print("----------------------")

# 012 生成一年的所有周一
data_range = pd.date_range(start = '2021-01-01',
    end='2021-12-31',
    freq='W-MON')
data_range = pd.date_range(start = '2021-01-01',
    periods=52,freq='W-MON')
print(data_range)

# 013 生成一天的所有小时
date_range = pd.date_range(start='2022-01-01',periods = 24,freq = 'H')
date_range = pd.date_range(start='2022-01-01',end='2022-01-02',freq='H',closed='left')
print(date_range)

# 014 生成日期DateFrame
date_range = pd.date_range(start='2022-01-01',periods = 31)
df = pd.DataFrame(data = date_range,columns =['day'])
df['day_of_year'] = df['day'].dt.dayofyear
print(df)

#015 使用日期和随机数生成DataFrame
date_range = pd.date_range(start='2022-01-01',periods = 1000)
data = {
    'norm':np.random.normal(loc=0,scale=1,size=1000),
    'uniform':np.random.uniform(low=0,high=1,size=1000),
    'binomial':np.random.binomial(n=1,p=0.2,size=1000)
}
df = pd.DataFrame(data = data,index=date_range)
print(df)

# 016 打印DataFrame的前后5行
print(df.head(10)) #打印前10行
print() # 空行
print(df.tail(5))

# 017 查看df的信息和基本数据统计
print(df.info())
print(df.describe())

# 018 统计数据列的值出现次数
print(df['binomial'].value_counts())


# 019 df前N行存入CSV文件
date_range = pd.DataFrame(
    data = {"norm":np.random.normal(loc=0,scale=1,size=1000),
            "uniform":np.random.uniform(low=0,high=1,size=1000),
            "binomial":np.random.binomial(n=1,p=0.2,size=1000)},
            index = pd.date_range(start='2022-01-01',periods=1000))
df.head(100).to_csv('./分布数据前100.csv')#df前N行存入csv文件
print("----------------------")

# 020 加载CSV文件到df
df = pd.read_csv('./分布数据前100.csv',index_col = 0)
print(df.info())
print(df.head())

# 021 加载股票数据CSV文件
df = pd.read_csv("./data/00700.HK.csv",index_col=0)
print(df)



# 比较两列平均值的大小
print(df['Close'].mean() > df['Open'].mean())
