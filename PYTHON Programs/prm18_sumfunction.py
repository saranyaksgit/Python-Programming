def add():
	print("Sum of N numbers")
	n=int(input("Enter a limit :"))
	sum=0
	for i in range(1,n+1):
		sum=sum+i
	print(sum)
add()
