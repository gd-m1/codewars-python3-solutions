# https://www.codewars.com/kata/541c8630095125aba6000c00

def digital_root(n):
    sum = 0
    for digit in str(n):
        sum += int(digit)
    if sum < 10:
        return sum
    else:
        return digital_root(sum)
