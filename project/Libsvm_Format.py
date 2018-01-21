def Libsvm_format_generator(x):
    p=[]
    b={}
    index=[[i+1 for i in range(len(x[0]))] for k in range(len(x))]
    for k in range (len(x)):
        b[k]={}
        for i in range (len(x[0])):
            b[k][index[k][i]]=x[k][i]
    for k in range (len(x)):
        p.append(b[k])
    return(p)
