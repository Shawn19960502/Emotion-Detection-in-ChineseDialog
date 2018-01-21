from svmutil import *
from SVM_DataProcess import *

def SVM_Training_Save(train_result,train_vec_libsvm,parameter,file,switch):
    prob = svm_problem(train_result, train_vec_libsvm)
    param = svm_parameter(str(parameter))
    print("Start Training")
    model = svm_train(prob, param)
    print("Stop Training")
    if switch==1:
        svm_save_model(str(file),model)
    else:
        return(model)
'''
a=[1,1,0,0]
b=[{1:1,2:1},{1:2,2:2},{1:3,2:3},{1:4,2:4}]
SVM_Training_Save(a,b,'-s 0 -t 0 -c 200','model_file.txt',1)
'''
