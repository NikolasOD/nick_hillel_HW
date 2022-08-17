list_of_lists = [
    [34587, 'Learning Python, Mark Lutz', 4, 40.95],
    [98762, 'Programming Python, Mark Lutz', 5, 56.80],
    [77226, 'Head First Python, Paul Barry', 3, 32.95],
    [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
]


# Это был мой первый вариант, но он не все условия задачи выполнял,
# однако получился короче поэтому решил его оставить =)
# def func(db):
#     return [(i[0], (lambda x: x < 100 and x+10 or x)(round(i[2]*i[3], 2))) for i in db]
#
#
# print(func(list_of_lists))


def func2(db):
    return list(map(lambda x: x if x[1] >= 100 else (x[0], x[1] + 10), map(lambda x: (x[0], round(x[2] * x[3], 2)), db)))


print(func2(list_of_lists))
