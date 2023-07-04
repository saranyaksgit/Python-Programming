print("Ranklist of students in descending order")
n=int(input("How many records :"))
d={}
for i in range(n):
	name=input("Enter name :") 
	marks=int(input("Enter marks :"))
	rank=int(input("Enter the rank :"))
	d[rank]=[marks,name]  
print(sorted(d.values(),reverse=True))  
