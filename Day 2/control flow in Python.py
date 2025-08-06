# # Control flow in Python
# num = 14
# if num>0:
#     print("Number is positive")
# else:
#     print("Negative")

# # Using Ternary Operator
# res="Positive" if num>0 else "Negative"
# print(res)

# # Nested Loop
# if num > 0:
#     if num >18:
#         print("Can vote")
#     else:
#         print("Not eligible for vote")
# else:
#     print("Enter a positive Value")

# # Loops in Python
# arr = [1,2,3,4,5]
# for i in arr:
#     print(i)
# arr.append(10)
# print(arr)
count = 5
while count > 0:
    print(count)
    count -= 1
print("While loop completed")
# Using break and continue statement
for i in range(10):
    if i == 3:
        continue
    if i == 5:
        break
    print(i)
    
print("Outside the loop")

