#encoding=utf-8
import sys
import codecs
import os
'''from Data_final_process import *
from svmutil import *'''
def input_message_process(a):
    b=[]
    for i in range(len(a)):
        if a[i] == 'A':
            for k in range(i+1,len(a)):
                if a[k]=='\s':
                    break
                if a[k]=='\n':
                    break
                if a[k]=='B':
                    break
                else:
                    b+=a[k]
    f = codecs.open('final_test.txt', 'w','utf-8')
    f.truncate()
    f.writelines(b)
    f.close
''''    m=svm_load_model('model_file.txt')
   (x,y)=SVM_Final_DataProcess("final_test.txt")
    print(y[0][1947])
    print(x)
    print(len(y[0]))
    l_labels, l_acc, l_vals = svm_predict(x,y,m)
    print(l_labels)
    return(l_labels)'''

