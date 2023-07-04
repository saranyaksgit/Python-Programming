print("Student list based on attendance")
n=int(input("How many records :"))
d={}
for i in range(n):
	name=input("Enter name :") 
	attendance=int(input("Enter attendance :"))
	d[name]=[attendance,name]
print(sorted(d.values(),reverse=True))  
