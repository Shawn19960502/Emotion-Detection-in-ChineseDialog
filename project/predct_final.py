from Data_final_process import *
from svmutil import *


def predict():
    m=svm_load_model('model_file.txt')
    (x,y)=SVM_Final_DataProcess("final_test.txt")
    l_labels, l_acc, l_vals = svm_predict(x,y,m)
    return(l_labels)

