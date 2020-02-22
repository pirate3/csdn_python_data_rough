'''
使⽤数组直接创建,此时索引为默认索引
使⽤数组创建，显式指定索引
使⽤字典创建
'''

import pandas as pd

# 直接使⽤数组进⾏创建
data = pd.Series([10, 11, 12, 13, 14])
print("完整Series内容是：\n", data)
print("\nSeries的值： \n\n", data.values)
print("\nSeries的索引是： \n", data.index)

# 显式制定索引
data_index = pd.Series([10, 11, 12, 13, 14], index=[1, 2, 3, 4, 5])
print("data_index: \n", data_index)

# 使⽤字典进⾏创建
d = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
d_s = pd.Series(d)
print(d_s)

# 对于字典，可以通过index来显式筛选内容
d = {4: "four", 5: "five", 1: "one", 3: "trhee", 2: "two"}
d_s = pd.Series(d, index=[2, 1, 3])
print(d_s)
