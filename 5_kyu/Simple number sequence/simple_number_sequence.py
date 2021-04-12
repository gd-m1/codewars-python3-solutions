# https://www.codewars.com/kata/5a28cf591f7f7019a80000de

def missing(s):
    for i in range(1, len(s)//2):
        if validate(int(s[:i]), s):
            return validate(int(s[:i]), s)
    return -1


def validate(num, s):
    result = []
    for i in range(len(s)):
        if s == '':
            break
        elif not s.startswith(str(num)):
            result.append(num)
        else:
            s = s.replace(str(num), '', 1)
        num += 1
    if len(result) == 1:
        return result[0]
    return False
