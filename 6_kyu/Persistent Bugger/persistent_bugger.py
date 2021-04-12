# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec

def persistence(n, count=0):
    mult = 1
    n = list(map(int, str(n)))
    if len(n) > 1:
        for num in n:
            mult *= num
        count += 1
        count = persistence(mult, count)
    return count
