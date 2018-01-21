from svmutil import *
from SVM_DataProcess import *
from SVM_Training_Save import *

(train_result, train_vec)= SVM_DataProcess("dict.txt","pos.txt",1,5126,"neg.txt",-1,5263,"neutral.txt",0,5026)
(test_result, test_vec)=SVM_DataProcess("dict.txt","test_dialog_pos.txt",1,10,"test_dialog_neg.txt",-1,10,"test_dialog_neu.txt",0,10)
m=SVM_Training_Save(train_result,train_vec,'-s 0 -t 0 -c 30',"model_file.txt",0)
#m=SVM_Training_Save(train_result,train_vec,'-s 0 -t 2 -c 10 -g 0.01',"model_file.txt",0)
#(test_result, test_vec)=SVM_DataProcess("dict.txt","test_dialog_pos.txt",1,5,"test_dialog_neg.txt",-1,6,"test_dialog_neu.txt",0,5)
#m=svm_load_model('model_file.txt')
p_labels, p_acc, p_vals = svm_predict(train_result, train_vec,m)
l_labels, l_acc, l_vals = svm_predict(test_result, test_vec,m)

