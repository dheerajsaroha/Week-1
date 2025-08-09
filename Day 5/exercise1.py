# create a Text Cleaner
import re

def clean_txt(text):
    # remove puntuation
    text = re.sub(r"[^\w\s]","",text)

    # remove extra spaces
    text = " ".join(text.split())

    # convert to lowercase
    return text.lower()

input_txt = "Hello World!  Welcome to the re;al world ; Be Honest There is no real world"

print(clean_txt(input_txt))