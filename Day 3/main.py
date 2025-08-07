# function with parameter with return result
def add_numbers(a,b,c):
    sum = a+b+c
    return sum

print("Sum: ",add_numbers(28,9,2002))

greet = "Hi Guys"# Global Scope

def print_msg():
    message="Happy Birthday!" #Local Scope
    return message
print(greet)
print(print_msg())