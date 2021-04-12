# https://www.codewars.com/kata/55c45be3b2079eccff00010f

def order(sentence):
    sentence = sentence.split()
    sorted_sentence = []
    index = 0
    while len(sorted_sentence) != len(sentence):
        index += 1
        for word in sentence:
            if str(index) in word:
                sorted_sentence.append(word)
    return ' '.join(word for word in sorted_sentence)