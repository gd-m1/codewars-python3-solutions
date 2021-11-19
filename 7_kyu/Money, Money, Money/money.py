# https://www.codewars.com/kata/563f037412e5ada593000114

def calculate_years(principal, interest, tax, desired):
    if desired == principal:
        return 0
    years = 0
    while principal <= desired:
        interest_sum = principal * interest
        principal += interest_sum - interest_sum * tax
        years += 1
    return years
