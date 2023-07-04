print("Check whether it is a Prime Number")
n=int(input("Enter the number :"))
temp=0
if(n>1):
	for i in range(2,n):
		if(n%i)==0:
			temp=1
			break
if(temp==1):
	print(n,"is not a Prime Number")
else:
	print(n,"is a Prime Number")

