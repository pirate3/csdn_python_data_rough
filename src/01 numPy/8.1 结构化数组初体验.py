# 定义⼀个学⽣信息数组，包括姓名，成绩，身⾼
import numpy as np

x = np.zeros(4, dtype={"names": ("name", "score", "heigh"), \
                       "formats": ("U10", "i4", "f8")})
print("x = ", x)
print("x.dtype = ", x.dtype)

'''
x =  [('', 0, 0.) ('', 0, 0.) ('', 0, 0.) ('', 0, 0.)]
x.dtype =  [('name', '<U10'), ('score', '<i4'), ('heigh', '<f8')]
'''

# 可以对某⼀项进⾏统⼀赋值
x['name'] = "LIU Ying"
x['score'] = 98
x['heigh'] = 185
print("统⼀赋值后的x = \n", x)

# 可以采⽤key的形式进⾏访问列
print("学⽣的姓名是： ", x['name'])
# 也可以采⽤索引的形式进⾏访问⾏
print("第⼀⾏的同学是: ", x[0])

# 可以对结构化数据进⾏批量赋值
names = ["Alice", "Bob", "Cindy", "Day"]
score = [86, 45, 68, 98]
heigh = [154, 184, 198, 178]
x["name"] = names
x["score"] = score
x["heigh"] = heigh
print("统⼀赋值后的 x = \n", x)

# 结构化数据的掩码操作
# 选择成绩⼩于90的同学的姓名
print(x[x['score'] < 90]['name'])
