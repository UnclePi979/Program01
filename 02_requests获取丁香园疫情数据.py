# 1.导入模块
import requests
# 2.发送请求
response =requests.get('https://ncov.dxy.cn/ncovh5/view/pneumonia')
# 3.从响应中获取数据
print(response.content.decode())