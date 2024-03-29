# 导入所需的库
from pycipher import SimpleSubstitution as SimpleSub  # 使用简单的替代密码
import random  # 用于生成随机数
import re  # 用于处理正则表达式
from ngram_score import ngram_score  # 用于计算解密结果的分数
import tkinter as tk  # 用于创建GUI界面
import proability  # 用于处理密钥的概率

def decrypt_text(ciphertext):
    fitness = ngram_score('quadgrams.txt')  # 加载四元组统计数据
    ctext = re.sub('[^A-Z]', '', ciphertext.upper())  # 将密文中的非字母字符去除，并转换为大写
    maxkey = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')  # 初始的最佳密钥为正常的字母顺序
    maxscore = -99e9  # 初始的最高得分
    parentscore, parentkey = maxscore, maxkey[:]
    print("为了得到正确的结果,请按Ctrl+C退出程序。")
    # 持续进行解密直到用户中断程序
    i = 0
    while True:
        i = i + 1
        random.shuffle(parentkey)  # 随机打乱密钥顺序
        deciphered = SimpleSub(parentkey).decipher(ctext)  # 使用当前密钥解密密文
        parentscore = fitness.score(deciphered)  # 计算当前解密结果的分数
        count = 0
        while count < 1000:
            a = random.randint(0, 25)  # 随机选择两个位置
            b = random.randint(0, 25)
            child = parentkey[:]  # 复制父密钥
            # 在子密钥中交换两个字符的位置
            child[a], child[b] = child[b], child[a]
            deciphered = SimpleSub(child).decipher(ctext)  # 使用子密钥解密密文
            score = fitness.score(deciphered)  # 计算子密钥解密结果的分数
            # 如果子密钥得分更高，则将父密钥替换为子密钥
            if score > parentscore:
                parentscore = score
                parentkey = child[:]
                count = 0
            count = count + 1
        # 记录到目前为止看到的最高得分和对应的最佳密钥
        if parentscore > maxscore:
            maxscore, maxkey = parentscore, parentkey[:]
            ss = SimpleSub(maxkey)
            plaintext = ss.decipher(ctext)
            plaintext1 = add_punctuation_and_spaces(ciphertext, plaintext)  # 添加标点和空格到明文中
            return plaintext1

def output(string1, dic, string2):
    modified_string1 = list(string1)
    modified_string2 = list(string2)
    for i in range(len(string1)):
        if modified_string1[i] in dic and modified_string2[i] != ' ':
            modified_string2[i] = dic[modified_string1[i]]  # 根据密钥字典替换明文中的字符
    modified_string2 = ''.join(modified_string2)
    return modified_string2

def add_punctuation_and_spaces(ciphertext, plaintext):
    result = ""
    j = 0  # 用于遍历明文的索引
    for i in range(len(ciphertext)):
        if not ciphertext[i].isalpha():  # 如果是非字母字符（标点或空格）
            result += ciphertext[i]  # 直接添加到结果中
        else:
            if ciphertext[i].islower():  # 如果是小写字母
                result += plaintext[j].lower()  # 添加对应位置的小写明文字母
            else:
                result += plaintext[j].lower()  # 添加对应位置的小写明文字母
            j += 1  # 明文索引递增
    return result

def decrypt_and_update_output():
    ciphertext = input_entry.get("1.0", tk.END).strip()  # 获取输入的密文
    key = key_entry.get("1.0", tk.END).strip()  # 获取输入的密钥
    key_dic=proability.read_key(key)  # 将密钥解析为字典
    plaintext = decrypt_text(ciphertext)  # 解密密文
    plaintext = output(ciphertext,key_dic,plaintext)  # 根据密钥替换明文中的字符
    output_text.config(state='normal')
    output_text.delete('1.0', tk.END)
    output_text.insert(tk.END, plaintext)
    output_text.config(state='disabled')

# 创建GUI窗口
window = tk.Tk()
window.title('解密工具')

# 设置窗口大小
window.geometry('960x700')

# 创建输入部件
input_label = tk.Label(window, text='输入密文：')
input_label.pack()
input_entry = tk.Text(window, width=55, height=12)
input_entry.pack()

key_label = tk.Label(window, text='密钥(输入格式为a=B,不同密钥之间用空格隔开):')
key_label.pack()
key_entry = tk.Text(window, width=50, height=2)
key_entry.pack()

decrypt_button = tk.Button(window, text='解密', command=decrypt_and_update_output)
decrypt_button.pack()

# 创建输出部件
output_label = tk.Label(window, text='明文：')
output_label.pack()
output_text = tk.Text(window, height=15, state='disabled', width=60)
output_text.pack()

window.mainloop()
