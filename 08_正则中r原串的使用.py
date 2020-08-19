import re

# 1.在不适用r原串时, 遇到转义怎么做

rs = re.findall('a\nbc', 'a\nbc')
print(rs)

rs = re.findall('a\\nbc', 'a\\nbc')
print(rs)

rs = re.findall('a\\\nbc', 'a\\nbc')
print(rs)

rs = re.findall('a\\\\nbc', 'a\\nbc')
print(rs)

# r原串在正则中就可以消除转义符带来的影响

rs = re.findall(r'a\\nbc', 'a\\nbc')
print(rs)

# 扩展: 可以解决写正则时,不符合PEP8规范的问题(如果写的是'\d'的话,鼠标放在'\d'上会显示不符合PEP8规范)
rs = re.findall(r'\d', '123')
print(rs)