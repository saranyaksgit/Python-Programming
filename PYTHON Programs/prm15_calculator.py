print("CALCULATOR")
print("__________")
print("Enter two numbers")
a=int(input("Enter the first number :"))
b=int(input("Enter the second number :"))
print("Choose your operaton : + , - , * , \ , % ")
op=input("Enter your option :")
if(op=="+"):
	sum=a+b
	print("Sum is :",sum)
elif(op=="-"):
	sub=a-b
	print("Difference is :",sub)
elif(op=="*"):
	mul=a*b
	print("Product is :",mul)
elif(op=="/"):
	div=a/b
	print("Dividion is :",div)
elif(op=="%"):
	mod=a%b
	print("MOdulus is :",mod)
else:
	print("Invalid Choice")	
