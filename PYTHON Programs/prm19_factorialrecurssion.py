print("Factorial using Recursion")
n=int(input("Enter the number :"))
def fact(x):
	if(x==1):
		return 1
	else:
		return x*fact(x-1)
f=fact(n)
print("Factorial of",n,"=",f)  
