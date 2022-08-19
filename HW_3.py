from random import randint

M = int(input("Введите любое целое, положительное число, больше 5:"))
matrix = [[randint(1, 50) for column in range(M)] for row in range(M)]
list_of_sums = [sum([matrix[list_i][i] for list_i in range(M)]) for i in range(M)]


# Сортировка массивов
def bubble_sort(sums, array):
    # Сортировка столбцов по возрастанию сумм
    trigger = True
    while trigger:
        trigger = False
        for i in range(M-1):
            j = i + 1
            if sums[i] > sums[j]:
                sums[i], sums[j] = sums[j], sums[i]
                trigger = True
                for v in range(M):
                    array[v][i], array[v][j] = array[v][j], array[v][i]

    # Сортировка значений столбцов по возрастанию
    for f in range(M):
        # сортировка сверху вниз нечётных столбцов
        if not f % 2:
            trigger = True
            while trigger:
                trigger = False
                for i in range(M-1):
                    j = i + 1
                    if array[i][f] > array[j][f]:
                        array[i][f], array[j][f] = array[j][f], array[i][f]
                        trigger = True
        # сортировка снизу вверх чётных столбцов
        else:
            trigger = True
            while trigger:
                trigger = False
                for i in range(M-1):
                    j = i + 1
                    if array[i][f] < array[j][f]:
                        array[i][f], array[j][f] = array[j][f], array[i][f]
                        trigger = True


# Вывод в терминал
def pretty_print(sums, array):
    for r in array:
        print(*list(map('{{:>4}}'.format().format, r)))
    print(*list(map('{{:>4}}'.format().format, sums)))


print('Массив до сортировки')
pretty_print(list_of_sums, matrix)
print('<' + '====='*M + '>')
bubble_sort(list_of_sums, matrix)
print('Массив после сортировки')
pretty_print(list_of_sums, matrix)
