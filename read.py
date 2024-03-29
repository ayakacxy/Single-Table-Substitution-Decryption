import string
def map_to_lowercase(s):
    # 获取小写字母表
    lowercase = string.ascii_lowercase
    # 创建一个空字典
    mapping = {}
    # 遍历字符串中的字符
    for i, c in enumerate(s):
        # 如果字符不在字典中，就将其映射到小写字母表中的相应位置
        if c not in mapping:
            mapping[c] = lowercase[i % 26]
    # 创建一个空字符串
    result = ""
    # 遍历字符串中的字符
    for c in s:
        # 如果字符在字典中，就用字典中的值替换它，否则保持不变
        result += mapping.get(c, c)
    # 返回结果
    return result
input_string=input()
input_string=map_to_lowercase(input_string)
print(input_string)