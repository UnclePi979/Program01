# 一、
# 1.导入模块
from bs4 import BeautifulSoup
# 2.准备文档字符串
html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <title>The Dormouse's story</title>
</head>
<body>
<p class="title">
<b>The Dormouse's story</b>
</p>
<p class="story">Once Upon a time three were three little sister;and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>, 
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>and 
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well. 
</p>
<p class="story">...</p>
</body>
</html>
'''
# 3.创建BeautifulSoupd对象
soup = BeautifulSoup(html,'lxml')
# 4.查找title标签
title = soup.find('title')
print(title)
# 5.查找a标签
a = soup.find('a')
print(a)
#查找所以的a标签
a_s = soup.find_all('a')
print(a_s)
# 二、
# 查找id为link1的标签
# 1:通过命名参数进行指定的
a = soup.find(id='link1')
print(a)
# 2:使用attrs来指定属性字典,进行查找
a = soup.find(attrs={'id': 'link1'})
print(a)
# 三.根据文本内容进行查找
text = soup.find(text='Elsie')
print(text)

# Tag对象 ,对应xml或者html标签
print(type(a)) #<class 'bs4.element.Tag'>
print('标签名:', a.name)
print('标签所有属性:', a.attrs)
print('标签内容:', a.text)