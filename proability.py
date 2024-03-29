def notuse (notusing_character):#用于屏蔽在密文破解时用于分割句子的符号，例如句号，分号这类符号
    blacklist={}
    #允许用户重复输入一个黑名单字符，采用字典类型存储黑名单。
    for char in notusing_character:
        if (char in blacklist):
            blacklist[char]+=1
        else:
            blacklist[char]=1
    return blacklist

def read_key(string):#读入密钥，并生成映射字典
   pairs = string.split()  # 分割字符串为键值对列表
   dict={}
   for pair in pairs:
       key, value = pair.split('=')  # 分割键值对为键和键值
       dict[key] = value
   return dict

# # def count_character(string, blacklist):
# #     "记录不同字符的概率"
# #     character_count = {}#存放字符频率的字典
# #     number1 = 0
# #     for char in string:
# #         if (char not in blacklist):#跳过黑名单字符
# #             if (char in character_count):
# #                 character_count[char] += 1
# #             else:
# #                 character_count[char] = 1
# #             number1 += 1#计算有效字符的总个数

# #     character_proability = {}#存放字符概率的字典
# #     for char, count in character_count.items():
# #         proability = count / number1
# #         formatted_proability = "{:.2%}".format(proability)
# #         character_proability[char] = formatted_proability#计算字符的概率

#     # return sort_dict(character_proability)
def count_bingary_character(string,blacklist):
    "记录二元字符的概率"
    bingary_character_count = {}#存放二元字符频率的字典
    number2=0
    # 遍历字符串，提取二元字符并统计频率
    for i in range(len(string) - 1):
        char1 = string[i]
        char2 = string[i + 1]

        if (char1 not in blacklist) and (char2 not in blacklist):  # 跳过黑名单字符，若两个字符都不在黑名单中则合成一个二元字符
            bingary_character = char1 + char2

            if bingary_character in bingary_character_count:
                bingary_character_count[bingary_character] += 1
            else:
                bingary_character_count[bingary_character] = 1
        number2+=1#计算有效二元字符的数量

    bingary_character_proability = {}#存放二元字符概率的字典
    for bingary_character, count in bingary_character_count.items():
        probability = count / number2
        formatted_proability = "{:.2%}".format(probability)
        bingary_character_proability[bingary_character] = formatted_proability#计算二元字符的概率

    return sort_dict(bingary_character_proability)

# def count_ternary_character(string,blacklist):
#     "记录三元字符的概率"
#     ternary_character_count = {}#存放三元字符频率的字典
#     number3=0
#     # 遍历字符串，提取三元字符并统计频率
#     for i in range(len(string) - 2):
#         char1 = string[i]
#         char2 = string[i + 1]
#         char3 = string[i + 2]

#         if (char1 not in blacklist) and (char2 not in blacklist) and (char3 not in blacklist):  # 跳过黑名单字符，若三个字符都不属于黑名单则合成一个三元字符
#             ternary_character = char1 + char2 +char3
#             if ternary_character in ternary_character_count:
#                 ternary_character_count[ternary_character] += 1
#             else:
#                 ternary_character_count[ternary_character] = 1
#         number3+=1#计算有效三元字符的数量

#     ternary_character_proability = {}#存放三元字符概率的字典
#     for ternary_character, count in ternary_character_count.items():
#         proability = count / number3
#         formatted_proability = "{:.2%}".format(proability)#直接把小数显示为百分数
#         ternary_character_proability[ternary_character] =formatted_proability#计算三元字符的概率

#     return sort_dict(ternary_character_proability)


def print_dict(dictionary):  # 打印字典
    dictionary = sort_dict(dictionary)
    for key, value in dictionary.items():
        print(key, ":", value)


def sort_dict(percentage_dict):  # 字典排序
    sorted_dict = dict(sorted(percentage_dict.items(
    ), key=lambda item: float(item[1].rstrip("%")), reverse=True))
    return sorted_dict

# def read_frequency_file(file_path,frequency_dict):#读入英文字频分布
#     with open(file_path, 'r') as file:
#         for line in file:
#             line = line.strip()
#             if line:  # 确保不是空行
#                 letter, frequency = line.split()
#                 letter = letter.strip()
#                 frequency = frequency.strip().rstrip('%')
#                 frequency = float(frequency) / 100.0  # 将百分数转换为浮点数
#                 formatted_number = "{:.2%}".format(frequency)#直接把小数显示为百分数
#                 frequency_dict[letter] =formatted_number
#     return frequency_dict

# def read_frequency_file1(file_path,frequency_list):#三元组的具体频率没找到只找到概率排序
#     with open(file_path, 'r') as file:
#         for line in file:
#             line = line.strip()
#             if line:
#                 frequency_list.append(line)
#     return frequency_list

# def print_list(lst):
#     for index, value in enumerate(lst):
#         print(f"Index {index}: {value}")
