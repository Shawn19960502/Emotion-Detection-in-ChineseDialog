#encoding=utf-8
import sys
import codecs
import os
import jieba
import jieba.analyse
lines=[]
i=0
source = codecs.open("dictt.txt", 'r','utf-8')
result = codecs.open("dict.txt",'w','utf-8')
line=source.readline()
while line:
    i+=1
    lines+=line
    line=source.readline()
    liness=['\n' if x == '\r' else x for x in lines]
result=result.writelines(["%s" % item  for item in liness])
print(i)
