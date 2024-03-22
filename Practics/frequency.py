name = input("please enter a name \n")
di = {'a':0,'e':0,'i':0,'o':0,'u':0}
for i in name:
    if i in di:
        value=di[i]
        di[i]=value+1
print(di)