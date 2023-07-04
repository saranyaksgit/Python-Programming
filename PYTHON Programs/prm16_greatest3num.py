print("Greatest Among Three Numbers")
a=int(input("Enter First Number :"))
b=int(input("Enter Second Number :"))
c=int(input("Enter Third Number :"))
if(a>=b)and(a>=c):
	largest=a
elif(b>=a)and(b>=c):
	largest=b
else:
	largest=c
print("The largest number is",largest)
