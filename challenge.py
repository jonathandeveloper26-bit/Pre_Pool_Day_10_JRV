# Create a program that takes an integer N as an argument and counts 
# how many letters would be used if all the numbers from 1 to N (included) 
# were written out in words.

from num2words import num2words

def count_letters(N: int):
    letters = 0
    try:
        for i in range(1,N+1):
            letters += len(num2words(i).replace(" ", "").replace("-",""))
    except Exception as e:
        return e
    return letters

print(count_letters(42))