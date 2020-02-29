"""
    这是理科大学计算机基础的大作业设计
    基于python的简单文本编辑器
    综合运用字符串处理、matplotlib的数据可视化以及GUI图形用户界面设计
    实现简单文本的单词查找、删除、替换、关键词频统计等功能
"""
from tkinter import *
import tkinter.messagebox
import matplotlib.pyplot as plt
import numpy as np
import re
from tkinter import simpledialog
import webbrowser
f=open('Englishtext.txt','r+')
text=f.read()
text1=re.findall(r'\w+\b',text)
s=(' '.join(text1)).lower()
text2=s.split()
f.close()
fstop=open('stopwords.txt','r')
sw=fstop.read()
stopword=sw.split()
fstop.close()
def opentext():
    t.insert(1.0,s)
    print(s)
def words():
    tt=t.get(1.0,END)
    listt=tt.split()
    print(len(listt))
    tkinter.messagebox.showinfo('单词总数统计','单词总数为'+str(len(listt)))
def wordsf():
    ttt=t.get(1.0,END)
    ttt1=ttt.split()
    wordset=set(ttt1)
    for item in wordset:
        print(item,ttt1.count(item))
def keyword():
    y=[]
    x1=[]
    y1=[]
    ttt=t.get(1.0,END)
    ttt1=ttt.split()
    lis=list(set(ttt1))
    for i in range(len(lis)):
        if lis[i] in stopword:
            continue
        else:
            y.append([ttt1.count(lis[i]),i])
    y.sort(reverse=True)
    for m in range(6):
        x1.append(lis[y[m][1]])
        y1.append(y[m][0])
    x=np.arange(0,6,1)
    keybar=plt.bar(x,y1)
    plt.xticks(x,x1,color='blue')
    plt.xlabel('keywords',color='orange')
    plt.ylabel('frequency',color='orange')
    plt.title('key words frequency bar',color='red')
    for rect in keybar:
        height=rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2,1.05*height,'%d'%int(height))
    plt.show()
