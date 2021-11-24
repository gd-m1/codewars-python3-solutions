# https://www.codewars.com/kata/530e15517bc88ac656000716

def rot13(message):
    key = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    val = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
    trans = dict(zip(key, val))

    return ''.join(trans.get(ch, ch) for ch in message)
