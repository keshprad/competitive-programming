# Problem: https://www.codewars.com/kata/52449b062fb80683ec000024/


def generate_hashtag(s):
    if len(s) > 140 or len(s) == 0:
        return False
    else:
        s = s.split()
        res = "#"
        for word in s:
            res += word.capitalize()
        if len(res) == 1 or len(res) > 140:
            return False
        return res
