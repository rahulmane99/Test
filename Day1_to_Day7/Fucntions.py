x = 8
print (id(x))
#if will give the address of stored variables

a = "9.1"
print (id(a))

s = "abc"
print (id(s))

y = 9
z = 9
print (id(y),id(z))
print (y is z)

q=999
w=999
print (q is w)
# above statement showing as veriable stored address location with (id) and is for comapreing the values
#------------------

print ("Hello World") # printing in same line
print ("Hello\n world") # \n meanse printing in next line
print ("hello\t world") #\t measn in next tab
print ("Hello \"world\"") #\" before and after the veriables
#print ("Hello \\world\") print ("Hello \\world\")
           #SyntaxError: unterminated string literal (detected at line 26)
print("hello \\ world") # \\ for singal \