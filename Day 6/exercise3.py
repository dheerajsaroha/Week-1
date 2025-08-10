# Write a program to copy the contents of one file to another
# def copy_content(filename,newfile):
#     try:
#         with open(filename,"r") as file:
#             content = file.readlines()
#     except FileNotFoundError:
#         print("File Not Found!")
    
#     try:
#         with open(newfile,"w") as file:
#             for line in content:
#                 file.write(line)
#     except PermissionError:
#         print("File Do not have Permission to write or update")

# copy_content("sample.txt","sample_copy.txt")

# with open("sample_copy.txt","r") as file:
#     content = file.read()
#     print(content)

# updated code
def copy_content(filename, newfile):
    try:
        with open(filename, "r") as file:
            content = file.readlines()
    except FileNotFoundError:
        print("File Not Found!")
        return  # Exit early if file not found

    try:
        with open(newfile, "w") as file:
            file.writelines(content)  # Write all at once
    except PermissionError:
        print("File does not have permission to write or update")

# Copy the file
copy_content("sample.txt", "sample_copy.txt")

# Display copied content
with open("sample_copy.txt", "r") as file:
    print(file.read())
