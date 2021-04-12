# https://www.codewars.com/kata/526989a41034285187000de4

def ips_between(start, end):
    start, end = [int(i) for i in start.split('.')], [int(i) for i in end.split('.')]
    start_sum = start[0]*256**3 + start[1]*256**2 + start[2]*256 + start[3]
    end_sum = end[0]*256**3 + end[1]*256**2 + end[2]*256 + end[3]
    
    return end_sum - start_sum
