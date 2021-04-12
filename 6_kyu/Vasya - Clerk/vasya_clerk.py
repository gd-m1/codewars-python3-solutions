# https://www.codewars.com/kata/555615a77ebc7c2c8a0000b8

def tickets(people):
    Vasya = {25: 0, 50: 0}
    for bill in people:
        if bill == 25:
            Vasya[25] += 1
        if bill == 50:
            Vasya[25] -= 1
            if Vasya[25] < 0:
                return "NO"
            Vasya[50] += 1
        if bill == 100:
            if Vasya[50] >= 1 and Vasya[25] >= 1:
                Vasya[50] -= 1
                Vasya[25] -= 1
            elif Vasya[25] >= 3:
                Vasya[25] -= 3
            else:
                return "NO"
    return "YES"
