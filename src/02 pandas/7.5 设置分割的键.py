from pandas.tests.groupby.test_value_counts import df

# 普通数组作为分组键
L = [0, 1, 1, 0, 2, 1]
a = df.groupby(L).sum()
print(a)
# 直接⽤键值也可以，⽐较啰嗦
a = df.groupby(df['key']).sum()
print(a)

# 利⽤字典分组
D_mapping = {'A': "One", 'B': "Two", 'C': "Three"}
df = df.set_index('key')
a = df.groupby(D_mapping).sum()
print(a)

# 传⼊任意分组
a = df.groupby(str.lower).mean()
print(a)

# 利⽤上⾯定义的字典，我们可以组合成多级索引
a = df.groupby([str.lower, D_mapping]).mean()
print(a)

'''
      data_1 data_2
a One 101.5 4.0
b Two 102.5 3.5
c Three 103.5 6.0
'''