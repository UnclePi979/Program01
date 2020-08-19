import re

# re.findall(pattern, string, flags=0) 格式

# 1.findall方法, 返回匹配的结果列表
rs =re.findall('\d+', 'chuan13zhi24')
print(rs)

# 2.findall方法中,flag参数的作用
rs = re.findall('a.bc', 'a\nbc')
rs = re.findall('a.bc', 'a\nbc', re.DOTALL) #更改匹配模式可以直接和换行符'\n'匹配
rs = re.findall('a.bc', 'a\nbc', re.S) #更改匹配模式可以直接和换行符'\n'匹配,re.DOTALL和re.S匹配的效果一样
print(rs)

# 3.findall方法中分组的使用
rs = re.findall('a.+bc', 'a\nbc', re.DOTALL)
print(rs)

rs = re.findall('a(.+)bc', 'a\nbc', re.DOTALL) #'()'可以用作定位,例如这里只要夹在a和bc之中的部分
print(rs)