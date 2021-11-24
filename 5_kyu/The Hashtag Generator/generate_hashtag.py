# https://www.codewars.com/kata/52449b062fb80683ec000024

def generate_hashtag(s):
    if not s:
        return False
    result = '#' + ''.join(item for item in [word.capitalize() for word in s.split()])
    return False if len(result) > 140 else result
