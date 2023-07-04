def fib():
	x=0;
	y=1;
	n=int(input("Enter the limit :"))
	print("The fibonnaci series is :")
	print(x)
	print(y)
	while(n>=0):
		z=x+y
		x=y
		y=z
		n=n-1
		print(z)
fib()
