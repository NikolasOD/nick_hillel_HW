src_string = 'red car is parked right behind another car and blue building with red walls and blue door cat python tiger tiger python kiwi'
my_dict = {}

for word in src_string.lower().split():
    my_dict[word] = my_dict.get(word, 0) + 1

print([v for v in my_dict if my_dict[v] == max(my_dict.values())][-1])
