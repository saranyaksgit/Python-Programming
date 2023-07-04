print("Arithmetic Operations")
print("Enter two Numbers")
a=int(input("Enter first number :"))
b=int(input("Enter second number :"))
print("Operations are : + , - , * , % , /")
c=input("Enter your choice :")
if c=='+':
	add=a+b
	print(add)
elif c=='-':
	dif=a-b
	print(dif)
elif c=='*':
	mul=a*b
	print(mul)
elif c=='/':
	div=a/b
	print(div)
elif c=='%':
	mod=a%b
	print(mod)
else:
	print("invalid input")
	
