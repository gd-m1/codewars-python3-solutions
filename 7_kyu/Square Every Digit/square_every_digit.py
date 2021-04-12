# https://www.codewars.com/kata/546e2562b03326a88e000020

def square_digits(num):
    square_every_digit = ''
    for digit in str(num):
        square_digit = int(digit) ** 2
        square_every_digit += str(square_digit)
    return int(square_every_digit)
