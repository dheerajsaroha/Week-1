def count_vowels(txt):
    vowel = 'aeiou'
    count = 0
    txt = txt.lower()
    for i in txt:
        if i in vowel:
            count +=1
        else:
            count = count
    return count

input_txt = input("Enter the input")
print(count_vowels(input_txt))