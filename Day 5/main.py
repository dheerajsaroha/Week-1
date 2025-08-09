# Working with string

# String manipulation
# 1) Concatenation
string = "Hello"
string1 = "World"

result = string +" "+string1
print(result)

# 2) Slicing
string ="Python Programming"
print(string[:])

# 3) Format
name = "Dheeraj"
age = 22
print(f"My name is {name} and I'm {age} years old.")

# Common string method
# # Split() used to store string element in list
# num = input("Enter the number")
# print(num.split())
# num1 = []
# for i in range(0,len(num)):
#     print(type(num[i]))
# print(num1)
# for i in num:
#     a = int(i)
#     num1.append(a)
# print(num1)
# print(type(num1[0]))

# join()
print(string.join("Hi"))

# replace()-> replace a substring to other string
string1 = "Hello"
string2 = "World"
string3 =string1.replace(string1,string2)
print(string3)

# strip() function removee whitespaces
string_1 = " My name is Dheeraj . I am from  Panipat. I will graduate in 2026 "
print(string_1)
print(string_1.strip())
print(string_1.lstrip())
print(string_1.rstrip())

# Regular Expression for Pattern matching
# regular is just a way to search and match and also manipulate on the basis of the pattern
import re
print(re.search("@","dheerajsaroha2892002@gmail.com"))
print(re.findall(r".com","dheerajsaroha2892002@gmail.com and btcl220010159010gjust@gmail.com"))
text = "contact me at 893-060-1580"
digit = re.findall(r"\d+",text)
print(digit)

updated_txt = re.sub(r"\d","X",text)
print(updated_txt)