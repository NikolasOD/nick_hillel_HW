# Чтение исходного файла
with open('src_14.txt', 'r') as src_file:
    data = [line.split() for line in src_file.readlines()]

# Создание словаря: ключ - имя студента, значение - оценка
dict_of_students = {s[1] + ' ' + s[0][0] + '.': round(sum(map(int, s[2:]))/len(s[2:]), 2) for s in data}


# Вывод на экран, с соблюдением выравнивания
def pretty_print(student, rate):
    return student + " "*(20-len(student)) + str(rate)


# Вывод плохих студентов
def get_bad_students(students):
    print("Учащиеся, чей средний балл меньше 5:")
    for s, r in students.items():
        if r < 5:
            print(pretty_print(s, r))


# Расчёт среднего балла
def get_average_rate(students):
    return round(sum(students.values())/len(students.values()), 2)


# Вывод в терминал
get_bad_students(dict_of_students)
print(f"Средний балл по классу: {get_average_rate(dict_of_students)}")

# Запись нового файла со списком учащихся и оценками
with open('students.txt', 'w') as new_file:
    for s, r in dict_of_students.items():
        new_file.write(pretty_print(s, r)+"\n")
