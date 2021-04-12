# https://www.codewars.com/kata/534d2f5b5371ecf8d2000a08

def multiplication_table(size):
    return [[(i + 1)*(j + 1) for j in range(size)] for i in range(size)]
