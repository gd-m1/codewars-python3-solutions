# https://www.codewars.com/kata/5526fc09a1bbd946250002dc

def find_outlier(integers):
    counter = 0
    for i in integers:
        if i % 2 == 0:
            counter += 1
    if counter == 1:
        return [i for i in integers if i % 2 == 0][0]
    return [i for i in integers if i % 2 != 0][0]
