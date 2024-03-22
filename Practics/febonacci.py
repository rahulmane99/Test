x= int(input("Please enter a number \n"))
a=0
b=1
c=0
for i in range(x):
    print(c, end=" ")
    a=b
    b=c
    c=a+b