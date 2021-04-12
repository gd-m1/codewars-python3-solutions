# https://www.codewars.com/kata/52fba66badcd10859f00097e

def disemvowel(string):
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    for letter in string:
        if letter in vowels:
            string = string.replace(letter, '')
    return string
