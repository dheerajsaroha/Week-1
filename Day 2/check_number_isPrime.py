n= int(input("Enter your number : "))
if n<=1:
    print("Number is not prime")
else:
    is_Prime = True
    for i in range(2,int(n**0.5)+1): #Starts a loop from 2 to √num (square root of the number) rounded down and incremented by 1.The reason for using square root:Any non-prime number n must have a factor less than or equal to √n.Optimizes the check instead of checking till num - 1.
        if n % i == 0:
            # print("Number is not prime")
            is_Prime=False
            break
    if is_Prime == True:
        print("Number is Prime")
    else:
        print("Number is not prime")