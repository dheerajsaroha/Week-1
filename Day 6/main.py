# File Handling in Python
# open() method for opening file and r|w|a|r+ are used

# # function used to read file read(),readline(),readlines()
# with open("sample.txt","r+") as file:
#     content = file.read()
#     print(content)
# with open("sample.txt","r+") as file:
#     content = file.readline()
#     print(content)
# with open("sample.txt","r+") as file:
#     content = file.readlines()
#     print(content)

# function used to write content in file, .write() and writelines()
with open("sample1.txt","w+") as file:
    file.write("Hello World!")
    file.writelines(["Dheeraj","Nitin","A"])

# using with statement for file management
try:
    with open("helo_world.txt","r") as file:
        content = file.read()
except FileNotFoundError:
    print("File Not found")