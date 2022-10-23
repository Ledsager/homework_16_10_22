# Задайте последовательность чисел. Напишите программу, которая выведет
# список неповторяющихся элементов исходной последовательности.

def input_mas():
    mas = []
    mas = [int(i) for i in input().split()]
    return mas


print('Введите массив переменных : ')
list_a = input_mas()
# первый вариант. Неповторяющиеся элементы.
single_element_list_a = []
for i in range(len(list_a)):
    if (list_a.count(list_a[i]) == 1):
        single_element_list_a.append(list_a[i])
print('Неповторяющиеся элементы: ', single_element_list_a)

# второй вариант. Выводит элементы по 1 разу.
single_element_list_a = [list_a[0]]
for i in range(len(list_a)):
    if (list_a[i] not in single_element_list_a):
        single_element_list_a.append(list_a[i])
print('Массив без повторяющихся элементов: ', single_element_list_a)
