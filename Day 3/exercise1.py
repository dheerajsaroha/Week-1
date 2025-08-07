# Create a function for factorial and call it into another function
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num-1)

def print_factorial(n):
    result = factorial(n)
    print(f"Factorial of {n} is : {result}")
print_factorial(5)