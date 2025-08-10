# Count Words in a line and line in a file
def count_word_and_lines(filename):
    try:
        with open(filename,"r") as file:
            lines = file.readlines()
            line_count = len(lines)
            word_count = sum(len(line.split()) for line in lines)

            print(f"Number of lines = {line_count}\nNumber of words ={word_count}")
    except FileNotFoundError:
        print("File not found!")
    
count_word_and_lines("sample.txt")