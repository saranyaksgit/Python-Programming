def count_vowels(string):
    vowels = 'aeiou'
    count = 0
    for char in string:
        if char.lower() in vowels:
            count += 1
    return count

# example usage
string = "Hello, world!"
print(count_vowels(string))  # output: 3

