# Single Table Substitution Decryption

#### 介绍
单表代换解密器

#### 软件架构
代换密码（Simple Substitution Cipher），顾名思义，就是一种使用substitution来进行加密的算法。代换密码采用一一映射的方式，将明文每个字符逐一唯一地代换成另外的一个字符。本程序采用贪心算法中的爬山法。在这种算法中，我们需要通过尝试不同解密密钥，然后给每一个解密出来的明文计算出一个适应度。若解密出来的明文越接近我们的日常用的英语，它的适应度就越高；若解密出来的明文越难读懂或者越不像我们日常用的英语，则其适应度越低。

本算法是一个基于quadgram statistics计算适应度的模型。该模型的具体内容可以访问这个网页：http://practicalcryptography.com/cryptanalysis/text-characterisation/quadgrams/.
这个算法的具体运行步骤如下：

1.首先先随机生成一个解密密钥key，称为parentkey，用它解密得对应的明文m1，对明文计算适应度为d1。

2.然后随机交换parentkey中的两个字符得到子密钥childkey，解密出对应的明文m2并计算适应度d2。

3.若d1<d2，则childkey成为新的parentkey。

4.然后不断循环迭代，直到不再产生适应度更大的密钥key。

5.回到第一步重新生成parentkey继续迭代寻找，或者由操作者终止程序（crtl+c退出程序）。

（第5步的主要目的是防止第2步和第3步的操作使其陷入局部最优的情况。）


#### 安装教程

1.  首先修改main.py中quadgrams.txt的文件路径为本地路径
2.  然后打开main.py直接运行


#### 使用说明

1.  首先阅读readme.txt
2.  之后根据文档操作即可


