a =20
b = 30 if a>20 else 40
print (b) # if a grater than 20 then b should be 30 otherwise 40 as else

z= 100
y = 101 if z>90 else 99
print (y)

a = 21
b = 30
c = a if a>b else b
print (c)

# user input
a = int(input("please enter age"))
b = int(input("plesae enter number"))
max = a if a>b else b
print ("max",max)

#-------tripple value

x=19
y=18
z=20
max = x if x>y and x >z else y if y>z else z
print ("max",max)