print("Prime Numbers in an Interval")
beg=int(input("Enter the first interval :"))
end=int(input("Enter the second interval :"))
print("Prime numbers between",beg,"and",end,"are:")
for num in range(beg,end+1):
	if num>1:
		for i in range(2,num):
			if(num%i)==0:
				break
		else:
			print(num)
