# https://www.codewars.com/kata/523a86aa4230ebb5420001e1

def anagrams(word, words):
    return [element for element in words if sorted(element) == sorted(word)]
