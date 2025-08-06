# Menu Driven Calculator
print("Hi, Welcome to you")
def Addition(a,b):
    return a+b
def Subtraction(a,b):
    return a-b
def Multiplication(a,b):
    return a*b
def Division(a,b):
    if b!=0:
        return a/b
    else:
        return "Division with zero are not allowed! "

def Modulus(a,b):
    return a%b
while True:
    print("\n Menu")
    print("1) Addition")
    print("2) Subtraction")
    print("3) Multiplication")
    print("4) Division")
    print("5) Modulus")
    print("Q/q for exit")

    choice = input("Enter your choice based upon Menu\n")
    if choice == 'Q' or choice == 'q':
        print("Existing the Program")
        break
    num1 = float(input("Enter first number : "))
    num2 = float(input("Enter second number : "))

    if choice == '1':
        print("Output:",Addition(num1,num2))
    elif choice == '2':
        print("Output:",Subtraction(num1,num2))
    elif choice == '3':
        print("Output:",Multiplication(num1,num2))
    elif choice == '4':
        print("Output:",Division(num1,num2))
    elif choice == '5':
        print("Output:",Modulus(num1,num2))
    else:
        print("Invalid choice! Please try again.")



