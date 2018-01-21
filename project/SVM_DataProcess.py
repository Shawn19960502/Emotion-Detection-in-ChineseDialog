import prep
from svmutil import *
from Libsvm_Format import *

def SVM_DataProcess(dictionary,pos_data,pos_label,pos_num,neg_data,neg_label,neg_num,neu_data,neu_label,neu_num):
    pos=prep.preprocess(str(dictionary),str(pos_data),pos_num,pos_label)
    neg=prep.preprocess(str(dictionary),str(neg_data),neg_num,neg_label)
    neu=prep.preprocess(str(dictionary),str(neu_data),neu_num,neu_label)

    (pos_res,pos_vec)=pos.vector_generator()
    (neg_res,neg_vec)=neg.vector_generator()
    (neu_res,neu_vec)=neu.vector_generator()
    train_result=[]
    train_vec_libsvm=[]
    train_vec=[]
    train_result=pos_res+neg_res+neu_res
    train_vec=pos_vec+neg_vec+neu_vec

    train_vec_libsvm=Libsvm_format_generator(train_vec)
    
    print("Preprocess Finished")
    return(train_result,train_vec_libsvm)


