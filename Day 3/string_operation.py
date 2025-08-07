def palindrome(a):
    a = a.lower()
    if a[:] == a[::-1]:
        return "Palindrome"
    else:
        return "not Palindrome"

def reverse_string(a):
    a = a.lower
    return a[::-1]

def count_vowel(a):
    a = a.lower()
    count = 0
    for i in a:
        if i in 'aeiou':
            count +=1 
    return count


