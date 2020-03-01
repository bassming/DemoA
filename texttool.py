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
def menu1():
    ttt=t.get(1.0,END)
    ttt1=ttt.split()
    r=simpledialog.askstring('单词个数查找','请输入要查找的单词')
    tkinter.messagebox.showinfo('单词个数查找','单词'+r+'的个数是'+str(ttt1.count(r)))
    lineend=t.index(END)
    lisline=lineend.split('.')
    linenum=int(lisline[0])
    for i in range(1,linenum+1):
        content=t.get(str(i)+'.0',str(i)+'.end')
        liscon=content.split()
        for k in range(len(liscon)):
            if liscon[k] == r:
                temp=0
                for m in range(k):
                    temp+=len(liscon[m])
                t.tag_add(str(temp)+str(i),str(i)+'.'+str(temp+k),str(i)+'.'+str(temp+k+len(r)))
                t.tag_config(str(temp)+str(i),background='red',foreground='white')
def menu2():
    t0=simpledialog.askstring('单词替换','请输入需要替换的单词')
    t1=simpledialog.askstring('单词替换','请输入替换后的单词')
    t11=t.get(1.0,END)
    t111=t11.split()
    for i in range(len(t111)):
        if t111[i]==t0:
            t111[i]=t1
    changet=' '.join(t111)
    t.delete(1.0,END)
    t.insert(1.0,changet)
    tkinter.messagebox.showinfo('单词替换','替换成功')
def menu3():
    u=simpledialog.askstring('删除单词','请输入您要删除的单词')
    s2=t.get(1.0,END)
    liss2=s2.split()
    for item in liss2:
        if item==u:
            liss2.remove(item)
    s22=' '.join(liss2)
    t.delete(1.0,END)
    t.insert(1.0,s22)
    tkinter.messagebox.showinfo('删除单词','删除成功')
def back():
    t.edit_undo()
def save():
    way=simpledialog.askstring('文本另存为','请输入文件路径')
    context=t.get(1.0,END)
    savetext=open(way,'w+')
    savetext.write(context)
    savetext.close()
top=Tk()
top.geometry('740x450')
top['background']='peachpuff'
top.title('lgm的文本编辑器')

t=Text(top,undo=True,width=95,height=25,highlightcolor='red',highlightthickness=1,selectbackground='red',background='LightCyan')
t.grid(row=0,column=0,columnspan=4)
ybar=Scrollbar(top,orient=VERTICAL,width=16)
ybar.config(command=t.yview )
t.config(yscrollcommand=ybar.set)
ybar.grid(row=0,column=4,sticky=NS)

button1=Button(top,text='显示文本',command=opentext,background='orange').grid(row=1,column=0,padx=30)
button2=Button(top,text='单词总数',background='orange',command=words).grid(row=1,column=1)
button3=Button(top,text='全部单词词频',background='orange',command=wordsf).grid(row=1,column=2)
button4=Button(top,text='关键词频统计',background='orange',command=keyword).grid(row=1,column=3)

var=StringVar()
statelabel=Label(top,textvariable=var,background='LightCyan').grid(row=3,column=0)
def state(event):
    location=t.index(CURRENT)
    numlis=location.split('.')
    num=int(numlis[1])+1
    var.set('光标位置之前共有'+str(num)+'个字符')
top.bind('<Button-1>',state)

linkt=Text(top,height=1,width=10)
linkt.grid(row=2,column=1,columnspan=2,pady=25)
label=Label(top,text='此处超链接>',width=10,bg='lightcoral').grid(row=2,column=1)
linkt.insert(1.0,'北航教务网')
linkt.tag_add('link','1.0',END)
linkt.tag_config('link',underline=True,foreground='blue')
def over(event):
    linkt.config(cursor='arrow')
def click(event):
    webbrowser.open('http://jiaowu.buaa.edu.cn/')
linkt.tag_bind('link','<Enter>',over)    
linkt.tag_bind('link','<Button-1>',click)

img=PhotoImage(file='2019060320395547519.gif')
imglabel=Label(top,image=img).grid(row=2,column=2)
