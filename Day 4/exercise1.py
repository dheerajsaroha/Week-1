# Manipulate data in dictionary
person = {"name":"Dheeraj","age":22,"grade":"A"}

# Add a new key value
person["address"]="Mahawati,Panipat"
# print updated data
print(person)

# update age 
person["age"] = 23

print(person)

# remove grade
if "grade" in person:
    del person["grade"]
print(person)