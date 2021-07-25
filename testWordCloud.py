#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @author_="Sen"
# @date:2021/7/24 22:00
# @FileName: testWordCloud.py
# @Email : 
# @Software: PyCharm
# @Blog ：

import jieba
from matplotlib import pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import numpy as np
import sqlite3

#准备工作
con=sqlite3.connect('movie.db')
cur=con.cursor()
sql='select  instruction from movie250'
data=cur.execute(sql)
text=""
for item in data:
    text=text+item[0]
#print(text)

cur.close()
con.close()

# 分词
cut=jieba.cut(text)
string='  '.join(cut)

#绘图

#生成遮罩
img=Image.open(r".\static\assets\images\img.png")
img_array=np.array(img)#将图片转为数组

wc=WordCloud(
    background_color='white',
    mask=img_array,
    font_path=r"C:\Windows\Fonts\msyhbd.ttc"#注意路径
)
wc.generate_from_text(string)

#绘制图片
fig=plt.figure(1)
plt.imshow(wc)
plt.axis('off')#是否显示坐标轴
#plt.show()#显示生成的词云
plt.savefig("word.jpg")
print("保存成功")
#plt.show("word.jpg")




