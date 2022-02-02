from random import randint

print('Задание 3.')

# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
# медианы, в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно, используйте метод
# сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).


m = int(input('Введите число m: '))
lst = [randint(0, 100) for i in range(2 * m + 1)]
print('Список размером 2m + 1 до сортировки:', lst)


def counting_sort(lst, largest):
    c = [0] * (largest + 1)
    for i in range(len(lst)):
        c[lst[i]] = c[lst[i]] + 1

    c[0] = c[0] - 1
    for i in range(1, largest + 1):
        c[i] = c[i] + c[i - 1]

    result = [None] * len(lst)

    for x in reversed(lst):
        result[c[x]] = x
        c[x] = c[x] - 1

    return result


k = max(lst)
sorted_list = counting_sort(lst, k)
print('Список размером 2m + 1 после сортировки: ', end='')
print(sorted_list)


def Median(sorted_list):
    if len(sorted_list) % 2 == 0:
        med_1 = int(((len(sorted_list) / 2) + ((len(sorted_list) / 2) + 1)) / (len(sorted_list)))
        return sorted_list[med_1]
    else:
        med_2 = (len(sorted_list) // 2)
        return sorted_list[med_2]


median = Median(sorted_list)
print('Медиана:', median)