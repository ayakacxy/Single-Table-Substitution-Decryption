# Single Table Substitution Decryption

#### 介绍
单表代换解密器

#### 软件架构
代换密码（``Simple Substitution Cipher``），顾名思义，就是一种使用``substitution``来进行加密的算法。代换密码采用一一映射的方式，将明文每个字符逐一唯一地代换成另外的一个字符。本程序采用贪心算法中的爬山法。在这种算法中，我们需要通过尝试不同解密密钥，然后给每一个解密出来的明文计算出一个适应度。若解密出来的明文越接近我们的日常用的英语，它的适应度就越高；若解密出来的明文越难读懂或者越不像我们日常用的英语，则其适应度越低。

本算法是一个基于``quadgram statistics``计算适应度的模型。该模型的具体内容可以访问这个网页：http://practicalcryptography.com/cryptanalysis/text-characterisation/quadgrams/.
这个算法的具体运行步骤如下：

1.  首先先随机生成一个解密密钥``key``，称为``parentkey``，用它解密得对应的明文``m1``，对明文计算适应度为``d1``。

2.  然后随机交换``parentkey``中的两个字符得到子密钥``childkey``，解密出对应的明文``m2``并计算适应度``d2``。

3.  若``d1<d2``，则``childkey``成为新的``parentkey``。

4.  然后不断循环迭代，直到不再产生适应度更大的密钥``key``。

5.  回到第一步重新生成``parentkey``继续迭代寻找，或者由操作者终止程序（``crtl+c``退出程序）。

（第5步的主要目的是防止第2步和第3步的操作使其陷入局部最优的情况。）


#### 安装教程

1.  首先修改``main.py``中``quadgrams.txt``的文件路径为本地路径
2.  然后打开``main.py``直接运行


#### 使用说明

本程序是一个基于``ngram``模型的爬山法破解单表代换的一个``python``脚本。
1.  ``main.py``为本程序的主函数，其余``.py``文件均为``main.py``所调用的模块。
2.  本程序允许英文字符输入但不仅限于英文字符，如果输入的为非英文字符，如``#&``等，则首先运行``read.py``,然后输入要破译的字符串，并把输出作为解密器的输入。
3.  运行``main.py``会出现图形化界面，根据页面提示即可破解密文。
4.  密钥的添加会直接改变明文中对应的内容，可能会对破解明文的正确性带来一定影响。
5.  本程序算法基于贪心算法，如果觉得最终输出的明文不符合预期，可以点击``decrypt``按键继续迭代。
6.  程序在计算较短密文时，可能会出现陷入局部最优的情况，暂时无法解决。
7.  在``proability``模块中，注释的部分可以用于字频的攻击，函数可以直接调用，用于统计一元，二元，三元英文字母组的频率。


