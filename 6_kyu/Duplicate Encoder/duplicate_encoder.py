# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c

def duplicate_encode(word):
    result = ''
    for s in word.lower():
        if word.lower().count(s) > 1:
            result += ')'
        else:
            result += '('
    return result
