# https://www.codewars.com/kata/520b9d2ad5c005041100000f

def pig_it(text):
    result = []
    delimiters = ['!', ';', ':', '.', ',', '?']
    for word in text.split():
        if word not in delimiters:
            result.append(word[1:] + word[:1] + 'ay')
        else:
            result.append(word)
    return ' '.join(s for s in result)
