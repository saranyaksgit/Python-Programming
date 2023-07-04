def find_longest_word(words_list):
    longest_word = ""
    for word in words_list:
        if len(word) > len(longest_word):
            longest_word = word
    return len(longest_word)
    
words_list = ["apple", "banana", "orange", "pineapple"]
print("Length of the longest word in the list:", find_longest_word(words_list))

