# https://www.codewars.com/kata/5ef9ca8b76be6d001d5e1c3e

import re


def encode(string):
    bits = [bin(ord(d)).replace('b', '') for d in string]
    for i in range(len(bits)):
        if len(bits[i]) < 8:
            bits[i] = '0' + bits[i]
    return ''.join([d.replace('0', '000').replace('1', '111') for d in bits])


def decode(bits):
    string = re.findall('\d{3}', bits)

    if not error_check(string):
        error_correct(string)
        
    for i in range(len(string)):
        if string[i] == '000':
            string[i] = '0'
        else:
            string[i] = '1'
    string = re.findall('\d{8}', ''.join(string))   
    string = [int(d, 2) for d in string]
    return ''.join([chr(b) for b in string])


def error_check(string):
    for _ in string:
        if _ != '000' or _ != '111':
            return False
    return True


def error_correct(string):
    for i in range(len(string)):
        if len(re.findall('0', string[i])) > len(re.findall('1', string[i])):
            string[i] = '000'
        else:
            string[i] = '111'
    return string
