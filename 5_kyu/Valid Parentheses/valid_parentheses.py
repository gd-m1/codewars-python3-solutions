# https://www.codewars.com/kata/52774a314c2333f0a7000688

def valid_parentheses(string):
    count = 0
    for ch in string:
        if ch == '(':
            count += 1
        elif ch == ')':
            count -= 1
        if count < 0:
            return False
    return count == 0
