#encoding=utf-8
import sys
import codecs
import os
import jieba
import jieba.analyse
def dict_vec_generator(txt):
    a=list()
    b=list()
    source = codecs.open(str(txt), 'r','utf-8')
    line = source.readline()
    line = line.replace('\r','\n')
    line=line.replace(' ','')
    line=line.replace('2','')
    line=line.replace('3','')
    line=line.replace('4','')
    line=line.replace('1','')
    line=line.replace('5','')
    line=line.replace('6','')
    line=line.replace('7','')
    line = line.rstrip('\n')
    line = line.rstrip(' ')
    while line!="":
        a=jieba.lcut(line,HMM=False)
        b+=a
        line = source.readline()
        line = line.rstrip('\n')
        line = line.rstrip(' ')
        line=line.replace(' ','')
        line=line.replace('1','')
        line=line.replace('2','')
        line=line.replace('3','')
        line=line.replace('4','')
        line=line.replace('5','')
        line=line.replace('6','')
        line=line.replace('7','')
    return(b)
def data_vec_generator(txt,data_num):
    a=list()
    b=[[] for row in range(data_num)]
    source = codecs.open(str(txt), 'r','utf-8')
    for c in range(data_num):
        line = source.readline()
        line=line.replace('\r','\n')
        while line:
            if line=='\n':
                break
            if line=='\n\n':
                break
            else:
                a=jieba.lcut(line,HMM=False)
                b[c]+=a
                line = source.readline()
                line=line.replace('\r','\n')
    return(b)
def length_of_dictionary(txt):
    length=codecs.open(str(txt),'r','utf-8')
    c=len(length.readlines())
    return(c)

class preprocess:
    '''this module is used to preprocess the data'''
    def __init__(self,dictionary,data,data_num,data_prop):
        self.dictionary=dictionary
        self.data=data
        self.data_num=data_num
        self.data_prop=data_prop
        print("preprocess constructor is called")
    def vector_generator(self):
        vec=[[0 for col in range(length_of_dictionary(self.dictionary))] for row in range(self.data_num)]
        jieba.set_dictionary(str(self.dictionary))
        jieba.initialize()
        x=[]
        y=[]
        x=dict_vec_generator(str(self.dictionary))
        y=data_vec_generator(str(self.data),self.data_num)
        for l in range(self.data_num):
            for k in y[l]:
                for j in x:
                    if k==j:
                        vec[l][x.index(j)]+=1
        res=[self.data_prop]*self.data_num
        
        return(res,vec)




