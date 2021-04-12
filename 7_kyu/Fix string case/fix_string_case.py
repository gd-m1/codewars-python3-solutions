# https://www.codewars.com/kata/5b180e9fedaa564a7000009a

def solve(s):
    upper = 0
    for letter in s:
        if letter.isupper():
            upper += 1
    if upper > len(s) * 0.5:
        return s.upper()
    else:
        return s.lower()
