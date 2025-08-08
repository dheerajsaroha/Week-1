# write a program to reverse a list and remove duplicates using a set

numbers = [1,3,5,2,3,4,6,7,4,8,9]
temp_set = set()
for i in numbers:
    temp_set.add(i)
updated_list =list(temp_set)
updated_list.reverse()
print(updated_list)



