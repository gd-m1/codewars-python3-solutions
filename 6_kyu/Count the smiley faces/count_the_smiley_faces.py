# https://www.codewars.com/kata/583203e6eb35d7980400002a

def count_smileys(arr):
    smiles = [':)', ':-)', ':~)', ';)', ';-)', ';~)', ':D', ':-D', ':~D', ';D', ';-D', ';~D']
    count = 0
    for smile in arr:
        if smile in smiles:
            count += 1
    return count
