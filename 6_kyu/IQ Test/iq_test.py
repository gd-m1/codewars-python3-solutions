# https://www.codewars.com/kata/552c028c030765286c00007d

def iq_test(numbers):
    numbers = numbers.split()
    even = 0
    for n in numbers:
        if int(n) % 2 == 0:
            even += 1
    if even > 1:
        for i in range(len(numbers)):
            if int(numbers[i]) % 2 != 0:
                return i + 1
    else:
        for i in range(len(numbers)):
            if int(numbers[i]) % 2 == 0:
                return i + 1
