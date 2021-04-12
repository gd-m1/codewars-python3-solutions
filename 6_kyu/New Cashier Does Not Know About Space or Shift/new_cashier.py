# https://www.codewars.com/kata/5d23d89906f92a00267bb83d

MENU = ['Burger', 'Fries', 'Chicken', 'Pizza', 'Sandwich', 'Onionrings', 'Milkshake', 'Coke']


def get_order(order):
    result = ''
    for item in MENU:
        while item.lower() in order:
            result += item + ' '
            order = order[:order.find(item.lower())] + order[order.find(item.lower()) + len(item):]
    return result[:-1]
