# https://www.codewars.com/kata/54ff3102c1bad923760001f3

def getCount(sentence):
    return len(list(filter(lambda letter: letter in ('a', 'e', 'i', 'o', 'u'), sentence)))
