def count_consonants(string):
    consonants = "bcdfghjklmnpqrstvwxyz"
    count = 0
    for char in string:
        if char.lower() in consonants:
            count += 1
    return count

string = "Hello, World!"
print("Number of consonants in the string:", count_consonants(string))

