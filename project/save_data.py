def save_data(res,source,file_name):

    f=open(str(file_name),'w')
    f.truncate()
    t=''
    for n in range (len(res)):
        t=t+str(res[n])+' '
        for m in range (len(source[n])):
            if m+1==len(source[n]):
                t=t+str(m+1)+':'+str(source[n][m+1])+'\n'
            else:
                t=t+str(m+1)+':'+str(source[n][m+1])+' '
    p=list(t)
    f.writelines(p)
    f.close()

