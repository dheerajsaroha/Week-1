# Create a program that count numbers of occurences of a specific word in a text file
# def count_word_occurences(filename):
#     try:
#         with open(filename,"r") as file:
#             sentence = file.read()
#             words = sentence.split()
#             # initialize a dictionary
#             word_count = {}

#             # count word frequency
#             for word in words:
#                 word = word.lower()
#                 if word in word_count:
#                     word_count[word] +=1 
#                 else:
#                     word_count[word] =1
#             print(word_count)
#     except FileNotFoundError:
#         print("File Not Found")

# count_word_occurences("sample.txt")

# updated code

import re

def count_word_occurrences(filename):
    try:
        with open(filename, "r") as file:
            text = file.read().lower()
            words = re.findall(r"\b\w+\b", text)  # Extract words ignoring punctuation

            word_count = {}
            for word in words:
                word_count[word] = word_count.get(word, 0) + 1

            print(word_count)
    except FileNotFoundError:
        print("File Not Found")

count_word_occurrences("sample.txt")
