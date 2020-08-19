# 1.导入模块
from bs4 import BeautifulSoup

# 2.创建BeautifulSoup对象
soup = BeautifulSoup('<html>data</html>', 'lxml')
print(soup)