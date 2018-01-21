import prep
from svmutil import *
from Libsvm_Format import *

def SVM_Final_DataProcess(data):
    data=prep.preprocess("dict.txt",str(data),1,1)
    (data_res,data_vec)=data.vector_generator()

    data_vec_libsvm=Libsvm_format_generator(data_vec)

    return(data_res,data_vec_libsvm)


