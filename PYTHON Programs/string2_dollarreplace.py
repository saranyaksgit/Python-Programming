a=list(input("Enter a Word:"))
b=input("enter a letter to be replaced:")
c=0
for i in range(len(a)):
	if a[i]==b:
		c+=1
		if c>1:
			a[i]="$"
print("".join(a))		

