import json

# 1.把PYTHON转化为JSON字符串
# 1.1 PYTHON类型的数据
json_str = '''[{"provinceName":"美国","cityName":"","currentConfirmedCount":3424215,"confirmedCount":5494239},
 {"provinceName":"英国","cityName":"","currentConfirmedCount":279163,"confirmedCount":321098}]'''
rs = json.loads(json_str)
# 1.2 转化
json_str = json.dumps(rs, ensure_ascii=False) #1.不要取名为json,会冲突2.多一个属性ensure_ascii=False可以不使用ascii码
print(json_str)

# 2.把PYTHON以JOSN格式存储到文件中
# 2.1 构建要写入的文件对象
with open('data/test1.json', 'w') as fp:
    # 2.2 储存到文件中
    json.dump(rs, fp,ensure_ascii=False)