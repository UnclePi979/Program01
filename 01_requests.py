#1.导入模块
import requests

#2.发送请求，获取响应
response = requests.get('http://www.baidu.com')
print(response)
#3.获取响应数据
#print(response.encoding)
# response.encoding = 'utf8'
# print(response.text)
# print(response.content.decode(encoding='utf8'))
response = requests.get('https://ncov.dxy.cn/ncovh5/view/pneumonia')
