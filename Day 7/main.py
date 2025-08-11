squares = [x**2 for x in range(10)]
print(squares)

evens = [x for x in range(100) if x%2 == 0]
print(evens)

# Lambda Function
add = lambda x,y: x+y
print(add(4,5))

count_char = lambda input_string: len(input_string)
print(count_char("Dheeraj"))

#  Map function
numbers = [2,4,6,8,10]
squares = map(lambda x:x**2 ,numbers)
print(list(squares))

# filter function
numbers = [x for x in range(1,20)]
even_list = filter(lambda x: x%2 == 0 , numbers)
print(list(even_list))

# reduce function
from functools import reduce
product = reduce(lambda x,y: x*y,numbers)
print(product)

