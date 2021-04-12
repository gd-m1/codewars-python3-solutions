# https://www.codewars.com/kata/514a024011ea4fb54200004b

def domain_name(url):
    if 'http://' in url:
        url = url.replace('http://', '')
    if 'https://' in url:
        url = url.replace('https://', '')
    if 'www.' in url:
        url = url.replace('www.', '')
    return ''.join(url.split('.')[0])
