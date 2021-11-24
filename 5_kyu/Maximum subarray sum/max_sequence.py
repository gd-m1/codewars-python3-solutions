# https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c

def max_sequence(arr):
    if not arr:
        return 0

    result = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if sum(arr[i:j+1]) > result:
                result = sum(arr[i:j+1])

    return result
