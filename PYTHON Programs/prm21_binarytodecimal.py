def binarydecimal():
	p=2
	n=0
	s=0
	print("Binary to Decimal")
	num=int(input("Enter the Binary Number :"))
	while(num!=0):
		rem=num%10
		s=s+rem*p**n
		num=int(num/10)
		n=n+1
	print("The decimal value is",s)
binarydecimal()
	
