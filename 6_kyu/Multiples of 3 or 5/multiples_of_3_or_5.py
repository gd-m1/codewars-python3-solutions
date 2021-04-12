# https://www.codewars.com/kata/514b92a657cdc65150000006

def solution(number):
    sum = 0
    for n in range(number):
        if n % 3 == 0 or n % 5 == 0:
            sum += n
    return sum
