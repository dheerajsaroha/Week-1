n= int(input("Enter your number : "))
if n<=1:
    print("Number is not prime")
else:
    is_Prime = True
    for i in range(2,n):
        if n % i == 0:
            # print("Number is not prime")
            is_Prime=False
            break
    if is_Prime == True:
        print("Number is Prime")
    else:
        print("Number is not prime")