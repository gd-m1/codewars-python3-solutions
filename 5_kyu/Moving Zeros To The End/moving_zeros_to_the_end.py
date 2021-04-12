# https://www.codewars.com/kata/52597aa56021e91c93000cb0

def multiplication_table(size):
    return [[(i + 1)*(j + 1) for j in range(size)] for i in range(size)]
