src_string = 'red car is parked right behind another car and blue building with red walls and blue door cat python tiger tiger python kiwi'
my_dict = {}

for word in src_string.lower().split():
    my_dict[word] = my_dict.get(word, 0) + 1

# print(sorted(my_dict.items(), key=lambda x: (x[1], x[0]))[-1][0])
# print(list(v for v in my_dict if my_dict[v] == max(my_dict.values()))[-1])
# print({k: v for k, v in my_dict.items() if v == max(my_dict.values())})
print(dict(filter(lambda x: x[1] == max(my_dict.values()), my_dict.items())).popitem()[0])
