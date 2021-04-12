# https://www.codewars.com/kata/52685f7382004e774f0001f7

def make_readable(seconds):
    h = seconds // 60 // 60
    if len(str(h)) < 2:
        h = '0' + str(h)
    m = (seconds - int(h) * 60 * 60) // 60
    if len(str(m)) < 2:
        m = '0' + str(m)
    s = (seconds - int(h) * 60 * 60) % 60
    if len(str(s)) < 2:
        s = '0' + str(s)
    time = f'{h}:{m}:{s}'
    
    return time
