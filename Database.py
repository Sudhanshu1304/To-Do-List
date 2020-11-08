File="Enter the File path here "

def Count_tab(value):
    count=0
    for e in value:
        if e=='\t':
            count=count+1
    return count


def Remove_tab(val):
    a=val.split('\t')
    return a[-1]


def Done(task):
    pass

def Read():

    file=open(File,"r")
    content=file.read()
    content=content.split(":\n")
    content.reverse()
    main_dic={}
    child_dic={}
    input=0
    for cont in content:
        if len(cont)>=1:

            if Count_tab(cont)==2:
                cont = Remove_tab(cont)
                input=cont
            elif Count_tab(cont)==1:
                cont = Remove_tab(cont)
                child_dic[cont]=input
            elif Count_tab(cont)==0 :
                cont = Remove_tab(cont)
                user=cont
                main_dic[user] = child_dic
                child_dic={}

    file.close()

    return main_dic



def Write3(dic):
    file = open(File, "w")
    for user in dic.keys():
        file.write(user + ":\n")
        D = dic[user]
        for task in D.keys():

            if len(D[task]) != 0:
                Tab(1, file)
                file.write(task + ":\n")
                Tab(2, file)
                file.write(D[task] + ":\n")

    file.close()


def Write2(dic):

    previous_data = Read()
    if len(list(previous_data.keys()))==0:
        previous_data=dic


    for user in dic.keys():

        if user  in  list(previous_data.keys()):
            previous_data[user].update(dic[user])
        else:
            previous_data[user]=dic[user]

    file = open(File, "w")
    for user in previous_data.keys():
        file.write(user + ":\n")
        D = previous_data[user]
        for task in D.keys():
            #print("Task is : ",task)
            if len(D[task]) != 0:
                Tab(1, file)
                file.write(task + ":\n")
                Tab(2, file)
                file.write(D[task] + ":\n")

    file.close()


def Tab(val,file):
    for _ in range(val):
        file.write("\t")










