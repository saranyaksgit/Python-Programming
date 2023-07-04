# Define a list of integers
my_list = [10, 20, 30, 40, 50]

# (a) Find the sum of the elements in the list
list_sum = sum(my_list)
print("Sum of the elements in the list:", list_sum)

# (b) Total number of elements in the list
num_elements = len(my_list)
print("Total number of elements in the list:", num_elements)

# (c) Insert an element into the list at the specified index
my_list.insert(2, 25) # Insert the value 25 at index 2
print("List after inserting element:", my_list)

# (d) Copy the contents of list into another list
new_list = my_list.copy()
print("New list:", new_list)

