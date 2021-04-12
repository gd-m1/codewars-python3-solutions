#https://www.codewars.com/kata/5693239fb761dc8670000001

result = []


def find_additive_numbers(num):
    n = len(num)
    for i in range(1, n):
        for j in range(i+1, n+1):
            num1, num2, num3 = num[:i], num[i:j], num[j:]
            result.clear()
            result.append(num1)
            result.append(num2)
            if validation(num1, num2, num3):
                return result
    return []


def validation(num1, num2, num3):
    if (len(num1) > 1 and num1[0] == '0') or (len(num2) > 1 and num2[0] == '0'):
        return False
    sum = str(int(num1) + int(num2))
    if sum == num3:
        result.append(sum)
        return True
    elif num3.startswith(sum):
        result.append(sum)
        return validation(num2, sum, num3[len(sum):])
    return False
