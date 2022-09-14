import re
src_string = 'Red car is parked right behind another car and blue building (with red walls) and blue door?\n Cat, python, tiger. Tiger, python-kiwi!'
src_string = re.sub('[()!@#$\n-.,?]', ' ', src_string)    # Удаление пунктуации
my_dict = {}

for word in src_string.lower().split():
    my_dict[word] = my_dict.get(word, 0) + 1

print([v for v in my_dict if my_dict[v] == max(my_dict.values())][-1])
