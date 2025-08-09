# Create a program  to find and replace  all email addresses in text using regex

import re

def convert_and_replace(text):
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    text = re.sub(pattern,"[EMAIL_HIDDEN]",text)

    return text
input_txt = input("Enter text")
print(convert_and_replace(input_txt))