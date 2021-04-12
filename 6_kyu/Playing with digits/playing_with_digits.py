# https://www.codewars.com/kata/5552101f47fc5178b1000050

def dig_pow(n, p):
    N = list(map(int, str(n)))
    sum = 0
    for num in N:
        sum += num ** p
        p += 1
    if sum % n == 0:
        return sum / n
    else:
        return -1
