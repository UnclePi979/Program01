# coding=gbk
import json

# 1.把JSON字符串转化为PYTHON数据
# 1.1准备json字符串
json_str = '''[{"provinceName":"美国","cityName":"","currentConfirmedCount":3424215,"confirmedCount":5494239},
 {"provinceName":"英国","cityName":"","currentConfirmedCount":279163,"confirmedCount":321098}]'''
# 1.2转化
rs = json.loads(json_str)
# print(rs)
# print(type(rs))
# print(type(rs[0]))

# 2.把JOSN格式文件转化为PYTHON类型的数据
# 2.1构建指向该文件的对象
with open('data/test.json', encoding='utf8') as fp:   #我的电脑是需要加上encoding='utf8'的,不然会乱码.
    # 2.2加载该文件对象并转化
    python_list = json.load(fp)
    print(python_list)
    print(type(python_list))
    print(type(python_list[0]))