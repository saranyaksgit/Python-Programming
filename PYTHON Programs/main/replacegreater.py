user_input = input("Enter a list of integers separated by spaces: ")
int_list = list(map(int, user_input.split()))
for i in range(len(int_list)):
    if int_list[i] > 100:
        int_list[i] = "over"
print(int_list)

