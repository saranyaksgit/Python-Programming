print("Print N Prime Numbers")
n=int(input("Enter the range :"))
print("Prime Numbers till",n)
for num in range(1,n):
	if num>1:
		for i in range(2,num):
			if(num%i)==0:
				break
		else:
			print(num)
