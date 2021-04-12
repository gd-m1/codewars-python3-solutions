# https://www.codewars.com/kata/526571aae218b8ee490006f4

def countBits(n):
    n = str(bin(n))[2:]
    return len(''.join(b for b in n if b == '1'))
