a= int(input("Please enter the number"))
print (a)
if a%2 == 0:
    print(f"This number is even")
else:
    print(f"this number is odd")

#-------------------------------------------------

x = int(input("please enter the number"))
y = range(1,x+1,1)
sum = 0
for i in y:
    if i % 2 != 0:
        print(i, end=" ")
    sum = sum+i
print()
print("sum", sum)

#sum of odd value

n=int(input("Please enter a number "))
x = range(1,n+1,1)
add=0
for i in x:
    if i % 2 != 0:
        print (i, end=" ")
        add = add+i
print()
print ("sum", add)
