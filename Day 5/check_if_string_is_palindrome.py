# Check if a string is a palindrome

# string = "Naman"
# a = string.lower()
# check_str = a[::-1]
# if a == check_str:
#     print("String is Palindrome")
# else:
#     print("String is not Palindrome")

def is_palindrome(text):
    text = "".join(char.lower() for char in text if char.isalnum())
    return text == text[::-1]

input_txt = input("Enter the txt ")
if is_palindrome(input_txt):
    print(f'"{input_txt}" is palindrome')
else:
    print(f'"{input_txt}" is not palindrome')

