# Reverse the words in a sentence without reversing the letters

def reverse_words(sentence):
    # Split sentence into words
    words = sentence.split()
    
    # Reverse the list of words
    reversed_words = words[::-1]
    
    # Join them back into a sentence
    return " ".join(reversed_words)

# Take user input
sentence = input("Enter a sentence: ")
result = reverse_words(sentence)
print("Reversed sentence:", result)
