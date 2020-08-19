# 导入正则模块
import re

# 字符匹配
rs = re.findall('abc', 'abc')
rs = re.findall('a.c', 'a\nc') # '.'可以匹配除'\n'外的任意符号
rs = re.findall('a.c', 'abc')
rs = re.findall('a\.c', 'a.c')# 用转义符'\'可以使'.'变为原来的意思
rs = re.findall('a[bc]d', 'abd')# [...]匹配字符集中任意字符

# 预定义的字符集
rs = re.findall('\d', '123') # '\d'匹配[0-9]任意数字
rs = re.findall('\w', 'Az123_阿达%$')# '\w'匹配[A-Za-z0-9_]中文也行,除了'_'外的特殊字符不行


# 数量词
rs = re.findall('a\d*', 'a123') # '*'表示出现0次或多次,就是克林闭包啦.前面一定要有一个限定符,因为'*'是允许匹配空的.
rs = re.findall('a\d+', 'a') # '+'表示出现1次或多次,就是正闭包啦.所以这边这个不匹配.
rs = re.findall('a\d?', 'a123')# '?'匹配0个或1个字符.
rs = re.findall('a\d{2}', 'a123')# '{m}'花括号里面加数字可以匹配当前字符m次
print(rs)