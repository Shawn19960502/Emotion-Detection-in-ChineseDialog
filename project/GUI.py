#encoding=utf-8
from tkinter import *
import sys
import codecs
import os
from input_process import *
from predct_final import *
def check():
    content=t.get('1.0',END)
    a=list(content)
    input_message_process(a)
    q=predict()
    print(q)
    if q[0]==1.0:
        p.delete(0,END)
        p.insert(0,"积极")
    elif q[0]==0.0:
        p.delete(0,END)
        p.insert(0,"中性")
    elif q[0]==-1.0:
        p.delete(0,END)
        p.insert(0,"消极")
    else:
        p.delete(0,END)
res=StringVar
top=Tk()
top.title('text_check')
v1=StringVar()
v2=StringVar()
t=Text(top,width=80,height=10,background="grey")
Button(top,text='test',command=check,width=10,height=2).grid(row=1,column=0)
p=Entry(top,width=12)
t.grid(row=0,column=0,padx=10,pady=10)
p.grid(row=1,column=0,padx=10,pady=10,sticky=E)

top.mainloop()


