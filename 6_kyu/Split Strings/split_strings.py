# https://www.codewars.com/kata/515de9ae9dcfc28eb6000001

def solution(s):
    list = []
    if len(s) % 2 != 0:
        s = s + '_'
    for i in range(len(s)):
        if i % 2 == 1:
            list.append(s[i-1] + s[i])
    return list
