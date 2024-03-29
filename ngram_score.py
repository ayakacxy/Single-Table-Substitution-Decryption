from math import log10


class ngram_score(object):
    def __init__(self, ngramfile, sep=' '):
        '''加载包含ngrams和计数的文件,计算对数概率'''
        self.ngrams = {}  # 存储ngrams及其计数的字典
        with open(ngramfile, 'r') as file:
            for line in file:
                key, count = line.split(sep)  # 将行按分隔符分割为ngram和计数
                self.ngrams[key] = int(count)  # 将ngram及其计数存储到字典中
        self.L = len(key)  # ngram的长度
        self.N = sum(self.ngrams.values())  # 所有ngrams的总计数
        # 计算对数概率
        for key in self.ngrams.keys():
            self.ngrams[key] = log10(
                float(self.ngrams[key]) / self.N)  # 计算ngram的对数概率
        self.floor = log10(0.01 / self.N)  # 用于处理未知的ngrams的默认对数概率阈值

    def score(self, text):
        '''计算文本的分数'''
        score = 0
        ngrams = self.ngrams.__getitem__  # 获取ngrams的对数概率函数
        for i in range(len(text) - self.L + 1):
            if text[i:i+self.L] in self.ngrams:
                score += ngrams(text[i:i+self.L])  # 若ngrams在文本中存在，则加上对数概率
            else:
                score += self.floor  # 若ngrams在文本中不存在，则加上默认对数概率阈值
        return score
