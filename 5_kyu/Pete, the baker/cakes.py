# https://www.codewars.com/kata/525c65e51bf619685c000059

def cakes(recipe, available):
    count = []
    for key in recipe:
        if key not in available:
            return 0
        count.append(available[key] // recipe[key])
    return min(count)
