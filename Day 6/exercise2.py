# Write and read a list of items
def write_items_to_file(filename,items):
    try:
        with open(filename,"w") as file:
            for item in items:
                file.write(item + "\n")
    except PermissionError:
        print("File don't have permission to write!")

def read_items_from_file(filename):
    try:
        with open(filename,"r") as file:
            items = file.readlines()
            print("Items in files")
            for item in items:
                print(item.strip())
    except FileNotFoundError:
        print("File Not Found!")

fruits = ["Apple","banana","guava","grapes","berry"]
write_items_to_file("fruits.txt",fruits)
read_items_from_file("fruits.txt")